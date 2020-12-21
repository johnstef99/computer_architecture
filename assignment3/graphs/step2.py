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
            round(values[i])), fontweight='bold', fontsize=18)
    plt.barh(y_pos, values)
    plt.yticks(y_pos, ids, fontsize=18)
    plt.xlabel(xlabel, fontsize=18)
    plt.title(label, fontsize=22)
    plt.tight_layout()
    plt.savefig('./'+BNAME+'_'+filename+'.png', dpi=300)
    plt.close()


if __name__ == "__main__":
    with open('../useful_results/results.json') as f:
        data = json.load(f)

    benchmarks_names = ['specbzip', 'spechmmer',
                        'speclbm', 'specmcf', 'specsjeng']
    for BNAME in benchmarks_names:
        benchmark_id = []
        edp = []
        energys = []
        peaks = []
        print(BNAME)
        for benchmark in data:
            bid: str = benchmark['benchmark']
            if bid.split('_')[1] == '1GHz':
                continue
            if bid[:bid.find('_')] == BNAME:
                benchmark_id.append(bid)
                energy = benchmark['energy']
                runtime = benchmark['runtime']
                area = benchmark['area']
                peak_power = benchmark['peak_power']
                energys.append(energy)
                peaks.append(peak_power)
                edp.append(energy*runtime)

        bar_chart(benchmark_id, edp, BNAME + ' - EDP',
                  'energy * delay', 'edp')
        bar_chart(benchmark_id, energys, BNAME + ' - Energy (mJ)',
                  'energy', 'energy')
        bar_chart(benchmark_id, peaks, BNAME + ' - Peak Power (W)',
                  'peak power', 'peak_power')
