import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import json


def bar_chart(ids, values, label, xlabel, filename):
    """export chart"""
    y_pos = np.arange(len(ids))
    figure(num=None, figsize=(24, 12),
           facecolor='w', edgecolor='k')
    plt.subplots_adjust(left=0.25, right=0.9)
    for i in range(len(values)):
        plt.text(x=values[i], y=y_pos[i], s=str(
            round(values[i]))+' A', fontweight='bold', fontsize=18)
    plt.barh(y_pos, values)
    plt.yticks(y_pos, ids, fontsize=18)
    plt.xlabel(xlabel, fontsize=18)
    plt.title(label, fontsize=22)
    plt.tight_layout()
    plt.savefig('../graphs/step3/'+BNAME+'_'+filename+'.png', dpi=300)
    plt.close()


if __name__ == "__main__":
    with open('./data.json') as f:
        data = json.load(f)

    benchmarks_names = ['specbzip', 'spechmmer',
                        'speclbm', 'specmcf', 'specsjeng']
    for BNAME in benchmarks_names:
        benchmark_id = []
        costs = []
        funcs = []
        print(BNAME)
        for benchmark in data:
            bid: str = benchmark['id']
            if bid.split('_')[1] == '1GHz':
                continue
            if bid[:bid.find('_')] == BNAME:
                benchmark_id.append(bid)
                cpi = benchmark['cpi']
                cache_line_size = benchmark['cache_line_size']
                kb_32 = 32 * 1024
                mb_1 = 1024 * 1024
                l1i = (benchmark['l1_icache'] / kb_32) * \
                    benchmark['l1_icache_assoc']
                l1d = (benchmark['l1_dcache'] / kb_32) * \
                    benchmark['l1_dcache_assoc']
                l2 = (benchmark['l2_cache'] / mb_1) * benchmark['l2_assoc']
                cost = (l1i + 2*l1d + 0.2*l2)*cache_line_size/32
                func = cost * cpi
                costs.append(cost)
                funcs.append(func)

        bar_chart(benchmark_id, funcs, BNAME + ' - Cost * CPI (στρογγυλοποιημένα)',
                  'cost * cpi', 'cost')
