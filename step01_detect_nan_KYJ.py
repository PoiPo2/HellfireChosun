import pandas as pd

df = pd.read_csv('./rawdata/Jeonnam_Wando.csv', encoding='CP949', index_col=False)
print(df)
print(df.info())

print(df[df['평균기온(℃)'].isnull()])
# print('----------------------------------------------')

# print(df[df['최고기온(℃)'].isnull()])
# print('----------------------------------------------')
# print(df[df['최저기온(℃)'].isnull()])
# print('----------------------------------------------')
# print(df[df['최고기온시각'].isnull()])
# print('----------------------------------------------')
# print(df[df['최저기온시각일교차'].isnull()])
# #
df.iloc[9044, 3] = 20.1
df.iloc[9231, 3] = 13.7
df.iloc[10185, 3] = 9.7
df.iloc[10259, 3] = 4.4
df.iloc[10460, 3] = 25.9

df.iloc[10461, 3] = 26.1
df.iloc[10461, 4] = 30.1
df.iloc[10461, 5] = '00:00'
df.iloc[10461, 6] = 23.5
df.iloc[10461, 7] = '00:00'

df.iloc[10462, 3] = 26.5
df.iloc[10462, 4] = 30.8
df.iloc[10462, 5] = '00:00'
df.iloc[10462, 6] = 22.9
df.iloc[10462, 7] = '00:00'

df.iloc[10463, 3] = 23.7
df.iloc[11093, 3] = 20.3
df.iloc[11094, 3] = 16.1

print(df.info())
# # # # # # # # # # # #

df.to_csv('./rawdata/Jeonnam_Wando_process.csv', index=False)
# # # df.to_csv('./rawdata/Jeju_Seogwipo_process.csv', index=False)



