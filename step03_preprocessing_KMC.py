from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import numpy as np
import os
import pandas as pd
import pickle
import time
import warnings


""" 넘파이(numpy) 패키지 경고를 출력하지 않도록 변경합니다. """
warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)

""" 시퀀스 데이터의 주기(period)를 정의합니다. 단위는 일(day) 입니다. """
PERIOD = 30                             # 수정 금지

""" (경로 수정 금지) 파일을 불러오거나 저장하는 경로를 설정합니다. """
LOAD_PATH = './data'
SAVE_PATH = './sequence_data'           # 없으면 sequence_data 이름으로 폴더를 만드셔야 합니다.

""" 자동으로 시퀀스데이터와 스케일러 메타데이터를 생성하기 위한 지역명을 입력합니다. """
REGION = 'Gyeonggi'


def getPeriod():
    return PERIOD


if __name__ == '__main__':
    for element in os.listdir(LOAD_PATH):
        if REGION in element:
            start_time = time.time()
            filename = element.split('renew')[0]
            np_filename = ''.join([filename, f'sequence.npy'])

            """ 전처리하고자 하는 csv 파일을 불러옵니다. """
            data = pd.read_csv(f'{LOAD_PATH}/{element}', index_col='datetime')

            """ 모든 데이터 값들을 0과 1사이의 값으로 스케일링(Scaling) 합니다. """
            minmaxscaler = MinMaxScaler()
            scaled_data = minmaxscaler.fit_transform(data)
            filename = element.split('renew')[0]
            pickle_filename = ''.join([filename, f'scaler.pickle'])
            with open(f'{SAVE_PATH}/{pickle_filename}', 'wb') as f:
                pickle.dump(minmaxscaler, f)
                print(f'"{pickle_filename}" is saved.')

            """ 시퀀스(Sequence) 데이터를 생성하기 위한 리스트를 정의합니다. """
            sequence_x, sequence_y = [], []
            for idx in range(len(scaled_data) - PERIOD):
                x = scaled_data[idx:idx + PERIOD]
                y = scaled_data[idx + PERIOD]
                sequence_x.append(x)
                sequence_y.append(y)

            """ 시퀀스 데이터를 np.array 타입으로 변형합니다. (모델 입력을 위한 변형) """
            sequence_x = np.array(sequence_x)
            sequence_y = np.array(sequence_y)

            """ 학습 및 테스트에 사용할 데이터셋을 구분 및 생성합니다. """
            x_train, x_test, y_train, y_test = train_test_split(sequence_x, sequence_y, test_size=0.15)
            training_metadata = x_train, x_test, y_train, y_test

            """ 생성한 데이터셋을 .npy 파일로 저장합니다. """
            np.save(f'{SAVE_PATH}/{np_filename}', training_metadata)
            print(f'"{np_filename}" is saved.')
            print('----------------------------------------------------------------------')
    print(f'runtime is {round(time.time() - start_time, 3)} seconds.')
