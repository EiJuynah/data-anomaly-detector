import pandas as pd
import numpy as np


def pair_anomaly_detect(df1, df2, comparison_metrics: dict):
    '''
    对两段数据进行对比，如果指标变化超过阈值，则返回False，反之返回False
    :param dataframe: 需要冲突检测的源数据
    :param metrics: a dict:{指标：阈值}
    :return: 如果指标变化超过阈值，则返回False，反之返回False
    '''
    for comp_metric in comparison_metrics.keys():
        threshold_value = comparison_metrics[comp_metric]
        if abs(df1[comp_metric] - df2[comp_metric]) > threshold_value:
            return False

    return True


def anomaly_detector(dataloader, datasaver, comparison_metrics: dict, screening_metrics: list, ):
    df = dataloader.load_data()

    anomaly_df=pd.DataFrame()
    datasaver.save_data(anomaly_df)


def main():
    pair_anomaly_detect()


if __name__ == '__main__':
    main()
