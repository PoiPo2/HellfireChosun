from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
import pickle
import pandas as pd
import time


if __name__ == '__main__':
    start_time = time.time()
    # _, x_test, _, y_test = np.load('./training_metadata_730.npy', allow_pickle=True)
    # _, x_test, _, y_test = np.load('./training_metadata_Mungyeong_730.npy', allow_pickle=True)
    _, x_test, _, y_test = np.load('./training_metadata_Mungyeong_30.npy', allow_pickle=True)
    # model = load_model('./test_model_Mungyeong_part3.h5')
    model = load_model('./model_GB-3-5.h5')
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

    """ 스케일러 파일을 불러옵니다. (미구현)(정상 동작 안됌) """
    # minmaxscaler = None
    # with open('./scaler.pickle', 'rb') as f:
    #     minmaxscaler = pickle.load(f)
    #     # dummy = minmaxscaler.transform(predict)
    #     dummy = minmaxscaler.inverse_transform(predict)
    #     print(dummy)



