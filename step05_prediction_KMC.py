# Version 1.2
# - 기존 예측 함수(predict)는 다른 이름으로 변경 (predict -> single_predict)
# + 애플리케이션 전용 예측 함수(predict) 추가

from datetime import datetime
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pickle
from step03_preprocessing_KMC import getPeriod


""" (경로 수정 금지) 파일을 불러오거나 저장하는 경로를 설정합니다. """
LOAD_PATH = './models'
SAVE_PATH = './models'              # 없으면 models 이름으로 폴더를 만드셔야 합니다.


def single_predict(province, **kwargs):
    scaler = None
    period = getPeriod()
    """ 지역명에 맞는 전처리된 파일(.csv)을 불러옵니다. """
    for element in os.listdir('./data'):
        if province in element:
            data = pd.read_csv(f'./data/{element}', index_col='datetime')
            print(f'Success to read "{element}" dataframe.')
            break

    data = kwargs['input_data'] if 'input_data' in kwargs else data

    """ 지역명에 맞는 스케일 정보가 담긴 파일을 불러옵니다. """
    for element in os.listdir('./sequence_data'):
        if province in element and '.pickle' in element:
            with open(f'./sequence_data/{element}', 'rb') as f:
                scaler = pickle.load(f)
            print(f'Success to read "{element}" scaler data.')
            break

    """ 지역명에 맞는 모델(.h5)을 불러옵니다. """
    for element in os.listdir('./models'):
        if province in element:
            model = load_model(f'./models/{element}')
            print(f'Success to read "{element}" model.')
            break

    """ 설정된 스케일에 맞게 전처리된 파일을 스케일링 합니다. """
    scaled_data = scaler.transform(data)

    """ 다음 날 결과 데이터를 확인하기 모델 예측을 위한 입력 차원을 조절합니다. """
    tomorrow_predict = model.predict(scaled_data[-period:].reshape(1, period, 3))

    """ 스케일링 된 데이터를 원래의 값(온도)으로 롤백합니다. """
    tomorrow_value = scaler.inverse_transform(tomorrow_predict)
    print('-------------------- 2021-12-24일 예측 결과 --------------------')
    print(f'평균기온: {tomorrow_value[0][0]:.1f}\n최저기온: {tomorrow_value[0][1]:.1f}\n최고기온: {tomorrow_value[0][2]:.1f}')

    """ 예측값 평가하기 """
    for element in os.listdir('./sequence_data'):
        if province in element and '.npy' in element:
            _, x_test, _, y_test = np.load(f'./sequence_data/{element}', allow_pickle=True)
            print(f'Success to read "{element}" sequence data.')
            break
    evaluate_data = model.predict(x_test)

    actual = {'avg_tmp': [], 'min_tmp': [], 'max_tmp': []}
    predict = {'avg_tmp': [], 'min_tmp': [], 'max_tmp': []}
    error = {'avg_tmp': [], 'min_tmp': [], 'max_tmp': []}
    for i in range(len(evaluate_data)):
        for idx, key in enumerate(actual):
            actual[key].append(y_test[i][idx])
            predict[key].append(evaluate_data[i][idx])
            error[key].append(abs(y_test[i][idx] - evaluate_data[i][idx]))

    plt.plot(actual['avg_tmp'][:100], label='actual_avg_tmp', color='red')
    plt.plot(predict['avg_tmp'][:100], label='predict_avg_tmp', color='green')
    plt.plot(error['avg_tmp'][:100], label='error_ratio', color='blue')
    # plt.plot([0 for _ in range(100)], label='base', color='black', linestyle='-')
    plt.legend()
    plt.show()


def predict(province, data):
    period = getPeriod()
    """ 지역명에 맞는 스케일 정보가 담긴 파일을 불러옵니다. """
    for element in os.listdir('./sequence_data'):
        if province in element and '.pickle' in element:
            with open(f'./sequence_data/{element}', 'rb') as f:
                scaler = pickle.load(f)
            print(f'[{datetime.now().strftime("%y-%m-%d %H:%M:%S")}] - Success to read "{element}" scaler data.')
            break

    """ 지역명에 맞는 모델(.h5)을 불러옵니다. """
    for element in os.listdir('./models'):
        if province in element:
            model = load_model(f'./models/{element}')
            print(f'[{datetime.now().strftime("%y-%m-%d %H:%M:%S")}] - Success to read "{element}" model.')
            break

    """ 설정된 스케일에 맞게 전처리된 파일을 스케일링 합니다. """
    scaled_data = scaler.transform(data)

    """ 다음 날 결과 데이터를 확인하기 모델 예측을 위한 입력 차원을 조절합니다. """
    tomorrow_predict = model.predict(scaled_data[-period:].reshape(1, period, 3))

    """ 스케일링 된 데이터를 원래의 값(온도)으로 롤백합니다. """
    tomorrow_value = scaler.inverse_transform(tomorrow_predict)
    # print(f'평균기온: {tomorrow_value[0][0]:.1f}\n최저기온: {tomorrow_value[0][1]:.1f}\n최고기온: {tomorrow_value[0][2]:.1f}')
    return tomorrow_value





if __name__ == '__main__':
    single_predict(province='Cheongju')
