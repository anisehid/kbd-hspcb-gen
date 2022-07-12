#!/usr/bin/env python3
# coding: utf-8

import os
import sys
from collections import defaultdict
from pprint import pprint
import json
from skidl import (
    Net,
    Part,
    Pin,
    generate_netlist,
    TEMPLATE,
    SchLib,
    SKIDL,
    lib_search_paths
)

skidl_lib = SchLib('lib_sklib.py', tool=SKIDL)  # Create a SKiDL library object from the new file.

# switch = Part(skidl_lib, 'MX', TEMPLATE, footprint="Keyboard:MXHS-1U", tool=SKIDL)
switch = Part(skidl_lib, 'MX_LED', TEMPLATE, footprint="Keyboard:MXHS-1U-RGB-ALI-3528-HOLE-NOPAD", tool=SKIDL)
btbconn = Part(skidl_lib, 'BTB', TEMPLATE, footprint="Keyboard:30PIN_0.4MM_BTB_MALE", tool=SKIDL)


x = "X"
default_desc = {
    "name" : "default",
    "layout" : [
    #esc 1  2  3  4  5  6      7  8  9  0  -  = bks
    [4,  4, 4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 8],
    #tab q  w  e  r  t       y  u  i  o  p  [  ] \
    [6,  4, 4, 4, 4, 4, -2,  4, 4, 4, 4, 4, 4, 4, 6],
    #cap a  s  d  f  g      h  j  k  l  ;  '  ret
    [7,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 4, 9],
    #LSH z  x  c  v  b      n  m  ,  .  /  rsh
    [9,  4, 4, 4, 4, 4, -2, 4, 4, 4, 4, 4, 11],
    #_   C  W  A  S  *       S  A  W  F  C  _
    ["2", 5, 5, 5, 8, 4, -2, 8, 5, 5, 5, 5, "3"]
    ],
    "num_rc": [5, 14],
    "key_matrix": [
    # esc   1     2     3     4     5   / 6   / 7     8     9      0      -      =      bks
    [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[1,13],[1,14]],
    # tab    q     w     e     r     t   / y     u     i     o      p      [      ]      \
    [[2,1], [2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[2,9],[2,10],[2,11],[2,12],[2,13],[2,14]],
    # cap      a     s     d     f     g   / h     j     k     l      ;      '           ret
    [[3,1],   [3,2],[3,3],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[3,10],[3,11],[3,12],     [3,14]],
    # lsh         z     x     c     v     b   / n     m     ,      .      /             rsh
    [[4,1],      [4,3],[4,4],[4,5],[4,6],[4,7],[4,8],[4,9],[4,10],[4,11],[4,12],        [4,14]],
    #LCTL  LWIN  LALT         S           *   / S     RFUN         RWIN   MENU   RCTL
    [[5,1],[5,2],[5,3],      [5,6],      [5,7],[5,8],[5,9],       [5,11],[5,12],[5,13]],
    ],
    "led_conn": [
        ["led1",17,16,15,14,13,12,11,21,22,23,24,25,26,36,35,34,33,32,31,41,43,44,45,46,47,57,56,53,52,51],
        ["led2",17,18,19,110,111,112,113,114,214,213,212,211,210,29,28,27,37,38,39,310,311,312,314,414,412,411,410,49,48,58,59,511,512,513],
    ],
    "conn_def": [
        #    1     2  3  4     5  6  7  8
        ["VCC","GND", x, x,"led1", x, x, x,
        "r1", "r2", "r3", "r4", "r5", x, # 14
        "c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", # 22
        x, x, x, x, x, x, x, x], #30
        #    1     2  3  4     5  6  7  8
        ["VCC","GND", x, x,"led2", x, x, x,
        "r1", "r2", "r3", "r4", "r5", x, # 14
        "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14", # 22
        x, x, x, x, x, x, x, x] #30
    ],
}

def r_c_num_to_str(r_num, c_num): return str(r_num) + str(c_num)
def rc_num_to_r_c_num(rc_num): return int(str(rc_num)[0]), int(str(rc_num)[1:])

def keymapidx_to_posmapidx_transdict(key_map):
    trans_dict = {}
    for r_id, row in enumerate(key_map):
        for c_id, key in enumerate(row):
            r, c = key
            tran_key = "%d%d" % (r, c)
            trans_dict[tran_key] = [r_id, c_id]

    return trans_dict

def gen_layoutdesc(sch_desc, row4_lshift=False, led_pos_up=False):
    #### prepare layout_desc  ####
    trans_dict = keymapidx_to_posmapidx_transdict(sch_desc["key_matrix"])

    MM_PER_INCH = 25.4
    KEY_DIST = 0.75 * MM_PER_INCH
    esc_key_cx_cy = (2.8125 * MM_PER_INCH, 2.90625 * MM_PER_INCH)
    ### calc key pos and sat pos
    key_pos = esc_key_cx_cy
    stabilizer_type = "pcb"
    # if modifier is None:
    # modifier = {}

    key_locs = []
    sat_locs = []
    for row_idx, row in enumerate(sch_desc["layout"]):
        key_locs.append([])
        for col_idx, col in enumerate(row):
            if type(col) is str:
                col = int(col)
            elif col < 0:
                col = 0 # -col  skip split gap
            else:
                # try:
                #     mod = modifier[(row_idx, col_idx)]
                #     rotate_deg = mod[0]
                #     width      = mod[1]
                #     mov_x      = mod[2][0]
                #     mov_y      = mod[2][1]
                # except:
                width = col
                rotate_deg = 0
                mov_x = 0
                mov_y = 0

                center_pos = (key_pos[0] + (col - 4) / 4 * KEY_DIST / 2 + mov_x / 4.0 * KEY_DIST,
                              key_pos[1] + (mov_y / 4.0) * KEY_DIST)
                key_locs[-1].append(center_pos)

                if col >= 8:  # sat axis
                    rev_sat_axis=(True if (row_idx == len(sch_desc["layout"]) - 1 and rotate_deg == 0) else False)
                    sat_locs.append([center_pos[0] - 0.46875 * MM_PER_INCH, center_pos[1], 180 if rev_sat_axis else 0])
                    sat_locs.append([center_pos[0] + 0.46875 * MM_PER_INCH, center_pos[1], 180 if rev_sat_axis else 0])
            key_pos = key_pos[0] + col / 4 * KEY_DIST, key_pos[1]

        # try:
        #     row_height = modifier[(row_idx,)][0] / 4.0 * KEY_DIST
        # except:
        row_height = KEY_DIST
        key_pos = esc_key_cx_cy[0], key_pos[1] + row_height

    layout_desc = {
        "name": sch_desc["name"],
        "trans_dict": trans_dict,
        "key_pos": key_locs,
        "sat_pos": sat_locs,
        "row4_lshift": row4_lshift,
        "led_pos_up": led_pos_up
    }

    with open(sch_desc["name"]+"_layoutdesc.json", "w") as f:
        json.dump(layout_desc, f)


def check_sch_desc(desc):
    assert "name" in desc           # str
    ### for case generation
    assert "layout"   in desc     # layout: [[width, width, ...]]  width in 1u 1.25u ...
    ### for netlist generation
    assert "num_rc"      in desc  # num_rc: (num_row, num_col)
    assert "key_matrix"  in desc  # matrix: [[(ROW, COL), ...]]        ROW/COL count from 1
    assert "led_conn"    in desc  # led_conn: [(SW_ID1, SW_ID2), ...]  SW_ID1 out to SW_ID2 in, SW_ID1 is NONE, from conn,
    assert "conn_def"    in desc  # conn_def: ["net1", "net2", ...]    conn_def[i]  (i+1) pin netname

    ### generated from layout above
    ### for pcb layout generation
    # assert "led_pos_up"  in desc  # led_pos_up: bool
    # assert "row4_lshift" in desc  # bool
    # assert "key_pos"  in desc     # layout: [[(X, Y, rot), ...]]  X, Y unit mm  rot
    # assert "sat_pos"  in desc     # layout: [[(X, Y, rot), ...]]  X, Y unit mm  rot


def gen_netlist(desc):
    check_sch_desc(desc)
    name = desc["name"]

    # nets = defaultdict(Net)
    nets = {}
    num_row, num_col = desc["num_rc"]
    for i in range(1, num_row+1):
        name = "r%d" % (i)
        nets[name] = Net(name)
    for i in range(1, num_col+1):
        name = "c%d" % (i)
        nets[name] = Net(name)
    nets["VCC"] = Net("VCC")
    nets["GND"] = Net("GND")

    # conn generation
    btb_conns = []
    for i, conn_def in enumerate(desc["conn_def"]):
        btb_conns.append(btbconn(ref="CN%d" % (i + 1)))
        assert len(conn_def) == 30
        for n, pin_name in enumerate(conn_def):
            pin_id = str(n + 1)
            if pin_name == "X":
                # btb_conns[i][pin_id] = False
                pass
            else:
                if pin_name in nets:
                    nets[pin_name] += btb_conns[i][pin_id]
                else:
                    nets[pin_name] = Net(pin_name)

    # key generation
    key_map = {}
    for key_row in desc["key_matrix"]:
        for key in key_row:
            r_id, c_id = key
            name = "S" + r_c_num_to_str(r_id, c_id)
            key_map[name] = switch(ref=name)
            nets["c%d" % c_id] += key_map[name]["1"]
            nets["r%d" % r_id] += key_map[name]["2"]
            nets["VCC"]        += key_map[name]["VCC"]
            nets["GND"]        += key_map[name]["GND"]

    # led conn generation
    for i, led_con_def in enumerate(desc["led_conn"]):
        print("======================")
        last_node_name = led_con_def[0]
        last_node = btb_conns[i][desc["conn_def"][i].index(last_node_name) + 1]
        for node_id in led_con_def[1:]:
            wire_name = "%s_%s" % (last_node_name, str(node_id))
            nets[wire_name] = Net(wire_name)
            nets[wire_name] += last_node
            nets[wire_name] += key_map["S%d" % (node_id)]["DI"]
            last_node_name = "S%d" % node_id
            last_node = key_map["S%d" % (node_id)]["DO"]

    # print(key_map)
    # s1 = switch(ref="S1")
    # btb_l = btbconn(ref="CN1")

    # r = Net("R1")
    # r += s1['1'], btb_l["3"]

    # r = Net("R2")
    # r += s1['GND'], btb_l["5"]

    # vcc += btb_l["1"]
    # vcc += s1["VCC"]
    # vcc += s1["2"]

    generate_netlist()

    # copy netlist to pcb project
    os.system("mv sch.net dest.net")


def check_pos_desc(desc):
    assert "name" in desc           # str

    ### generated from layout above
    ### for pcb layout generation
    assert "led_pos_up"  in desc  # bool default False
    assert "row4_lshift" in desc  # bool default False
    assert "trans_dict"  in desc  # S12 -> [0, 1] mapping
    assert "key_pos"  in desc     # layout: [[(X, Y), ...]]  X, Y unit mm
    assert "sat_pos"  in desc     # layout: [[(X, Y, rot), ...]]  X, Y unit mm  rot


import lib_pcbelem
def adjust_pcb(pcb_file, pos_desc_file):
    with open(pos_desc_file, "r") as desc_file:
        pos_desc = json.load(desc_file)
        check_pos_desc(pos_desc)
    print(pos_desc)

    pcb_lines = None
    with open(pcb_file, "r") as pcb_ro:
        pcb_lines = pcb_ro.read().split("\n")

    # adjust position of keys and conns
    new_pcb_lines = []
    state = "IDLE" # /"FP"
    fp_type = None # "SW"/"BTB"
    new_pos = None
    for l in range(len(pcb_lines) - 2):
        curr_line = pcb_lines[l]
        if state == "IDLE" and '(footprint "Keyboard' in curr_line:
            state = "FP"
            if "-1U-" in curr_line:
                fp_type = "SW"
            elif "BTB_MALE" in curr_line:
                fp_type = "BTB"
            else: assert False
            # find new pos for elem, find ref name
            l_fw = 1
            while "fp_text reference" not in pcb_lines[l + l_fw]:
                l_fw += 1
            ref_name = pcb_lines[l + l_fw].split('"')[1]
            if fp_type == "SW":
                new_pos_r, new_pos_c = pos_desc["trans_dict"][ref_name[1:]]
                new_pos = pos_desc["key_pos"][new_pos_r][new_pos_c]
            elif fp_type == "BTB":
                if ref_name == "CN1":
                    new_pos = [138.1125, 83.25]
                elif ref_name == "CN2":
                    new_pos = [252.4125, 83.25]
                else: assert False

        elif state == "FP" and '  )' == curr_line:
            state = "IDLE"
            fp_type = None
            new_pos = None
        else: pass  # state unchange


        if new_pos is not None and "  (at " in curr_line:
            if fp_type == "SW":
                new_pcb_lines.append("  (at %f %f %d)" % (new_pos[0], new_pos[1], 0 if pos_desc["led_pos_up"] else 180))
            elif fp_type == "BTB":
                new_pcb_lines.append("  (at %f %f)" % (new_pos[0], new_pos[1]))
        else:
            new_pcb_lines.append(curr_line)

    # print(pcb_lines[-5:-2])

    # add sat axis
    for sat_pos in pos_desc["sat_pos"]:
        x, y, rot = sat_pos
        new_pcb_lines.append(lib_pcbelem.mxst_tmpl % ("%f %f %d" % (x, y, rot)))
    # add split holes
    if pos_desc["row4_lshift"]:
        new_pcb_lines.append(lib_pcbelem.split_hole_lshift)
    else:
        new_pcb_lines.append(lib_pcbelem.split_hole_normal)
    # add mount holes
    new_pcb_lines.append(lib_pcbelem.padded_holes)
    # edge cut
    new_pcb_lines.append(lib_pcbelem.edgecut)


    new_pcb_lines.append(")")
    new_pcb_lines.append("")

    with open(pcb_file, "w") as pcb_w:
        pcb_w.write("\n".join(new_pcb_lines))

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(sys.argv[0])
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Print debug info'
    )
    subparsers = parser.add_subparsers(dest='command')
    sch = subparsers.add_parser('sch', help='generate sch and pos')
    # blame.add_argument('name', nargs='+', help='name(s) to blame')

    adjpcb = subparsers.add_parser('adjpcb', help='adjust generated pcb')
    adjpcb.add_argument('pcb_file', help='name of pcb_file (.kicad_pcb)')
    adjpcb.add_argument('pos_file', help='path to pos_file (.json)')
    args = parser.parse_args()
    if args.debug:
        print("debug: " + str(args))
    if args.command == 'sch':
       gen_netlist(default_desc)
       gen_layoutdesc(default_desc)
    elif args.command == 'adjpcb':
        adjust_pcb(args.pcb_file, args.pos_file)

    # cleanup temp files
    os.system("rm sch.log sch.erc sch_lib_sklib.py")
    os.system("rm -rf __pycache__")
