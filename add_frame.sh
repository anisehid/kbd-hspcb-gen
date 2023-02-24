#!/bin/bash
set -e
set -x

file_without_ext=${1%.*}

kikit panelize     \
   --layout 'grid; rows: 1; cols: 1; space: 2mm'     \
   --tabs 'fixed; hwidth: 5mm; vwidth: 320mm'     \
   --cuts vcuts     \
   --framing 'railstb; width: 5mm; space: 3mm; chamfer: 1mm'     \
   --tooling '3hole; hoffset: 2.5mm; voffset: 2.5mm; size: 1.5mm'     \
   --fiducials '3fid; hoffset: 5mm; voffset: 2.5mm; coppersize: 2mm; opening: 1mm;'     \
   --post 'millradius: 1mm'     \
   $1 ${file_without_ext}-frame.kicad_pcb

