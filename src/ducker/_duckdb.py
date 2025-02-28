__all__ = ['compare_handling_time']

import pandas as pd
import seaborn as sns
import duckdb
import time


def compare_handling_time(dataset_name: str):
    _data = sns.load_dataset(dataset_name)
    _data.to_csv('test_data.csv', index=False)
    _duck = duckdb.read_csv('test_data.csv')

    for _func in [_select_columns, _filter_rows]:
        print(f'\n{_func.__name__}')
        _func(_data, _duck)


def _select_columns(_data, _duck):
    _cols = _data.columns[:3]

    print('pandas')
    _start = time.time()
    _ = _data[_cols]
    print(time.time() - _start)

    print('duck with sql')
    _start = time.time()
    _ = duckdb.sql(f'select {", ".join(_cols)} from _data')
    print(time.time() - _start)

    print('duck with read_csv')
    _start = time.time()
    _ = _duck.project(f'{", ".join(_cols)}')
    print(time.time() - _start)
