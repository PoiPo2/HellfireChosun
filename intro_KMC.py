import pandas as pd

df1 = pd.read_csv('./rawdata/Incheon_1.csv', encoding='cp949', index_col=False)
print(df1.head(5))

df2 = pd.read_csv('./rawdata/Incheon_2.csv', encoding='cp949', index_col=False)
print(df2.head(5))

df3 = pd.read_csv('./rawdata/Incheon_3.csv', encoding='cp949', index_col=False)
print(df3.head(5))
print('----------------------------------------------------------------------------------------------------')
l1_avg_temperature = list(map(float, df1['평균기온(℃)']))       # 강화도의 평균 기온
l2_avg_temperature = list(map(float, df2['평균기온(℃)']))       # 백령도의 평균 기온
l3_avg_temperature = list(map(float, df3['평균기온(℃)']))       # 인천의 평균 기온
print(l1_avg_temperature)
print(l2_avg_temperature)
print(l3_avg_temperature)

# 새로운 데이터프레임을 생성하기 위해 리스트를 생성한다.
# n개 지역의 "평균 온도"를 산출하기 위해 이하 반복문을 시행한다.
avg_temperature = []
for i in range(len(l1_avg_temperature)):
    avg = round((l1_avg_temperature[i] + l2_avg_temperature[i] + l3_avg_temperature[i]) / 3, 1)
    avg_temperature.append(avg)

print(f'avg_temperature: {avg_temperature}')
print(len(avg_temperature))

print('----------------------------------------------------------------------------------------------------')
l1_max_temperature = list(map(float, df1['최고기온(℃)']))       # 강화도의 최고 기온
l2_max_temperature = list(map(float, df2['최고기온(℃)']))       # 백령도의 최고 기곤
l3_max_temperature = list(map(float, df3['최고기온(℃)']))       # 인천의 최고 기온
print(l1_max_temperature)
print(l2_max_temperature)
print(l3_max_temperature)

max_temperature = []
for i in range(len(l1_max_temperature)):
    max_tmp = round((l1_max_temperature[i] + l2_max_temperature[i] + l3_max_temperature[i]) / 3, 1)
    max_temperature.append(max_tmp)

print(f'max_temperature: {max_temperature}')

print('----------------------------------------------------------------------------------------------------')
l1_min_temperature = list(map(float, df1['최저기온(℃)']))       # 강화도의 최저 기온
l2_min_temperature = list(map(float, df2['최저기온(℃)']))       # 백령도의 최저 기온
l3_min_temperature = list(map(float, df3['최저기온(℃)']))       # 인천의 최저 기온
print(l1_min_temperature)
print(l2_min_temperature)
print(l3_min_temperature)

min_temperature = []
for i in range(len(l1_min_temperature)):
    min_tmp = round((l1_min_temperature[i] + l2_min_temperature[i] + l3_min_temperature[i]) / 3, 1)
    min_temperature.append(min_tmp)

print(f'min_temperature: {min_temperature}')

# 날짜(일시) 리스트 생성
print('----------------------------------------------------------------------------------------------------')
timestamp = list(df1['일시'])
print(type(timestamp), timestamp)
print(len(timestamp))

new_df = pd.DataFrame()
new_df['datetime'] = timestamp
new_df['avg_temp'] = avg_temperature
new_df['max_temp'] = max_temperature
new_df['min_temp'] = min_temperature

print(new_df.info())
print(new_df.head(5))
print(type(new_df))
print('----------------------------------------------------------------------------------------------------')
