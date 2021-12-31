from datetime import datetime, timedelta
from tensorflow.keras.layers import *
from tensorflow.keras.models import load_model, Sequential
import matplotlib.pyplot as plt
import numpy as np
import os
import pickle
import pandas as pd
import time
from step03_preprocessing_KMC import getPeriod

# Global constants
# _, X_TEST, _, Y_TEST = np.load('./training_metadata_Mungyeong_30.npy', allow_pickle=True)
_, X_TEST, _, Y_TEST = np.load('./Gyeongbuk_4_Bonghwa_sequence30.npy', allow_pickle=True)
MODEL = load_model('./Gyeongbuk_4_Bonghwa_model_1.h5')


def predictTomorrowResult():
    actual = {'avg_tmp': [], 'min_tmp': [], 'max_tmp': []}
    prediction = {'avg_tmp': [], 'min_tmp': [], 'max_tmp': []}
    data = pd.read_csv('./data/Gyeongbuk_3_Mungyeong_renew_11315.csv', index_col='datetime')
    before_time = (datetime.now() + timedelta(days=-30)).strftime('%Y-%m-%d')
    print(f'before_time: {before_time}')
    period = getPeriod()
    # print(data.loc[before_time:])
    print(len(data.loc[before_time:]))
    # before_time = (datetime.now() + timedelta(days=-30)).strftime('%Y-%m-%d')
    # print(f'before_time: {before_time}')
    # print(len(data.loc[before_time:]))

    """ 스케일러 정보가 담긴 파일을 불러옵니다. """
    with open('./scaler.pickle', 'rb') as f:
        minmaxscaler = pickle.load(f)
    scaled_data = minmaxscaler.transform(data)

    """ 다음 날 결과 데이터를 확인하기 모델 예측을 위한 입력 차원을 조절합니다. """
    tomorrow_predict = MODEL.predict(scaled_data[-period:].reshape(1, period, 3))
    # print(tomorrow_predict)
    # print(tomorrow_predict[0][0])

    """ 스케일링 된 데이터를 원래의 값(온도)으로 롤백합니다. """
    tomorrow_value = minmaxscaler.inverse_transform(tomorrow_predict)
    print('---------------------')
    print(tomorrow_value)
    print(f'예측한 평균기온: {tomorrow_value[0][0]:.1f}\n예측한 최저기온: {tomorrow_value[0][1]:.1f}\n예측한 최고기온: {tomorrow_value[0][2]:.1f}')





    # preds = models.predict(scaled_data[-period:].reshape(1, period, 3))
    # preds_val = minmaxscaler.inverse_transform(preds)
    # print(f'before avg_tmp: {preds_val[0][0]:.1f}\nbefore min_tmp: {preds_val[0][1]:.1f}\nbefore max_tmp: {preds_val[0][2]:.1f}')
    #
    # models.load_weights(f'./checkpoint/Gyeongbuk_4_Bonghwa_model_2.ckpt')
    # preds = models.predict(scaled_data[-period:].reshape(1, period, 3))
    # preds_val = minmaxscaler.inverse_transform(preds)
    # print(f'after avg_tmp: {preds_val[0][0]:.1f}\nafter min_tmp: {preds_val[0][1]:.1f}\nafter max_tmp: {preds_val[0][2]:.1f}')


""" (경로 수정 금지) 파일을 불러오거나 저장하는 경로를 설정합니다. """
LOAD_PATH = './models'
SAVE_PATH = './models'              # 없으면 models 이름으로 폴더를 만드셔야 합니다.


def predict(province):
    sequence_data = None
    scaler = None
    period = getPeriod()
    """ 지역명에 맞는 전처리된 파일(.csv)을 불러옵니다. """
    for element in os.listdir('./data'):
        if province in element:
            data = pd.read_csv(f'./data/{element}', index_col='datetime')
            print(f'Success to read "{element}" data.')
            break

    """ 지역명에 맞는 스케일 정보가 담긴 파일을 불러옵니다. """
    for element in os.listdir('./sequence_data'):
        if province in element and '.pickle' in element:
            with open(f'./sequence_data/{element}', 'rb') as f:
                scaler = pickle.load(f)
            print(f'Success to read "{element}" data.')
            break

    """ 설정된 스케일에 맞게 전처리된 파일을 스케일링 합니다. """
    scaled_data = scaler.transform(data)

    """ 다음 날 결과 데이터를 확인하기 모델 예측을 위한 입력 차원을 조절합니다. """
    tomorrow_predict = MODEL.predict(scaled_data[-period:].reshape(1, period, 3))

    """ 스케일링 된 데이터를 원래의 값(온도)으로 롤백합니다. """
    tomorrow_value = scaler.inverse_transform(tomorrow_predict)
    print('-------------------- 2021-12-24일 예측 결과 --------------------')
    print(f'평균기온: {tomorrow_value[0][0]:.1f}\n최저기온: {tomorrow_value[0][1]:.1f}\n최고기온: {tomorrow_value[0][2]:.1f}')

    """ 예측값 평가하기 """
    _, x_test, _, y_test = np.load('./sequence_data/Gyeonggi_1_Dongducheon_sequence.npy', allow_pickle=True)
    evaluate_data = MODEL.predict(x_test)

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
    plt.axis
    plt.legend()
    plt.show()






if __name__ == '__main__':
    predict(province='Dongducheon')
    # predictTomorrowResult()
    exit()
    start_time = time.time()
    # _, x_test, _, y_test = np.load('./training_metadata_730.npy', allow_pickle=True)
    # _, x_test, _, y_test = np.load('./training_metadata_Mungyeong_730.npy', allow_pickle=True)
    _, x_test, _, y_test = np.load('./training_metadata_Mungyeong_30.npy', allow_pickle=True)
    # model = load_model('./test_model_Mungyeong_part3.h5')
    model = load_model('./model_GB-3-6.h5')
    predict = model.predict(x_test)

    actual_dict = {'avg_tmp': [], 'min_tmp': [], 'max_tmp': []}
    predict_dict = {'avg_tmp': [], 'min_tmp': [], 'max_tmp': []}
    error_dict = {'avg_tmp': [], 'min_tmp': [], 'max_tmp': []}
    abs_error_dict = {'avg_tmp': [], 'min_tmp': [], 'max_tmp': []}
    for i in range(len(predict)):
        for idx, key in enumerate(actual_dict):
            actual_dict[key].append(y_test[i][idx])
            predict_dict[key].append(predict[i][idx])
            error_dict[key].append(y_test[i][idx] - predict[i][idx])
            abs_error_dict[key].append(abs(y_test[i][idx] - predict[i][idx]))

    avg_error_ratio_dict = pd.DataFrame()
    avg_error_ratio_dict['avg_tmp'] = (round(sum(abs_error_dict["avg_tmp"]) / len(abs_error_dict["avg_tmp"]), 6))
    avg_error_ratio_dict['min_tmp'] = (round(sum(abs_error_dict["min_tmp"]) / len(abs_error_dict["min_tmp"]), 6))
    avg_error_ratio_dict['max_tmp'] = (round(sum(abs_error_dict["max_tmp"]) / len(abs_error_dict["max_tmp"]), 6))
    avg_error_ratio_dict.reset_index(inplace=True)

    avg_error_ratio = round(sum(abs_error_dict["avg_tmp"]) / len(abs_error_dict["avg_tmp"]), 6)
    maximum_error = [round(max(error_dict['avg_tmp']), 6), round(max(error_dict['min_tmp']), 6), round(max(error_dict['max_tmp']), 6)]
    average_error = [round(sum(abs_error_dict["avg_tmp"]) / len(abs_error_dict["avg_tmp"]), 6),
                     round(sum(abs_error_dict["min_tmp"]) / len(abs_error_dict["min_tmp"]), 6),
                     round(sum(abs_error_dict["max_tmp"]) / len(abs_error_dict["max_tmp"]), 6)]
    print(f'최대 에러량: {maximum_error[0]}, {maximum_error[1]}, {maximum_error[2]}, (avg: {round(sum(maximum_error) / 3, 6)})')
    print(f'평균 에러량: {average_error[0]}, {average_error[1]}, {average_error[2]}, (avg: {round(sum(average_error) / 3, 6)})')
    print(f'runtime is {round(time.time() - start_time, 3)} seconds.')

    plt.plot(actual_dict['avg_tmp'][:100], label='actual_avg_tmp', color='red')
    plt.plot(predict_dict['avg_tmp'][:100], label='predict_avg_tmp', color='green')
    plt.plot(abs_error_dict['avg_tmp'][:100], label='abs_error_ratio', color='blue')
    # plt.plot([0 for _ in range(100)], label='base', color='black', linestyle='-')
    plt.legend()
    plt.show()
