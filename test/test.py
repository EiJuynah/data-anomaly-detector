import numpy as np
import pandas as pd
from core.detector import *


def create_random_test_df():
    # 创建随机id列表
    id_list = ['id' + str(i) for i in range(1, 11)]

    # 创建数据帧
    df = pd.DataFrame()

    for id in id_list:
        # 创建确定的a和随机b列表
        a_list = np.random.uniform(low=1.0, high=100.0, size=2)
        b_list = pd.date_range(start='2023-04-29', end='2023-04-30').date

        # 创建数据帧子集
        df_subset = pd.DataFrame({'id': [id] * 2, 'a': a_list, 'b': b_list})

        # 将子集添加到主数据帧
        df = pd.concat([df, df_subset], axis=0)

    return df


def create_test_df():
    id_list = ['id' + str(i) for i in range(1, 11)]

    # 创建数据帧
    df = pd.DataFrame()

    for id in id_list:
        # 创建a和b列表
        a_list = [23.5, 44.2, 17.8, 63.9, 85.1, 92.3, 72.6, 39.7, 56.4, 28.9,
                  10.5, 76.4, 94.8, 51.2, 31.7, 67.8, 49.1, 88.2, 12.3, 97.6]
        b_list = pd.date_range(start='2023-04-29', end='2023-04-30').date.tolist() * 10

        # 创建数据帧子集
        df_subset = pd.DataFrame({'id': [id] * 2, 'a': a_list, 'b': b_list})

        # 将子集添加到主数据帧
        df = pd.concat([df, df_subset], axis=0)

    return df


test_data = {
    'id': ['id1', 'id1', 'id2', 'id2', 'id3', 'id3', 'id4', 'id4', 'id5', 'id5',
           'id6', 'id6', 'id7', 'id7', 'id8', 'id8', 'id9', 'id9', 'id10', 'id10'],
    'a': [70.223783, 74.374187, 10.420534, 39.501072, 78.401490, 42.174456,
          98.661419, 73.611150, 78.205616, 21.816066, 53.726689, 39.053090,
          77.524560, 76.179863, 84.702250, 69.727168, 64.557689, 50.091032,
          76.163552, 85.768586],
    'c': [44.98, 43.58, 89.18, 45.79, 28.08, 34.89, 14.17, 4.73, 36.61, 73.31,
          22.29, 84.26, 22.6, 91.91, 29.26, 16.15,
          62.25, 46.57, 5.5, 93.85],
    'd': [62.38, 63.05, 68.15, 9.81, 90.72, 80.64, 61.01, 29.2, 57.95, 45.49,
          44.75, 81.02, 60.16, 41.86, 91.79, 9.61, 29.77, 63.11, 2.85, 61.38],

    'b': ['2023-04-29', '2023-04-30', '2023-04-29', '2023-04-30', '2023-04-29',
          '2023-04-30', '2023-04-29', '2023-04-30', '2023-04-29', '2023-04-30',
          '2023-04-29', '2023-04-30', '2023-04-29', '2023-04-30', '2023-04-29',
          '2023-04-30', '2023-04-29', '2023-04-30', '2023-04-29', '2023-04-30']
}
test_data_df = pd.DataFrame(test_data)

if __name__ == '__main__':
    test_data_df = test_data_df[test_data_df.id == 'id1']
    cm = {'a': 10,'c':5,'d':0.5}
    p = pair_anomaly_detect(test_data_df.loc[0], test_data_df.loc[1], comparison_metrics=cm)
    print(p)
