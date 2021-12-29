from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from step03_preprocessing_KMC import getPeriod
import matplotlib.pyplot as plt
import numpy as np
import os
import time


""" (경로 수정 금지) 파일을 불러오거나 저장하는 경로를 설정합니다. """
LOAD_PATH = './sequence_data'
SAVE_PATH = './models'              # 없으면 models 이름으로 폴더를 만드셔야 합니다.

""" 자동으로 시퀀스데이터를 불러오고 모델 생성에 필요한 파일명에 사용될 지역명을 입력합니다. """
REGION = 'Gyeonggi'

if __name__ == '__main__':
    for element in os.listdir(LOAD_PATH):
        """ 시퀀스데이터(.npy)만 LOAD_PATH 에서 불러옵니다. """
        if REGION in element and '.npy' in element:
            start_time = time.time()
            filename = element.split('sequence')[0]
            model_filename = ''.join([filename, 'model.h5'])
            """ 시퀀스데이터(.npy)를 불러옵니다. """
            x_train, x_test, y_train, y_test = np.load(f'{LOAD_PATH}/{element}', allow_pickle=True)

            """ LSTM 네트워크를 생성합니다. """
            model = Sequential([LSTM(256, input_shape=(getPeriod(), 3), activation='tanh', return_sequences=True),
                                Dropout(0.3),
                                LSTM(128, activation='tanh', return_sequences=True),
                                Dropout(0.2),
                                LSTM(64, activation='tanh', return_sequences=True),
                                Dropout(0.2),
                                LSTM(32, activation='tanh', return_sequences=False),
                                Dropout(0.1),
                                Flatten(),
                                Dense(3)])
            model.compile(loss='mse', optimizer='adam')

            """ 생성된 LSTM 모델을 학습합니다. """
            fit_hist = model.fit(x_train, y_train, epochs=100, validation_data=(x_test, y_test), shuffle=False,
                                 verbose=1)

            """ 모델을 저장합니다. """
            model.save(f'{SAVE_PATH}/{model_filename}')
            print(f'"{model_filename}" is saved.')
            print(f'runtime is {round(time.time() - start_time, 3)} seconds.')

            """ 학습이 완료된 모델의 척도를 그래프로 표현하고 저장합니다. """
            plt.plot(fit_hist.history['loss'], label='loss')
            plt.plot(fit_hist.history['val_loss'], label='val_loss')
            plt.legend()
            plt.savefig(f'./{model_filename}.png')
