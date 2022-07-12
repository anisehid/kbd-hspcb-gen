
# padded_holes, split_hole_normal, split_hole_lshift

mxst_tmpl = """
  (footprint "Keyboard:MXST" (layer "F.Cu")
    (tedit 5715303E) (tstamp 3d73b81f-64a7-4404-8441-ccec743f36c0)
    (at %s)
    (attr through_hole)
    (fp_text reference "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp ccc07ef9-6d63-4c05-b00e-5dfe3eb4c6f2)
    )
    (fp_text value "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 2d7eb3a0-fcc4-4320-89a3-131452e111a2)
    )
    (fp_line (start -3.429 10.668) (end 3.429 10.668) (layer "F.SilkS") (width 0.381) (tstamp 4ad43157-3ef0-4d9c-b1f0-e9129d72a9e8))
    (fp_line (start 3.429 10.668) (end 3.429 -8.001) (layer "F.SilkS") (width 0.381) (tstamp e7b1826b-ed4f-4a24-b1e5-aa7bda89e118))
    (fp_line (start -3.429 -8.001) (end -3.429 10.668) (layer "F.SilkS") (width 0.381) (tstamp e9504a34-7c05-4817-bcdb-3490f46e9a0d))
    (fp_line (start 3.429 -8.001) (end -3.429 -8.001) (layer "F.SilkS") (width 0.381) (tstamp fb5aca67-0b31-4916-864f-f3205c92f453))
    (pad "" np_thru_hole circle locked (at 0 -6.985) (size 3.048 3.048) (drill 3.048) (layers *.Cu *.Mask) (tstamp 70e0a615-845d-4708-ba61-54dc0daf8796))
    (pad "" np_thru_hole circle locked (at 0 8.255) (size 3.9802 3.9802) (drill 3.9802) (layers *.Cu *.Mask) (tstamp f5ed59bf-267c-40a8-bc11-344e100f66d4))
  )
"""

mounthole2d5mm_tmpl = """
  (footprint "Mounting_Holes:MountingHole_2.5mm" (layer "F.Cu")
    (tedit 5CB1B15C) (tstamp 00000000-0000-0000-0000-00005cbb643c)
    (at %s)
    (descr "Mounting Hole 2.5mm, no annular")
    (tags "mounting hole 2.5mm no annular")
    (attr through_hole)
    (fp_text reference "" (at 0 -3.5) (layer "F.SilkS") hide
      (effects (font (size 1 1) (thickness 0.15)))
      (tstamp 272c2a78-b5f5-4b61-aed3-ec69e0e92729)
    )
    (fp_text value "MountingHole_2.5mm" (at 0 3.5) (layer "F.Fab") hide
      (effects (font (size 1 1) (thickness 0.15)))
      (tstamp a3fab380-991d-404b-95d5-1c209b047b6e)
    )
    (fp_circle (center 0 0) (end 2.5 0) (layer "Cmts.User") (width 0.15) (fill none) (tstamp 7273dd21-e834-41d3-b279-d7de727709ca))
    (fp_circle (center 0 0) (end 2.75 0) (layer "F.CrtYd") (width 0.05) (fill none) (tstamp 62f15a9a-9893-486e-9ad0-ea43f88fc9e7))
    (pad "" thru_hole circle locked (at 0 0) (size 2.5 2.5) (drill 2.5) (layers *.Cu *.Mask) (tstamp b2b363dd-8e47-4a76-a142-e00e28334875))
  )
"""

mounthole2d5mmpadded_tmpl = """
  (footprint "Mounting_Holes:MountingHole_2.5mm" (layer "F.Cu")
    (tedit 5D2E15E2) (tstamp 11a6935f-c932-4d1f-916e-b410aebf1144)
    (at %s)
    (descr "Mounting Hole 2.5mm, no annular")
    (tags "mounting hole 2.5mm no annular")
    (attr through_hole)
    (fp_text reference "REF**" (at 0 -3.5) (layer "F.SilkS") hide
      (effects (font (size 1 1) (thickness 0.15)))
      (tstamp d8db916f-c8d2-493c-ba90-b70a418ab48c)
    )
    (fp_text value "MountingHole_padded_2.5mm" (at 0 3.5) (layer "F.Fab")
      (effects (font (size 1 1) (thickness 0.15)))
      (tstamp c4f68296-3c17-4b99-803f-43207612cf46)
    )
    (fp_circle (center 0 0) (end 2.5 0) (layer "Cmts.User") (width 0.15) (fill none) (tstamp 584f7ee5-300f-4226-9927-614933edbbe0))
    (fp_circle (center 0 0) (end 2.75 0) (layer "F.CrtYd") (width 0.05) (fill none) (tstamp 380592bc-77c3-4e7d-88ed-2125a285233b))
    (pad "" thru_hole circle locked (at 0 0) (size 3.25 3.25) (drill 2.5) (layers *.Cu *.Mask) (tstamp 8fe0cd38-cdd9-4b1c-8fdb-dd68eb399f6f))
  )
"""

edgecut = """
  (gr_arc (start 345.29 64.82) (mid 346.562792 65.347208) (end 347.09 66.62) (layer "Edge.Cuts") (width 0.0991) (tstamp 245afab8-87c2-4797-af78-aa00d5229c94))
  (gr_arc (start 347.09 157.22) (mid 346.562792 158.492792) (end 345.29 159.02) (layer "Edge.Cuts") (width 0.0991) (tstamp 435960f9-5f02-4a62-b70b-90c1310d341d))
  (gr_arc (start 62.49 66.62) (mid 63.017208 65.347208) (end 64.29 64.82) (layer "Edge.Cuts") (width 0.0991) (tstamp 53450cca-0496-4005-a7ef-5b1ae88fa402))
  (gr_line (start 347.09 66.62) (end 347.09 157.22) (layer "Edge.Cuts") (width 0.0991) (tstamp 5ee97714-8ad8-47a4-bd70-3ebc8406c7b5))
  (gr_arc (start 64.29 159.02) (mid 63.017208 158.492792) (end 62.49 157.22) (layer "Edge.Cuts") (width 0.0991) (tstamp c41835e2-2b20-4f99-a85d-b1859480e6e6))
  (gr_line (start 64.29 159.02) (end 345.28 159.02) (layer "Edge.Cuts") (width 0.0991) (tstamp e997c615-0a9d-46fc-872f-6b2d14f01b36))
  (gr_line (start 62.49 157.22) (end 62.49 66.62) (layer "Edge.Cuts") (width 0.0991) (tstamp ee19a334-b72e-4d54-9a8e-a742ee56e7f1))
  (gr_line (start 64.29 64.82) (end 345.29 64.82) (layer "Edge.Cuts") (width 0.0991) (tstamp f5156e03-6da9-4205-8d49-0997e01031c7))
  (gr_text "GH60 PCB design by komar007 & jdcarpe | split60(v0.3) PCB designed by ngzh" (at 345.2 157.6) (layer "B.SilkS") (tstamp 7075a498-5749-4f19-ba7d-9b8161486d1a)
    (effects (font (size 1.524 1.524) (thickness 0.3048)) (justify left mirror))
  )
"""

padded_holes = """
  (footprint "hole:PKRHC" (layer "F.Cu")
    (tedit 5CBDEAC4) (tstamp 00000000-0000-0000-0000-00005041fbb5)
    (at 322.3399 92.5208)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "HOLE" (at 0.1753 5.7861) (layer "F.SilkS") hide
      (effects (font (size 1.524 1.524) (thickness 0.3048)))
      (tstamp 2afbd14f-e6ea-4bea-882b-7e9761a0434e)
    )
    (fp_text value "VAL**" (at 0.17526 -4.9022) (layer "F.SilkS") hide
      (effects (font (size 1.524 1.524) (thickness 0.3048)))
      (tstamp 790aac60-8af7-4c8a-86b0-99f3fe64112a)
    )
    (pad "" np_thru_hole circle locked (at 0 0) (size 7.00024 7.00024) (drill oval 5.00126 2.49936) (layers *.Cu *.Mask) (tstamp 5a9c0dbe-9c68-4f1b-bb8c-18e35b87c9b2))
  )

  (footprint "hole:PKRHSL" (layer "F.Cu")
    (tedit 5C6978B5) (tstamp 00000000-0000-0000-0000-00005075a72a)
    (at 345.8312 121.1212)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "HOLE" (at 0 4.675) (layer "F.SilkS") hide
      (effects (font (size 1.524 1.524) (thickness 0.3048)))
      (tstamp 78a4062b-d2b4-4346-a029-0257bf4c7e99)
    )
    (fp_text value "VAL**" (at 0.508 -4.826) (layer "F.SilkS") hide
      (effects (font (size 1.524 1.524) (thickness 0.3048)))
      (tstamp 0b264411-5df7-4227-b41c-4ba7687d2096)
    )
    (pad "" np_thru_hole oval locked (at 0 0) (size 9.99998 5.00126) (drill oval 7.00024 2.49936) (layers *.Cu *.Mask) (tstamp d67f893e-d62b-44c0-a1ed-06c27930b246))
  )

  (footprint "hole:PKRHC" (layer "F.Cu")
    (tedit 5D59F7D3) (tstamp 00000000-0000-0000-0000-000051796fd9)
    (at 87.4893 92.5208)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "HOLE" (at 0 5.08) (layer "F.SilkS") hide
      (effects (font (size 1.524 1.524) (thickness 0.3048)))
      (tstamp f6c6b658-1bf6-4c26-b6a1-d4c107527951)
    )
    (fp_text value "VAL**" (at 0.508 -4.826) (layer "F.SilkS") hide
      (effects (font (size 1.524 1.524) (thickness 0.3048)))
      (tstamp 16ea365c-d7f5-4c44-b4c6-7d8ef461a0ca)
    )
    (pad "" np_thru_hole circle locked (at 0 0) (size 7 7) (drill oval 5.00126 2.4994) (layers F&B.Cu *.Mask) (tstamp 753c83e3-0e5d-49a7-99fa-14d791ee9328))
  )

  (footprint "hole:PKRHSL" (layer "F.Cu")
    (tedit 5C69786B) (tstamp 00000000-0000-0000-0000-00005c78d4a2)
    (at 63.7489 121.1212)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "HOLE" (at 0 4.675) (layer "F.SilkS") hide
      (effects (font (size 1.524 1.524) (thickness 0.3048)))
      (tstamp 3249bd81-9fd4-4194-9b4f-2e333b2195b8)
    )
    (fp_text value "VAL**" (at 0.508 -4.826) (layer "F.SilkS") hide
      (effects (font (size 1.524 1.524) (thickness 0.3048)))
      (tstamp 718e5c6d-0e4c-46d8-a149-2f2bfc54c7f1)
    )
    (pad "" np_thru_hole oval locked (at 0 0) (size 9.99998 5.00126) (drill oval 7.00024 2.49936) (layers *.Cu *.Mask) (tstamp 9e0e6fc0-a269-4822-b93d-4c5e6689ff11))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBDEAB1) (tstamp 00000000-0000-0000-0000-00005c600abe)
    (at 190.5 111.76)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "HOLE" (at 0.1753 5.7861) (layer "F.SilkS") hide
      (effects (font (size 1.524 1.524) (thickness 0.3048)))
      (tstamp 629fdb7a-7978-43d0-987e-b84465775826)
    )
    (fp_text value "VAL**" (at 0.17526 -4.9022) (layer "F.SilkS") hide
      (effects (font (size 1.524 1.524) (thickness 0.3048)))
      (tstamp df9a1242-2d73-4343-b170-237bc9a8080f)
    )
    (pad "" np_thru_hole oval locked (at 0 0) (size 7.00024 4) (drill oval 5.00126 2.49936) (layers *.Cu *.Mask) (tstamp 2d0d333a-99a0-4575-9433-710c8cc7ac0b))
    (model "cherry_mx1.wrl"
      (offset (xyz 0 0 0))
      (scale (xyz 1 1 1))
      (rotate (xyz 0 0 0))
    )
  )

"""


split_hole_normal = """

    (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD556F3) (tstamp 00000000-0000-0000-0000-00005cbca76a)
    (at 190.5 83.34502)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp e30e24b7-089a-4a23-ae9b-280b1c21fa75)
    )
    (fp_text value "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 8d4d8e7f-cc3a-4234-974b-8722042064fe)
    )
    (pad "" np_thru_hole oval locked (at 0 0) (size 14.75 4) (drill oval 14.75 4) (layers F&B.Cu *.Mask) (tstamp 968a6172-7a4e-40ab-a78a-e4d03671e136))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD5575B) (tstamp 00000000-0000-0000-0000-00005cbca912)
    (at 188 102.2)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 22471a88-5f5d-4af8-b741-06c4989b8f93)
    )
    (fp_text value "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp de8f00ba-0262-4c37-93c3-1627767e9ebb)
    )
    (pad "" np_thru_hole oval locked (at 0.11875 0.19502) (size 9.75 4) (drill oval 9.75 4) (layers F&B.Cu *.Mask) (tstamp 1876c30c-72b2-4a8d-9f32-bf8b213530b4))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD5579D) (tstamp 00000000-0000-0000-0000-00005cbcaa3e)
    (at 193.68125 121.20498)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 92d72e76-247a-447e-8ccc-48e25e6c2cb8)
    )
    (fp_text value "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 519ef6c8-1354-4112-888b-bd7511e3396c)
    )
    (pad "" np_thru_hole oval locked (at 1.58125 0.24004) (size 13.75 4) (drill oval 13.75 4) (layers F&B.Cu *.Mask) (tstamp 54ed3ee1-891b-418e-ab9c-6a18747d7388))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD55788) (tstamp 00000000-0000-0000-0000-00005cbcacc9)
    (at 190.20498 105.31875 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide 
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp bbaae04e-b547-458a-96f1-143a3fdf1b10)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp a31d440e-0d50-48fb-b3f4-f5a3774b9a03)
    )
    (pad "" np_thru_hole oval locked (at 0.11875 0.29502 90) (size 8.8 4) (drill oval 8.8 4) (layers F&B.Cu *.Mask) (tstamp a90361cd-254c-4d27-ae1f-9a6c85bafe28))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD55793) (tstamp 00000000-0000-0000-0000-00005cbcacd2)
    (at 190.40498 118.6 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 997c42c2-8676-4be4-bebe-7bfdef3a600c)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp b49c8bc6-72c9-4619-af09-3d35548d36fe)
    )
    (pad "" np_thru_hole oval locked (at 0.11875 0.09502 90) (size 9 4) (drill oval 9 4) (layers F&B.Cu *.Mask) (tstamp c210293b-1d7a-4e96-92e9-058784106727))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD5574E) (tstamp 00000000-0000-0000-0000-00005cbcacf6)
    (at 185.60498 97 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp a3e7ee29-d51c-459e-9b60-3d125408f42d)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 6d3e48d1-52d6-4c8b-8d08-162e4468bff5)
    )
    (pad "" np_thru_hole oval (at 0.51875 0.13252 90) (size 15 4) (drill oval 15 4) (layers F&B.Cu *.Mask) (tstamp 4641c87c-bffa-41fe-ae77-be3a97a6f797))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD556FE) (tstamp 00000000-0000-0000-0000-00005cbcad3f)
    (at 185.60498 84.61875 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp ef300cdb-771a-4639-b067-9cd94fab88bf)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 8837d285-ed0e-4151-9d2f-ea285196d5e2)
    )
    (pad "" np_thru_hole oval locked (at 0.11875 0.13252 90) (size 5.5 4) (drill oval 5.5 4) (layers F&B.Cu *.Mask) (tstamp 7a74c4b1-6243-4a12-85a2-bc41d346e7aa))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBCB0FF) (tstamp 00000000-0000-0000-0000-00005cbcb091)
    (at 193.6 64.63 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp a9d67b10-08e0-4de1-9429-3aa68addfb62)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 92f38eca-9c9f-4b54-a365-06ef22527867)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 3.2 3.2) (drill oval 3.2) (layers *.Cu *.Mask) (tstamp bb8162f0-99c8-4884-be5b-c0d0c7e81ff6))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBCB0FF) (tstamp 00000000-0000-0000-0000-00005cbcb121)
    (at 196.91 64.63 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 661d70a7-8236-43c4-872b-b171ae32da1c)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 2f70abf6-2c84-464f-8aae-3ea8826b2974)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 3.2 3.2) (drill oval 3.2) (layers *.Cu *.Mask) (tstamp d1c19c11-0a13-4237-b6b4-fb2ef1db7c6d))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C7D0) (tstamp 00000000-0000-0000-0000-00005cbcb135)
    (at 187.6 85.4 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 4e939423-08aa-4f08-981b-5c220c2c677f)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 0569787f-cbf4-45d1-96c5-956c980a6672)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp 7e1217ba-8a3d-4079-8d7b-b45f90cfbf53))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C7B7) (tstamp 00000000-0000-0000-0000-00005cbcb154)
    (at 187.6 100.4 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 28d9075e-0b7c-4b78-b87e-0b0533011d8c)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 07267344-5f30-4c94-b42b-b095fdca3a8a)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp f33ec0db-ef0f-4576-8054-2833161a8f30))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C787) (tstamp 00000000-0000-0000-0000-00005cbcb160)
    (at 188.7 104.4 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 33d2ca1f-ce6d-4895-be45-965df672b4fc)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp c05789e3-5de3-4d27-94cf-aac001645950)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp fd5f7d77-0f73-4021-88a8-0641f0fe8d98))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C76F) (tstamp 00000000-0000-0000-0000-00005cbcb17b)
    (at 192.3 119.4 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp c65adc2f-e297-4330-85f9-b2e7d6f45d1a)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp b049cdd4-6c3d-4f07-82de-137e613be57e)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp e76ec524-408a-4daa-89f6-0edfdbcfb621))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE3ABEA) (tstamp 00000000-0000-0000-0000-00005cbcb553)
    (at 200.025 123.4 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 94c92392-ce9e-49d7-9729-71249edfe100)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 6d62651d-24fb-481b-80e1-70817d757e7e)
    )
    (pad "" np_thru_hole oval locked (at -1.8 -0.025 90) (size 8 4) (drill oval 8 4) (layers F&B.Cu *.Mask) (tstamp a5362821-c161-4c7a-a00c-40e1d7472d56))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C97F) (tstamp 00000000-0000-0000-0000-00005cbcb7ad)
    (at 200 146.8 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 9711e04f-db41-4247-9cf4-e7d6b0d4bab1)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 5e262b0b-a8db-4c47-a1ba-5b96d44ce7e9)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 20 4) (drill oval 20 4) (layers F&B.Cu *.Mask) (tstamp ab8b0540-9c9f-4195-88f5-7bed0b0a8ed6))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBCB0FF) (tstamp 00000000-0000-0000-0000-00005cbcb921)
    (at 198.3 159.2 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 630cd62a-ee74-4f54-80e1-8175ce7efb15)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 47f1e435-ef92-4a67-b379-7c7c2721c3bd)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 3.2 3.2) (drill oval 3.2) (layers *.Cu *.Mask) (tstamp ca5b6af8-ca05-4338-b852-b51f2b49b1db))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBCB0FF) (tstamp 00000000-0000-0000-0000-00005cbcb92a)
    (at 201.7 159.2 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 0547add5-5039-40c6-928a-85855f7e8b3c)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp deb435d9-8745-49e7-8ae5-d24115cd0665)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 3.2 3.2) (drill oval 3.2) (layers *.Cu *.Mask) (tstamp 4344bc11-e822-474b-8d61-d12211e719b1))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5D1460DA) (tstamp 00000000-0000-0000-0000-00005cbdebbe)
    (at 195 80.3 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 04224d16-c919-428b-8e21-ef8fcbce96ee)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 69ee6172-0a51-453f-9e3e-62845da16afd)
    )
    (pad "" np_thru_hole oval locked (at -0.38125 0.25752 90) (size 8 4) (drill oval 8 4) (layers F&B.Cu *.Mask) (tstamp 6cb93665-0bcd-4104-8633-fffd1811eee0))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C818) (tstamp 00000000-0000-0000-0000-00005cbdebe9)
    (at 193.3 81.3 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 77bdc8f1-2725-42c2-980e-7cc64075e57c)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp db521a61-800d-4ff4-b860-0cf9230f9a01)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp 3e57b728-64e6-4470-8f27-a43c0dd85050))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBDEF01) (tstamp 00000000-0000-0000-0000-00005cbdeeb4)
    (at 196.67 84.02 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 6f474a47-19d5-4ed9-9722-519b08b86296)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 32dad4d9-873f-43ed-8dfc-2cce395619ed)
    )
    (pad "" np_thru_hole oval locked (at -0.23 0 90) (size 2.5 2.5) (drill oval 2.5) (layers F&B.Cu *.Mask) (tstamp 1cb22080-0f59-4c18-a6e6-8685ef44ec53))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBDEF01) (tstamp 00000000-0000-0000-0000-00005cbdef24)
    (at 184.3 103 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 3740062b-823b-433b-8d82-4ddb4c900590)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 3ce77a49-648b-481e-b7e2-673b9ee21f54)
    )
    (pad "" np_thru_hole oval (at -0.25 0 90) (size 2.5 2.5) (drill oval 2.5) (layers F&B.Cu *.Mask) (tstamp 14094ad2-b562-4efa-8c6f-51d7a3134345))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBDEF01) (tstamp 00000000-0000-0000-0000-00005cbdef31)
    (at 191.6 101.1 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 6b335b0e-d833-4fdf-9c0f-b7c674daa990)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 88c306cd-44d2-41bb-8063-355c1b0102aa)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp d0cd3439-276c-41ba-b38d-f84f6da38415))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBDEF01) (tstamp 00000000-0000-0000-0000-00005cbdef38)
    (at 189.3 122.6 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 761d7ed5-536b-470e-bdd5-9a6a54b759ac)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp f7d1c348-2680-4c39-8b35-bcecab85ba34)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp eac8d865-0226-4958-b547-6b5592f39713))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBDEF01) (tstamp 00000000-0000-0000-0000-00005cbdef42)
    (at 201.24 119.645 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 35be53d2-104e-45fb-884e-4891b7f7da3d)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp e7b9dddb-c718-4c18-9804-9bef2fc6cd51)
    )
    (pad "" np_thru_hole oval locked (at -0.725 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp f4a8afbe-ed68-4253-959f-6be4d2cbf8c5))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5D1460A1) (tstamp 00000000-0000-0000-0000-00005cdc4f50)
    (at 175.94248 67.30875 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 5e7966f8-86ae-4322-a362-bbcd488e36ea)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 187292ec-ba13-40f6-9f7c-f41c4a92267b)
    )
    (pad "" np_thru_hole oval locked (at 1.10875 0.27002 90) (size 8 4) (drill oval 8 4) (layers F&B.Cu *.Mask) (tstamp 7ce7415d-7c22-49f6-8215-488853ccc8c6))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5D1460CC) (tstamp 00000000-0000-0000-0000-00005cdc4f67)
    (at 175.95 80.29875 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 6e5e938e-ef71-49bf-a43e-8edb5cd07e54)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp abfffc34-5622-41e6-9606-94dbb039766c)
    )
    (pad "" np_thru_hole oval locked (at -0.3825 0.2625 90) (size 8 4) (drill oval 8 4) (layers F&B.Cu *.Mask) (tstamp 2b5a9ad3-7ec4-447d-916c-47adf5f9674f))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBCB0FF) (tstamp 00000000-0000-0000-0000-00005cdc4f9a)
    (at 177.87 64.63 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp face10f6-3c34-451e-b9cc-f679659098ee)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp c1726489-131a-487f-ba46-e3f3077d1c37)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 3.2 3.2) (drill oval 3.2) (layers *.Cu *.Mask) (tstamp f357ddb5-3f44-43b0-b00d-d64f5c62ba4a))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBCB0FF) (tstamp 00000000-0000-0000-0000-00005cdc4fa8)
    (at 174.55 64.62 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 736cc6c3-8ce6-476d-b203-e47d7a361718)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 45dbc8cb-a7b2-43fd-8991-02cda3273690)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 3.2 3.2) (drill oval 3.2) (layers *.Cu *.Mask) (tstamp 8b290a17-6328-4178-9131-29524d345539))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CDC50C0) (tstamp 00000000-0000-0000-0000-00005cdc4fca)
    (at 189.72 82.2)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp affe6e42-6aab-4fa5-b9e8-edd3bfc25300)
    )
    (fp_text value "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 48057626-ff9a-48a6-bd6f-6ab85c8e98ff)
    )
    (pad "" np_thru_hole oval locked (at -8.745 1.14502) (size 14.75 4) (drill oval 14.75 4) (layers F&B.Cu *.Mask) (tstamp 44646447-0a8e-4aec-a74e-22bf765d0f33))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C7E0) (tstamp 00000000-0000-0000-0000-00005cdc50f8)
    (at 183.9 86.2 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp f4e26d79-c05a-425b-9e6e-4a56cdbf843a)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 4f98591e-8d51-40bc-8591-1a4201863f40)
    )
    (pad "" np_thru_hole oval locked (at 0.8 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp cebb9021-66d3-4116-98d4-5e6f3c1552be))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C803) (tstamp 00000000-0000-0000-0000-00005ce148c3)
    (at 178.1 81.3 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 345607f4-f4bd-47ba-9e1d-3b48cd251a75)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 0f3d8509-1c2a-4b9e-ae11-5819c7d5024c)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp 2db910a0-b943-40b4-b81f-068ba5265f56))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBDEF01) (tstamp 00000000-0000-0000-0000-00005ce2c74d)
    (at 198.05 123.525 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp cbb0914d-ebe6-4800-b906-be043d191e36)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp c9a2f1b7-cb21-4f97-953e-f8047e1e0574)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp 9186dae5-6dc3-4744-9f90-e697559c6ac8))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBDEF01) (tstamp 00000000-0000-0000-0000-00005ce2fef5)
    (at 174.81 84.09 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 5b23db90-cf83-4b3f-9e55-1b6b9416d18e)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 4d711090-4bb9-4e55-9620-f0dd09fa5695)
    )
    (pad "" np_thru_hole oval locked (at -0.16 0 90) (size 2.5 2.5) (drill oval 2.5) (layers F&B.Cu *.Mask) (tstamp d88958ac-68cd-4955-a63f-0eaa329dec86))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE3AB13) (tstamp 00000000-0000-0000-0000-00005ce3ab96)
    (at 199.99 138.29 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 9cd4380a-dbc9-47a6-9a85-e4ea071772e7)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 89aa8239-bc61-40c7-a96b-a9dcdc8af99a)
    )
    (pad "" np_thru_hole oval locked (at 2 0 90) (size 8 4) (drill oval 8 4) (layers F&B.Cu *.Mask) (tstamp fbe8ebfc-2a8e-4eb8-85c5-38ddeaa5dd00))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD557D8) (tstamp 00000000-0000-0000-0000-00005ce3abb0)
    (at 200.01 155.16 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 5e321b24-ed5e-487b-a4ea-174aa20fc71a)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 719d08c3-2b09-40a9-b583-b2704b8b686f)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 10 4) (drill oval 10 4) (layers F&B.Cu *.Mask) (tstamp 6e435cd4-da2b-4602-a0aa-5dd988834dff))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 0) (tstamp 0cdab6ef-6f41-4374-aca0-38c32f37bec9)
    (at 195.375 66.175)
    (fp_text reference "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 1a4af7f3-e81d-47b8-973b-13d2361d9f54)
    )
    (fp_text value "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp ca92e070-77b7-46d9-86ef-02405dd98774)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 8 4) (drill oval 8 4) (layers F&B.Cu *.Mask) (tstamp 7ce7415d-7c22-49f6-8215-488853ccc8c6))
  )
"""

split_hole_lshift = """
  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD556F3) (tstamp 00000000-0000-0000-0000-00005cbca76a)
    (at 190.5 83.34502)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp e30e24b7-089a-4a23-ae9b-280b1c21fa75)
    )
    (fp_text value "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 8d4d8e7f-cc3a-4234-974b-8722042064fe)
    )
    (pad "" np_thru_hole oval locked (at 0 0) (size 14.75 4) (drill oval 14.75 4) (layers F&B.Cu *.Mask) (tstamp 968a6172-7a4e-40ab-a78a-e4d03671e136))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD5575B) (tstamp 00000000-0000-0000-0000-00005cbca912)
    (at 188 102.2)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 22471a88-5f5d-4af8-b741-06c4989b8f93)
    )
    (fp_text value "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp de8f00ba-0262-4c37-93c3-1627767e9ebb)
    )
    (pad "" np_thru_hole oval locked (at 0.11875 0.19502) (size 9.75 4) (drill oval 9.75 4) (layers F&B.Cu *.Mask) (tstamp 1876c30c-72b2-4a8d-9f32-bf8b213530b4))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD5579D) (tstamp 00000000-0000-0000-0000-00005cbcaa3e)
    (at 193.68125 121.20498)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 92d72e76-247a-447e-8ccc-48e25e6c2cb8)
    )
    (fp_text value "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 519ef6c8-1354-4112-888b-bd7511e3396c)
    )
    (pad "" np_thru_hole oval (at -0.68125 0.24004) (size 9 4) (drill oval 9 4) (layers F&B.Cu *.Mask) (tstamp 54ed3ee1-891b-418e-ab9c-6a18747d7388))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD55788) (tstamp 00000000-0000-0000-0000-00005cbcacc9)
    (at 190.20498 105.31875 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp bbaae04e-b547-458a-96f1-143a3fdf1b10)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp a31d440e-0d50-48fb-b3f4-f5a3774b9a03)
    )
    (pad "" np_thru_hole oval locked (at 0.11875 0.29502 90) (size 8.8 4) (drill oval 8.8 4) (layers F&B.Cu *.Mask) (tstamp a90361cd-254c-4d27-ae1f-9a6c85bafe28))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD55793) (tstamp 00000000-0000-0000-0000-00005cbcacd2)
    (at 190.40498 118.6 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 997c42c2-8676-4be4-bebe-7bfdef3a600c)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp b49c8bc6-72c9-4619-af09-3d35548d36fe)
    )
    (pad "" np_thru_hole oval locked (at 0.11875 0.09502 90) (size 9 4) (drill oval 9 4) (layers F&B.Cu *.Mask) (tstamp c210293b-1d7a-4e96-92e9-058784106727))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD5574E) (tstamp 00000000-0000-0000-0000-00005cbcacf6)
    (at 185.60498 97 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp a3e7ee29-d51c-459e-9b60-3d125408f42d)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 6d3e48d1-52d6-4c8b-8d08-162e4468bff5)
    )
    (pad "" np_thru_hole oval (at 0.51875 0.13252 90) (size 15 4) (drill oval 15 4) (layers F&B.Cu *.Mask) (tstamp 4641c87c-bffa-41fe-ae77-be3a97a6f797))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD556FE) (tstamp 00000000-0000-0000-0000-00005cbcad3f)
    (at 185.60498 84.61875 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp ef300cdb-771a-4639-b067-9cd94fab88bf)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 8837d285-ed0e-4151-9d2f-ea285196d5e2)
    )
    (pad "" np_thru_hole oval locked (at 0.11875 0.13252 90) (size 5.5 4) (drill oval 5.5 4) (layers F&B.Cu *.Mask) (tstamp 7a74c4b1-6243-4a12-85a2-bc41d346e7aa))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBCB0FF) (tstamp 00000000-0000-0000-0000-00005cbcb091)
    (at 193.6 64.63 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp a9d67b10-08e0-4de1-9429-3aa68addfb62)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 92f38eca-9c9f-4b54-a365-06ef22527867)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 3.2 3.2) (drill oval 3.2) (layers *.Cu *.Mask) (tstamp bb8162f0-99c8-4884-be5b-c0d0c7e81ff6))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBCB0FF) (tstamp 00000000-0000-0000-0000-00005cbcb121)
    (at 196.91 64.63 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 661d70a7-8236-43c4-872b-b171ae32da1c)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 2f70abf6-2c84-464f-8aae-3ea8826b2974)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 3.2 3.2) (drill oval 3.2) (layers *.Cu *.Mask) (tstamp d1c19c11-0a13-4237-b6b4-fb2ef1db7c6d))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C7D0) (tstamp 00000000-0000-0000-0000-00005cbcb135)
    (at 187.6 85.4 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 4e939423-08aa-4f08-981b-5c220c2c677f)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 0569787f-cbf4-45d1-96c5-956c980a6672)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp 7e1217ba-8a3d-4079-8d7b-b45f90cfbf53))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C7B7) (tstamp 00000000-0000-0000-0000-00005cbcb154)
    (at 187.6 100.4 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 28d9075e-0b7c-4b78-b87e-0b0533011d8c)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 07267344-5f30-4c94-b42b-b095fdca3a8a)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp f33ec0db-ef0f-4576-8054-2833161a8f30))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C787) (tstamp 00000000-0000-0000-0000-00005cbcb160)
    (at 188.7 104.4 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 33d2ca1f-ce6d-4895-be45-965df672b4fc)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp c05789e3-5de3-4d27-94cf-aac001645950)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp fd5f7d77-0f73-4021-88a8-0641f0fe8d98))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C76F) (tstamp 00000000-0000-0000-0000-00005cbcb17b)
    (at 192.3 119.4 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp c65adc2f-e297-4330-85f9-b2e7d6f45d1a)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp b049cdd4-6c3d-4f07-82de-137e613be57e)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp e76ec524-408a-4daa-89f6-0edfdbcfb621))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE3ABEA) (tstamp 00000000-0000-0000-0000-00005cbcb553)
    (at 200.025 123.4 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 94c92392-ce9e-49d7-9729-71249edfe100)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 6d62651d-24fb-481b-80e1-70817d757e7e)
    )
    (pad "" np_thru_hole oval locked (at -1.8 -4.7875 90) (size 8 4) (drill oval 8 4) (layers F&B.Cu *.Mask) (tstamp a5362821-c161-4c7a-a00c-40e1d7472d56))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C97F) (tstamp 00000000-0000-0000-0000-00005cbcb7ad)
    (at 200 146.8 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 9711e04f-db41-4247-9cf4-e7d6b0d4bab1)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 5e262b0b-a8db-4c47-a1ba-5b96d44ce7e9)
    )
    (pad "" np_thru_hole oval locked (at 0 -4.7625 90) (size 20 4) (drill oval 20 4) (layers F&B.Cu *.Mask) (tstamp ab8b0540-9c9f-4195-88f5-7bed0b0a8ed6))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBCB0FF) (tstamp 00000000-0000-0000-0000-00005cbcb921)
    (at 198.3 159.2 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 630cd62a-ee74-4f54-80e1-8175ce7efb15)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 47f1e435-ef92-4a67-b379-7c7c2721c3bd)
    )
    (pad "" np_thru_hole oval locked (at 0 -4.7625 90) (size 3.2 3.2) (drill oval 3.2) (layers *.Cu *.Mask) (tstamp ca5b6af8-ca05-4338-b852-b51f2b49b1db))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBCB0FF) (tstamp 00000000-0000-0000-0000-00005cbcb92a)
    (at 201.7 159.2 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 0547add5-5039-40c6-928a-85855f7e8b3c)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp deb435d9-8745-49e7-8ae5-d24115cd0665)
    )
    (pad "" np_thru_hole oval locked (at 0 -4.7625 90) (size 3.2 3.2) (drill oval 3.2) (layers *.Cu *.Mask) (tstamp 4344bc11-e822-474b-8d61-d12211e719b1))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5D1460DA) (tstamp 00000000-0000-0000-0000-00005cbdebbe)
    (at 195 80.3 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 04224d16-c919-428b-8e21-ef8fcbce96ee)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 69ee6172-0a51-453f-9e3e-62845da16afd)
    )
    (pad "" np_thru_hole oval locked (at -0.38125 0.25752 90) (size 8 4) (drill oval 8 4) (layers F&B.Cu *.Mask) (tstamp 6cb93665-0bcd-4104-8633-fffd1811eee0))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C818) (tstamp 00000000-0000-0000-0000-00005cbdebe9)
    (at 193.3 81.3 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 77bdc8f1-2725-42c2-980e-7cc64075e57c)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp db521a61-800d-4ff4-b860-0cf9230f9a01)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp 3e57b728-64e6-4470-8f27-a43c0dd85050))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBDEF01) (tstamp 00000000-0000-0000-0000-00005cbdeeb4)
    (at 196.67 84.02 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 6f474a47-19d5-4ed9-9722-519b08b86296)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 32dad4d9-873f-43ed-8dfc-2cce395619ed)
    )
    (pad "" np_thru_hole oval locked (at -0.23 0 90) (size 2.5 2.5) (drill oval 2.5) (layers F&B.Cu *.Mask) (tstamp 1cb22080-0f59-4c18-a6e6-8685ef44ec53))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBDEF01) (tstamp 00000000-0000-0000-0000-00005cbdef24)
    (at 184.3 103 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 3740062b-823b-433b-8d82-4ddb4c900590)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 3ce77a49-648b-481e-b7e2-673b9ee21f54)
    )
    (pad "" np_thru_hole oval (at -0.25 0 90) (size 2.5 2.5) (drill oval 2.5) (layers F&B.Cu *.Mask) (tstamp 14094ad2-b562-4efa-8c6f-51d7a3134345))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBDEF01) (tstamp 00000000-0000-0000-0000-00005cbdef31)
    (at 191.6 101.1 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 6b335b0e-d833-4fdf-9c0f-b7c674daa990)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 88c306cd-44d2-41bb-8063-355c1b0102aa)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp d0cd3439-276c-41ba-b38d-f84f6da38415))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBDEF01) (tstamp 00000000-0000-0000-0000-00005cbdef38)
    (at 189.3 122.6 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 761d7ed5-536b-470e-bdd5-9a6a54b759ac)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp f7d1c348-2680-4c39-8b35-bcecab85ba34)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp eac8d865-0226-4958-b547-6b5592f39713))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBDEF01) (tstamp 00000000-0000-0000-0000-00005cbdef42)
    (at 201.24 119.645 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 35be53d2-104e-45fb-884e-4891b7f7da3d)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp e7b9dddb-c718-4c18-9804-9bef2fc6cd51)
    )
    (pad "" np_thru_hole oval locked (at -0.725 -4.7625 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp f4a8afbe-ed68-4253-959f-6be4d2cbf8c5))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5D1460A1) (tstamp 00000000-0000-0000-0000-00005cdc4f50)
    (at 175.94248 67.30875 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS")
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 5e7966f8-86ae-4322-a362-bbcd488e36ea)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS")
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 187292ec-ba13-40f6-9f7c-f41c4a92267b)
    )
    (pad "" np_thru_hole oval locked (at 1.10875 0.27002 90) (size 8 4) (drill oval 8 4) (layers F&B.Cu *.Mask) (tstamp 7ce7415d-7c22-49f6-8215-488853ccc8c6))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5D1460CC) (tstamp 00000000-0000-0000-0000-00005cdc4f67)
    (at 175.95 80.29875 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 6e5e938e-ef71-49bf-a43e-8edb5cd07e54)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp abfffc34-5622-41e6-9606-94dbb039766c)
    )
    (pad "" np_thru_hole oval locked (at -0.3825 0.2625 90) (size 8 4) (drill oval 8 4) (layers F&B.Cu *.Mask) (tstamp 2b5a9ad3-7ec4-447d-916c-47adf5f9674f))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBCB0FF) (tstamp 00000000-0000-0000-0000-00005cdc4f9a)
    (at 177.87 64.63 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp face10f6-3c34-451e-b9cc-f679659098ee)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp c1726489-131a-487f-ba46-e3f3077d1c37)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 3.2 3.2) (drill oval 3.2) (layers *.Cu *.Mask) (tstamp f357ddb5-3f44-43b0-b00d-d64f5c62ba4a))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBCB0FF) (tstamp 00000000-0000-0000-0000-00005cdc4fa8)
    (at 174.55 64.62 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 736cc6c3-8ce6-476d-b203-e47d7a361718)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 45dbc8cb-a7b2-43fd-8991-02cda3273690)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 3.2 3.2) (drill oval 3.2) (layers *.Cu *.Mask) (tstamp 8b290a17-6328-4178-9131-29524d345539))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CDC50C0) (tstamp 00000000-0000-0000-0000-00005cdc4fca)
    (at 189.72 82.2)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp affe6e42-6aab-4fa5-b9e8-edd3bfc25300)
    )
    (fp_text value "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 48057626-ff9a-48a6-bd6f-6ab85c8e98ff)
    )
    (pad "" np_thru_hole oval locked (at -8.745 1.14502) (size 14.75 4) (drill oval 14.75 4) (layers F&B.Cu *.Mask) (tstamp 44646447-0a8e-4aec-a74e-22bf765d0f33))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C7E0) (tstamp 00000000-0000-0000-0000-00005cdc50f8)
    (at 183.9 86.2 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp f4e26d79-c05a-425b-9e6e-4a56cdbf843a)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 4f98591e-8d51-40bc-8591-1a4201863f40)
    )
    (pad "" np_thru_hole oval locked (at 0.8 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp cebb9021-66d3-4116-98d4-5e6f3c1552be))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE2C803) (tstamp 00000000-0000-0000-0000-00005ce148c3)
    (at 178.1 81.3 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 345607f4-f4bd-47ba-9e1d-3b48cd251a75)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 0f3d8509-1c2a-4b9e-ae11-5819c7d5024c)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp 2db910a0-b943-40b4-b81f-068ba5265f56))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBDEF01) (tstamp 00000000-0000-0000-0000-00005ce2c74d)
    (at 198.05 123.525 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp cbb0914d-ebe6-4800-b906-be043d191e36)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp c9a2f1b7-cb21-4f97-953e-f8047e1e0574)
    )
    (pad "" np_thru_hole oval locked (at 0 -4.7625 90) (size 2.5 2.5) (drill oval 2.5) (layers *.Cu *.Mask) (tstamp 9186dae5-6dc3-4744-9f90-e697559c6ac8))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CBDEF01) (tstamp 00000000-0000-0000-0000-00005ce2fef5)
    (at 174.81 84.09 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 5b23db90-cf83-4b3f-9e55-1b6b9416d18e)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 4d711090-4bb9-4e55-9620-f0dd09fa5695)
    )
    (pad "" np_thru_hole oval locked (at -0.16 0 90) (size 2.5 2.5) (drill oval 2.5) (layers F&B.Cu *.Mask) (tstamp d88958ac-68cd-4955-a63f-0eaa329dec86))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CE3AB13) (tstamp 00000000-0000-0000-0000-00005ce3ab96)
    (at 199.99 138.29 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 9cd4380a-dbc9-47a6-9a85-e4ea071772e7)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 89aa8239-bc61-40c7-a96b-a9dcdc8af99a)
    )
    (pad "" np_thru_hole oval locked (at 2 -4.7625 90) (size 8 4) (drill oval 8 4) (layers F&B.Cu *.Mask) (tstamp fbe8ebfc-2a8e-4eb8-85c5-38ddeaa5dd00))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 5CD557D8) (tstamp 00000000-0000-0000-0000-00005ce3abb0)
    (at 200.01 155.16 90)
    (attr exclude_from_pos_files exclude_from_bom)
    (fp_text reference "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 5e321b24-ed5e-487b-a4ea-174aa20fc71a)
    )
    (fp_text value "" (at 0 0 90) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 719d08c3-2b09-40a9-b583-b2704b8b686f)
    )
    (pad "" np_thru_hole oval locked (at 0 -4.7625 90) (size 10 4) (drill oval 10 4) (layers F&B.Cu *.Mask) (tstamp 6e435cd4-da2b-4602-a0aa-5dd988834dff))
  )

  (footprint "hole:PKRH" (layer "F.Cu")
    (tedit 0) (tstamp 0cdab6ef-6f41-4374-aca0-38c32f37bec9)
    (at 195.375 66.175)
    (fp_text reference "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp 1a4af7f3-e81d-47b8-973b-13d2361d9f54)
    )
    (fp_text value "" (at 0 0) (layer "F.SilkS") hide
      (effects (font (size 1.27 1.27) (thickness 0.15)))
      (tstamp ca92e070-77b7-46d9-86ef-02405dd98774)
    )
    (pad "" np_thru_hole oval locked (at 0 0 90) (size 8 4) (drill oval 8 4) (layers F&B.Cu *.Mask) (tstamp d98ef862-b56d-4fb0-8d7e-85127647fe8c))
  )
"""
