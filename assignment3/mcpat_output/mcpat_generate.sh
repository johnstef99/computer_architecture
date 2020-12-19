#!/bin/bash

mcpat_path='../../../my_mcpat/mcpat/mcpat'
xmls='../ProcessorDescriptionFiles/*.xml'

for file in $(ls $xmls)
do
  name=$(echo $file | rev | cut -d'/' -f1 | rev | cut -d'.' -f1)
  echo "Generating for $name"
  $mcpat_path -infile $file -print_level 5 > "$name.txt"
done
