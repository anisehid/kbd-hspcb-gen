#!/usr/bin/env python3
# coding: utf-8

import os
import sys
from collections import defaultdict
from pprint import pprint
import json
import math
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
pinheader = Part(skidl_lib, 'P', TEMPLATE, footprint='Connector_PinHeader_2.00mm:PinHeader_1x04_P2.00mm_Vertical', tool=SKIDL)
MM_PER_INCH = 25.4

def get_output_dir_from_name(name):
    if not os.path.exists(name):
        print("dir %s does not exists" % (name))
        sys.exit(1)
        #os.system("mkdir %s" % (name))
    elif not os.path.isdir(name):
        print("%s exists but is not a dir" % (name))
        sys.exit(1)
    else:
        output_dir = name
    return output_dir

def r_c_num_to_str(r_num, c_num): return str(r_num) + str(c_num)
def rc_num_to_r_c_num(rc_num): return int(str(rc_num)[0]), int(str(rc_num)[1:])

def keymapidx_to_posmapidx_transdict(key_map):
    trans_dict = {}
    for r_id, row in enumerate(key_map):
        for c_id, key in enumerate(row):
            r, c = key
            tran_key = "%d%d" % (r, c)
            trans_dict[tran_key] = (r_id, c_id)

    return trans_dict

def gen_layoutdesc(sch_desc, row4_lshift=False, led_pos_up=False):
    name = sch_desc["name"]
    output_dir = get_output_dir_from_name(name)

    #### prepare layout_desc  ####
    trans_dict = keymapidx_to_posmapidx_transdict(sch_desc["key_matrix"])
    rev_trans_dict = {}
    for k, v in trans_dict.items(): rev_trans_dict[v] = k

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
                              key_pos[1] + (mov_y / 4.0) * KEY_DIST,
                              180 if led_pos_up else 0) # rotate
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

    with open(output_dir + "/%s_posdesc.json" % (name), "w") as f:
        json.dump(layout_desc, f)

    ########### bom pos handle ###########
    bom_items = {"1N4148": ["SOD-323", ""],
                 "CONN2x15": ["2x15pin_0.4", ""],
                 "KHHS": ["HS1U", ""],
                 "led2812": ["3528-rev", ""],
                 "cap0603": ["C0603", ""]}
    bom_array = {"1N4148": [], "CONN2x15": [], "KHHS": [], "led2812": [], "cap0603": []}
    pos_items = []

    # add conn
    bom_array["CONN2x15"] += ["CN1", "CN2"]
    pos_items += [
        ["J1","Conn_02x15_Odd_Even","30PIN_0.4MM_BTB_MALE",138.112500,83.250000,0.000000,"bottom"],
        ["J2","Conn_02x15_Odd_Even","30PIN_0.4MM_BTB_MALE",252.412500,83.250000,0.000000,"bottom"]
    ]
    def add_d(pos_items, ref_suf, cx, cy, rot):
        bom_array["1N4148"].append("D" + ref_suf)
        pos_items.append(["D" + ref_suf, "1N4148", "SOD-323", cx, cy, rot, "bottom"])
    def add_l(pos_items, ref_suf, cx, cy, rot):
        bom_array["led2812"].append("LED" + ref_suf)
        pos_items.append(["LED" + ref_suf, "led2812", "3528-rev", cx, cy, rot, "bottom"])
    def add_h(pos_items, ref_suf, cx, cy, rot):
        bom_array["KHHS"].append("S" + ref_suf)
        pos_items.append(["S" + ref_suf, "hssocket", "kh1u", cx, cy, rot, "bottom"])
    def add_c(pos_items, ref_suf, cx, cy, rot):
        bom_array["KHHS"].append("S" + ref_suf)
        pos_items.append(["C" + ref_suf, "capacitor", "c0603", cx, cy, rot, "bottom"])

    for rid, row in enumerate(key_locs):
        for cid, key in enumerate(row):
            ref_name_suffix = rev_trans_dict[(rid, cid)]

            cx, cy, rot = key
            cos_rot = math.cos((rot / 180) * math.pi)
            sin_rot = math.sin((rot / 180) * math.pi)

            diode_offX, diode_offY = 5.355607, -2.009679
            led_offX, led_offY = 0, 5.08
            hs_offX, hs_offY = 0, -5.08
            cap_offX, cap_offY = 4.12, 4.355

            d_cx = cx + cos_rot * diode_offX
            d_cy = cy + cos_rot * diode_offY
            l_cx = cx + cos_rot * led_offX
            l_cy = cy + cos_rot * led_offY
            h_cx = cx + cos_rot * hs_offX
            h_cy = cy + cos_rot * hs_offY
            c_cx = cx + cos_rot * cap_offX
            c_cy = cy + cos_rot * cap_offY
            add_d(pos_items, ref_name_suffix, d_cx, d_cy, rot)
            add_l(pos_items, ref_name_suffix, l_cx, l_cy, rot)
            add_h(pos_items, ref_name_suffix, h_cx, h_cy, rot)
            add_c(pos_items, ref_name_suffix, c_cx, c_cy, rot)

    # to bom/pos file
    with open(output_dir + "/%s_bom.csv" % (name), "w") as f:
        bom_header = ['"Comment"', '"Designator"', '"Footprint"', '"PartNumber"']
        f.write(",".join(bom_header) + "\n")
        for k, v in bom_items.items():
            f.write(('"%s","%s,","%s","%s"' % (k, ",".join(bom_array[k]), v[0], v[1])) + "\n")
    with open(output_dir + "/%s_pos.csv" % (name), "w") as f:
        pos_header = ["Designator", "Val", "Package", "Mid X", "Mid Y", "Rotation", "Layer"]
        f.write(", ".join(pos_header) + "\n")
        for item in pos_items:
            for col in item[:-1]:
                if type(col) == str:
                    f.write('"%s", ' % (col))
                else:
                    f.write(str(col) + ", ")
            f.write('"%s"\n' % (item[-1]))


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
    name = desc["name"]
    output_dir = get_output_dir_from_name(name)

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

    pinheader_left  = pinheader(ref="P1")
    pinheader_right = pinheader(ref="P2")
    # I2c pin header
    nets["sdaR"] = Net("sdaR")
    nets["sdaL"] = Net("sdaL")
    nets["sclR"] = Net("sclR")
    nets["sclL"] = Net("sclL")
    nets["GND"] += pinheader_left["1"]
    nets["VCC"] += pinheader_left["2"]
    nets["sclL"] += pinheader_left["3"]
    nets["sdaL"] += pinheader_left["4"]
    nets["GND"] += pinheader_right["1"]
    nets["VCC"] += pinheader_right["2"]
    nets["sclR"] += pinheader_right["3"]
    nets["sdaR"] += pinheader_right["4"]

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
            nets["VCC"]        += key_map[name]["CP"]
            nets["GND"]        += key_map[name]["CN"]

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
    os.system("mv sch.net %s/gen.net" % (output_dir))



def check_pos_desc(desc):
    assert "name" in desc           # str

    ### generated from layout above
    ### for pcb layout generation
    assert "led_pos_up"  in desc  # bool default False
    assert "row4_lshift" in desc  # bool default False
    assert "trans_dict"  in desc  # S12 -> [0, 1] mapping
    assert "key_pos"  in desc     # layout: [[(X, Y), ...]]  X, Y unit mm
    assert "sat_pos"  in desc     # layout: [[(X, Y, rot), ...]]  X, Y unit mm  rot

def gen_mount_hole(hole_desc):
    holes_pcb = []
    for hole in hole_desc:
        x, y, attr = hole
        if "skip" in attr: continue
        if "padded" in attr:
            holes_pcb.append(lib_pcbelem.mounthole2d5mmpadded_tmpl % ("%f %f" % (x, y)))
        else:
            holes_pcb.append(lib_pcbelem.mounthole2d5mm_tmpl % ("%f %f" % (x, y)))
    return holes_pcb


import lib_pcbelem
def adjust_pcb(pcb_file, pos_desc_file):
    with open(pos_desc_file, "r") as desc_file:
        pos_desc = json.load(desc_file)
        check_pos_desc(pos_desc)
    print(pos_desc)

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
                    new_pos = [138.1125, 83.25, 0]
                elif ref_name == "CN2":
                    new_pos = [252.4125, 83.25, 0]
                else: assert False

        elif state == "FP" and '  )' == curr_line:
            state = "IDLE"
            fp_type = None
            new_pos = None
        else: pass  # state unchange


        if new_pos is not None and "  (at " in curr_line:
            if fp_type == "SW":
                new_pcb_lines.append("  (at %f %f %d)" % (new_pos[0], new_pos[1], new_pos[2]))
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
    # edge cut
    new_pcb_lines.append(lib_pcbelem.edgecut)
    # add mount holes
    new_pcb_lines.append(lib_pcbelem.padded_holes)

    # attribute
    # skip:   do not generate hole on pcb
    # padded: generate pcb hole with pad ring
    holes = [
        # left most (move right)
        (87.4893, 92.5208, "left skip"),
        (63.7489 + 1.5, 121.1212, "left skip"),
        # left top
        (80.9625,  73.81875, "left"),
        (157.1625, 73.81875, "left"),
        (176.2125, 73.81875, "left"),
        # left mid
        (128.58751, 102.1, "left"),
        (147.63751, 102.1, "left padded"),
        (166.68751, 102.1, "left"),
        # left mid low
        (104.775,  135.89, "left"),
        (142.875,  135.89, "left padded"),
        (180.975,  135.89, "left"),
        # right top
        (195.2625, 73.81875, "right"),
        (214.3125, 73.81875, "right"),
        (309.5625, 73.81875, "right"),
        # right mid
        (204.7875,  102.1, "right "),
        (228.6   ,  102.1, "right padded"),
        (261.93749, 102.1, "right"),
        # right mid low
        (219.075,  135.89, "right"),
        (257.175,  135.89, "padded"),
        (295.275,  135.89, "right"),
        # right most (move left)
        (322.3399, 92.5208, "right skip"),
        (345.8312 - 1.5, 121.1212, "right skip"),

        # side holes
        (63.7489 + 1.42,  121.1212 - 0.75 * 2 * MM_PER_INCH + 4.5, "left"),
        (63.7489 + 1.42,  121.1212 - 0.75 * 1 * MM_PER_INCH + 0  , "left"),
        (63.7489 + 1.42,  121.1212 + 0.75 * 1 * MM_PER_INCH + 4.5, "left"),
        (345.8312 - 1.42, 121.1212 - 0.75 * 2 * MM_PER_INCH + 4.5, "right"),
        (345.8312 - 1.42, 121.1212 - 0.75 * 1 * MM_PER_INCH + 0  , "right"),
        (345.8312 - 1.42, 121.1212 + 0.75 * 1 * MM_PER_INCH + 4.5, "right"),
    ]
    new_pcb_lines += gen_mount_hole(holes)

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
    sch.add_argument('desc', help='keyboard description')

    adjpcb = subparsers.add_parser('adjpcb', help='adjust generated pcb')
    adjpcb.add_argument('pcb_file', help='name of pcb_file (.kicad_pcb)')
    adjpcb.add_argument('pos_file', help='path to pos_file (.json)')
    args = parser.parse_args()
    print(args)

    if args.debug:
        print("debug: " + str(args))
    if args.command == 'sch':
        with open(args.desc) as f: desc = json.load(f)
        print(desc)
        check_sch_desc(desc)

        gen_netlist(desc)
        gen_layoutdesc(desc, led_pos_up=True)
    elif args.command == 'adjpcb':
        adjust_pcb(args.pcb_file, args.pos_file)

    # cleanup temp files
    os.system("rm -f sch.log sch.erc sch_lib_sklib.py")
    os.system("rm -rf __pycache__")
