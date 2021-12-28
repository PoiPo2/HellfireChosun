from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


""" 전처리하고자 하는 csv 파일을 불러옵니다. """
raw_data = pd.read_csv('./data/Gyeonggi_2_Suwon_renew_11315.csv', index_col='datetime')

data = raw_data[-730:]
# print(f'{data}\n{type(data)}')
""" 데이터를 차트로 그려 분포를 확인합니다. """
# data.plot()
# plt.show()
# print(data[:5])
# print(min(data['avg_tmp']))
# print(max(data['avg_tmp']))

""" 모든 데이터 값들을 0과 1사이의 값으로 스케일링(Scaling) 합니다. """
minmaxscaler = MinMaxScaler()
scaled_data = minmaxscaler.fit_transform(data)
# print(data[:10]['avg_tmp'])
# print(scaled_data[:10])


""" 시퀀스(Sequence) 데이터를 생성하기 위한 리스트를 정의합니다. """
sequence_x, sequence_y = [], []
""" 시퀀스 데이터의 주기(period)를 정의합니다. 단위는 일(day) 입니다. """
period = 30
for idx in range(len(scaled_data) - period):
    x = scaled_data[idx:idx + period]
    y = scaled_data[idx + period]
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
x_train, x_test, y_train, y_test = train_test_split(sequence_x, sequence_y, test_size=0.1)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

""" 모델 """
model = Sequential(name='model_exam')
model.add(LSTM(30, input_shape=(30, 3), activation='tanh'))
model.add(Dropout(0.2))
# model.add(LSTM(64, activation='tanh'))
# model.add(Dropout(0.1))
model.add(Flatten())
model.add(Dense(3))
model.compile(loss='mse', optimizer='sgd')
model.summary()

fit_hist = model.fit(x_train, y_train, epochs=50, validation_data=(x_test, y_test), shuffle=False)
plt.plot(fit_hist.history['loss'], label='loss')
plt.plot(fit_hist.history['val_loss'], label='val_loss')
plt.legend()
plt.show()
