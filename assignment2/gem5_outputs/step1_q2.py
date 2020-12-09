import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import json


def bar_chart(ids, values, label, xlabel, filename):
    """export chart"""
    y_pos = np.arange(len(ids))
    figure(num=None, figsize=(2*len(ids), len(ids)),
           facecolor='w', edgecolor='k')
    plt.subplots_adjust(left=0.25, right=0.9)
    plt.barh(y_pos, values)
    plt.yticks(y_pos, ids)
    plt.xlabel(xlabel)
    plt.title(label)
    plt.tight_layout()
    plt.savefig('../graphs/'+filename+'.png', dpi=300)
    plt.close()


if __name__ == "__main__":
    with open('./data.json') as f:
        data = json.load(f)

    benchmark_id = []
    sim_sec = []
    cpi = []
    l1_icache_miss_rate = []
    l1_dcache_miss_rate = []
    l2_cache_miss_rate = []
    ARGS = '2GHz_64_32kB_2_64kB_2_2MB_8'
    for benchmark in data:
        bid: str = benchmark['id']
        if bid[bid.find('_')+1:] == ARGS:
            benchmark_id.append(bid)
            sim_sec.append(benchmark['sim_seconds'])
            cpi.append(benchmark['cpi'])
            l1_icache_miss_rate.append(benchmark['icache_miss_rate'])
            l1_dcache_miss_rate.append(benchmark['dcache_miss_rate'])
            l2_cache_miss_rate.append(benchmark['l2_miss_rate'])

    bar_chart(benchmark_id, sim_sec, 'Simulation seconds',
              'sim_sec', 'sim_sec_'+ARGS)
    bar_chart(benchmark_id, cpi, 'CPI', 'cpi', 'cpi_'+ARGS)
    bar_chart(benchmark_id, l1_icache_miss_rate,
              'L1 instractions cache miss rate', 'miss_rate', 'icache_miss_rate_'+ARGS)
    bar_chart(benchmark_id, l1_dcache_miss_rate,
              'L1 data cache miss rate', 'miss_rate', 'dcache_miss_rate_'+ARGS)
    bar_chart(benchmark_id, l2_cache_miss_rate, 'L2 cache miss rate',
              'miss_rate', 'l2_cache_miss_rate_'+ARGS)
