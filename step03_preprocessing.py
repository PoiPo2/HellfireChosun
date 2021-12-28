from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time


""" 시퀀스 데이터의 주기(period)를 정의합니다. 단위는 일(day) 입니다. """
""" period 또한 적절히 분배할 필요가 있습니다. """
PERIOD = 1095
FILENAME = f'training_metadata_{PERIOD}.npy'


def getPeriod():
    return PERIOD


if __name__ == '__main__':
    start_time = time.time()
    """ 전처리하고자 하는 csv 파일을 불러옵니다. """
    data = pd.read_csv('./data/Gyeonggi_2_Suwon_renew_11315.csv', index_col='datetime')
    # print(f'{data}\n{type(data)}')

    """ 모든 데이터 값들을 0과 1사이의 값으로 스케일링(Scaling) 합니다. """
    minmaxscaler = MinMaxScaler()
    scaled_data = minmaxscaler.fit_transform(data)

    """ 시퀀스(Sequence) 데이터를 생성하기 위한 리스트를 정의합니다. """
    sequence_x, sequence_y = [], []
    for idx in range(len(scaled_data) - PERIOD):
        x = scaled_data[idx:idx + PERIOD]
        y = scaled_data[idx + PERIOD]
        sequence_x.append(x)
        sequence_y.append(y)
    # print(sequence_x[:3])
    # print(sequence_y[:3])

    """ 시퀀스 데이터를 np.array 타입으로 변형합니다. (모델 입력을 위한 변형) """
    sequence_x = np.array(sequence_x)
    sequence_y = np.array(sequence_y)
    # print(sequence_x[0], sequence_x.shape)
    # print(sequence_y[0], sequence_y.shape)

    """ 학습 및 테스트에 사용할 데이터셋을 구분 및 생성합니다. """
    x_train, x_test, y_train, y_test = train_test_split(sequence_x, sequence_y, test_size=0.2)
    # print(x_train.shape)
    # print(x_test.shape)
    # print(y_train.shape)
    # print(y_test.shape)
    training_metadata = x_train, x_test, y_train, y_test
    """ 생성한 데이터셋을 .npy 파일로 저장합니다. """
    np.save(f'./{FILENAME}', training_metadata)
    print(f'"{FILENAME}" is saved.')
    print(f'runtime is {round(time.time() - start_time, 3)} seconds.')
