import pandas as pd

df1 = pd.read_csv('./rawdata/Incheon_1.csv', encoding='cp949', index_col=False)
print(df1.head(5))

df2 = pd.read_csv('./rawdata/Incheon_2.csv', encoding='cp949', index_col=False)
print(df2.head(5))

df3 = pd.read_csv('./rawdata/Incheon_3.csv', encoding='cp949', index_col=False)
print(df3.head(5))
print('----------------------------------------------------------------------------------------------------')
l1_avg_temperature = list(map(float, df1['평균기온(℃)'][:5]))
l2_avg_temperature = list(map(float, df1['평균기온(℃)'][:5]))
l3_avg_temperature = list(map(float, df1['평균기온(℃)'][:5]))
# df1.reset_index(inplace=True)
print(l1_avg_temperature)

# new_df = list(df1['평균기온(℃)'][:5]) + list(df2['평균기온(℃)'][:5])
# print(new_df)