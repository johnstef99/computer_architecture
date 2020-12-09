#!/bin/bash

print_file () {
    echo "========================================"
    echo $1 | cut -d'/' -f2
    echo "========================================"
}

#get_stats STRING_TO_GET FILE_TO_GET_FROM
get_stats () {
  echo "$(grep $1 $2 | tr -s ' ' ' ' | cut -d' ' -f2)"
}

#get_stats LINE_TO_GET FILE_TO_GET_FROM
get_config () {
  sed -n -e $1p $file | cut -d'=' -f2
}

for file in $(find -name stats.txt -or -name config.ini | sort -h)
do
  if [[ $file == *"config.ini" ]]; then
    print_file $file
    printf 'cache_line_size: '; get_config 15 $file
    printf 'l1_dcache_assoc: '; get_config 152 $file
    printf 'l1_dcache: '; get_config 169 $file
    printf 'l1_icache_assoc: '; get_config 816 $file
    printf 'l1_icache: '; get_config 833 $file
    printf 'l2_assoc: '; get_config 1061 $file
    printf 'l2_cache: '; get_config 1078 $file
  fi
  if [[ $file == *"stats.txt" ]]; then
    printf 'sim_seconds: '; get_stats sim_seconds $file
    printf 'cpi: '; get_stats cpi $file
    printf 'host_cpu_clock: '; get_stats system.clk_domain.clock $file
    printf 'sim_cpu_clock: '; get_stats system.cpu_clk_domain.clock $file
    printf 'icache_miss_rate: '; get_stats icache.overall_miss_rate::total $file
    printf 'dcache_miss_rate: '; get_stats dcache.overall_miss_rate::total $file
    printf 'l2_miss_rate: '; get_stats l2.overall_miss_rate::total $file
    echo -e "\n"
  fi
done
