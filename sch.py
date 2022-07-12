#!/usr/bin/env python3
# coding: utf-8

import os
from collections import defaultdict
from pprint import pprint
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

def check_layout_desc(desc):
    assert "name" in desc           # str
    ### for case generation
    # assert "layout"   in desc     # layout: [[width, width, ...]]  width in 1u 1.25u ...
    ### for netlist generation
    # assert "num_rc"      in desc  # num_rc: (num_row, num_col)
    # assert "key_matrix"  in desc  # matrix: [[(ROW, COL), ...]]        ROW/COL count from 1
    # assert "led_conn"    in desc  # led_conn: [(SW_ID1, SW_ID2), ...]  SW_ID1 out to SW_ID2 in, SW_ID1 is NONE, from conn, 
    # assert "conn_def"    in desc  # conn_def: ["net1", "net2", ...]    conn_def[i]  (i+1) pin netname
    # assert "led_pos_up"  in desc  # led_pos_up: bool

    ### generated from layout above
    ### for pcb layout generation
    # assert "row4_lshift" in desc  # bool
    # assert "key_pos"  in desc     # layout: [[(X, Y, rot), ...]]  X, Y unit mm  rot
    # assert "sat_pos"  in desc     # layout: [[(X, Y, rot), ...]]  X, Y unit mm  rot


def gen_netlist(desc):
    check_layout_desc(desc)
    name = desc["name"]

    nets = defaultdict(Net)
    row_nets = []
    col_nets = []

    vcc = Net("VCC")
    gnd = Net("GND")


    s1 = switch(ref="S1")
    btb_l = btbconn(ref="CN1")

    r = Net("R1") 
    r += s1['1'], btb_l["3"]

    r = Net("R2") 
    r += s1['GND'], btb_l["5"]

    vcc += btb_l["1"]
    vcc += s1["VCC"]
    vcc += s1["2"]

    generate_netlist()

    # copy netlist to pcb project
    os.system("mv sch.net dest.net")
    os.system("rm sch.log sch.erc sch_lib_sklib.py")

desc = {"name" : "default"}
gen_netlist(desc)
