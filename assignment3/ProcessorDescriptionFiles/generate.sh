#!/bin/bash

gem5_outputs='../../assignment2/gem5_outputs'
gem5_to_mcpat='../../../my_mcpat/Scripts/GEM5ToMcPAT.py'
inorder='../../../my_mcpat/mcpat/ProcessorDescriptionFiles/inorder_arm.xml'

config=''
stats=''

for file in $(find $gem5_outputs -name stats.txt -or -name config.json | sort -h)
do
  name=$(echo $file | rev | cut -d'/' -f2 | rev)
  if [[ $file == *"config.json" ]]; then
    config=$file
  fi
  if [[ $file == *"stats.txt" ]]; then
    echo $name
    stats=$file
    python2 $gem5_to_mcpat $stats $config $inorder -o "$name.xml"
  fi
done
