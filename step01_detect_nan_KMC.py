import pandas as pd

filepath = './rawdata/Jeonnam_16_Heuksando.csv'
# df = pd.read_csv(filepath, index_col=False, encoding='cp949')
df = pd.read_csv(filepath, index_col=False)
df.info()

# print(df1[df1['최저기온(℃)'].isnull()])
""" df.iloc[n, m] 에서 n은 인덱스 번호, m은 컬럼 번호이다.
    m=3 (평균기온), m=4 (최고기온), m=6 (최저기온)  """
# df.iloc[10493, 3] = 18.6
# df.iloc[10941, 3] = -5.1
df.to_csv(filepath, index=False)
# df.iloc[9463, 3] = 0.3
# df.iloc[10492, 3] = 13.9
# df.iloc[7749, 4] = 10.1
# df.iloc[7749, 3] = 2.4
# df.iloc[7807, 4] = 22.7
# df.iloc[7807, 3] = 14.3
# df.iloc[9713, 3] = 29.3
# df.iloc[9714, 3] = 29.9


# print(df.iloc[2554:2557])
# df.iloc[2555, 4] = 32.0
# df.iloc[2555, 3] = 28.1
# print(df.iloc[2554:2557])

# df.iloc[9511, 3] = -8.0
# df.iloc[9849, 3] = -6.0
# df.iloc[10306, 3] = 8.4
# df.iloc[10403, 3] = 23.3
# df.info()

# df.to_csv(filepath, index=False)
#
# # print(df1[df1['최저기온(℃)'].isnull()])
# df1.iloc[6578, 6] = -4.8
# print(df1.info())
# df1.to_csv('./rawdata/GyeongGi_1_DongDuCheon.csv', index=False)
# print(df1.iloc[4622:4625])
# df = pd.read_csv('./rawdata/GyeongGi_1_DongDuCheon_1.csv', index_col=False)
# print(df.head(5))

