import time

import click
from codecarbon import track_emissions

from sorters import (
    bubble_sort,
    qsort_3_colors,
)


DEFAULT_ALGO = 'pythonStd'
SORTING_ALGOS = {
    'bubble': bubble_sort,
    'qsort3': qsort_3_colors,
    DEFAULT_ALGO: sorted,
}


def time_measurer(algo):
    def algo_caller(*args, **kwargs):
        start_time = time.time()
        res = algo(*args, **kwargs)
        end_time = time.time()
        print(f'Execution took {end_time - start_time} seconds.')
        return res
    return algo_caller


@click.command()
@click.option('--algo', prompt='Sorting algorithm')
@track_emissions()
def run_algo(algo):
    with open('input.txt', 'r', encoding='utf-8') as fp:
        array = list(
            map(int, fp.read().split(' '))
        )

    if algo not in SORTING_ALGOS:
        algo = DEFAULT_ALGO

    alg = time_measurer(SORTING_ALGOS[algo])
    print(f'{algo}:')
    alg(array)


if __name__ == '__main__':
    run_algo()
