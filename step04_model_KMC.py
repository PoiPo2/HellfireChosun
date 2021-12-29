from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from step03_preprocessing import getPeriod
import matplotlib.pyplot as plt
import numpy as np
import time


FILENAME = 'model_GB-3-5.h5'

if __name__ == '__main__':
    start_time = time.time()
    """ step03 과정에서 설정한 주기(period)값을 불러옵니다. """
    period = getPeriod()
    """ step03 과정에서 저장했던 학습 데이터를 불러옵니다. """
    # x_train, x_test, y_train, y_test = np.load(f'./training_metadata_{period}.npy', allow_pickle=True)
    # x_train, x_test, y_train, y_test = np.load(f'./training_metadata_Mungyeong_730.npy', allow_pickle=True)
    x_train, x_test, y_train, y_test = np.load(f'./training_metadata_Mungyeong_30.npy', allow_pickle=True)

    model = Sequential(name='exam')
    """ 전체적인 성능 개선을 위한 방법으로는 아래의 방법을 생각해볼만 합니다. """
    """ 1. LSTM Layer 갯수 및 파라미터 조절 """
    """ 2. Dropout과 같은 과적합방지 알고리즘의 적절한 사용 """
    """ 3. epochs(학습량)의 적절한 조절 """
    """ 4. 손실함수(loss-function) 및 최적화함수(optimizer)의 적절한 사용 """
    model.add(LSTM(768, input_shape=(period, 3), activation='tanh', return_sequences=True))
    model.add(Dropout(0.3))
    model.add(LSTM(512, activation='tanh', return_sequences=True))
    model.add(Dropout(0.25))
    model.add(LSTM(256, activation='tanh', return_sequences=True))
    model.add(Dropout(0.25))
    model.add(LSTM(128, activation='tanh', return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(64, activation='tanh', return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(32, activation='tanh', return_sequences=False))
    model.add(Dropout(0.1))
    model.add(Flatten())
    model.add(Dense(3))
    model.compile(loss='mse', optimizer='adam')
    model.summary()

    fit_hist = model.fit(x_train, y_train, epochs=60, validation_data=(x_test, y_test), shuffle=False)
    model.save(f'./{FILENAME}')
    print(f'"{FILENAME}" is saved.')
    print(f'runtime is {round(time.time() - start_time, 3)} seconds.')

    plt.plot(fit_hist.history['loss'], label='loss')
    plt.plot(fit_hist.history['val_loss'], label='val_loss')
    plt.legend()
    plt.show()
