import pandas as pd

pd.set_option('display.max_columns', 20)


#--------------------- 전라북도 ---------------------
# df1 = pd.read_csv('rawdata/Jeonbuk_1_Gochang_2010.csv', encoding='cp949', index_col=False)      # 고창2010 - 평균기온 11개, 최고기온 2개, 최저기온 1개
# df2 = pd.read_csv('rawdata/JeonBuk_2_GunSan.csv', encoding='cp949', index_col=False)        # 군산
# df3 = pd.read_csv('rawdata/JeonBuk_3_NamWon.csv', index_col=False)        # 남원 - 평균기온 9 개, 최고기온 2개, 최저기온 3개
# df4 = pd.read_csv('rawdata/JeonBuk_4_BuAn.csv', encoding='cp949', index_col=False)      # 부안 - 평균기온 2개, 최고기온 1개
# df5 = pd.read_csv('rawdata/JeonBuk_5_SunChang_2008.csv', encoding='cp949', index_col=False)     # 순창2008 - 평균기온 19개, 최고기온 2개, 최저기온 2개
# df6 = pd.read_csv('rawdata/JeonBuk_6_ImSil.csv', encoding='cp949', index_col=False)         # 임실 - 평균기온 5개
# df7 = pd.read_csv('rawdata/JeonBuk_7_JangSoo.csv', encoding='cp949', index_col=False)       # 장수 - 평균기온 5개, 최고기온 1개, 최저개온 1개
# df8 = pd.read_csv('rawdata/JeonBuk_8_JeonJu.csv', encoding='cp949', index_col=False)        # 전주 - 최저기온 1개
# df9 = pd.read_csv('rawdata/JeonBuk_9_JeongEub.csv', encoding='cp949', index_col=False)      # 정읍 - 평균기온 2개, 최저기온 1개

# print(df1.info())
# print('-------------------------------------------------------------------------------------------------------------------')
# print(df2.info())
# print('-------------------------------------------------------------------------------------------------------------------')
# print(df3.info())
# print('-------------------------------------------------------------------------------------------------------------------')
# print(df4.info())
# print('-------------------------------------------------------------------------------------------------------------------')
# print(df5.info())
# print('-------------------------------------------------------------------------------------------------------------------')
# print(df6.info())
# print('-------------------------------------------------------------------------------------------------------------------')
# print(df7.info())
# print('-------------------------------------------------------------------------------------------------------------------')
# print(df8.info())
# print('-------------------------------------------------------------------------------------------------------------------')
# print(df9.info())

# print(df5[df5['평균기온(℃)'].isnull()])
# print(df5[df5['최고기온(℃)'].isnull()])
# print(df5[df5['최저기온(℃)'].isnull()])


# 평균기온 - 3, 최고기온 - 4, 최저기온 - 6

# df1 - 고창 2010년~ (평균 11개, 최고 2개, 최저 1개)
# df1.iloc[2220, 3] = 0.1
# df1.iloc[2536, 3] = 14.9
# df1.iloc[2768, 3] = 22.9
# df1.iloc[3081, 3] = 14.7
# df1.iloc[3177, 3] = 29.3
# df1.iloc[3202, 3] = 24.6
# df1.iloc[3641, 3] = 16.8
# df1.iloc[3718, 3] = -1.0
# df1.iloc[3718, 4] = 2.3
# df1.iloc[3924, 3] = 22.1
# df1.iloc[3925, 3] = 25.0
# df1.iloc[3925, 4] = 27.4
# df1.iloc[3925, 6] = 22.6
# df1.iloc[3926, 3] = 28.0
#
# print(df1.info())
# df1.to_csv('./rawdata/Jeonbuk_1_Gochang_2010.csv', index=False)

# df2 - 군산 (clear)
# print(df2.info())
# df2.to_csv('./rawdata/JeonBuk_2_GunSan.csv', index=False)

# df3 - 남원 (평균 9개, 최고 2개, 최저 3개)
# df3.iloc[9125, 3] = 3.5
# df3.iloc[9691, 6] = 21.3
# df3.iloc[9857, 3] = -4.1
# df3.iloc[10571, 3] = 7.9
# df3.iloc[10580, 3] = 0.7
# df3.iloc[10596, 3] = 1.4
# df3.iloc[10614, 3] = 5.6
# df3.iloc[10636, 3] = 10.1
# df3.iloc[11093, 3] = 21.4
# df3.iloc[11093, 4] = 21.6
# df3.iloc[11093, 6] = 21.2
# df3.iloc[11094, 3] = 20.1
# df3.iloc[11094, 4] = 22.6
# df3.iloc[11094, 6] = 17.7
#
# print(df3.info())
# df3.to_csv('./rawdata/JeonBuk_3_NamWon.csv', index=False)

# df4 - 부안(평균 2개, 최고 1개)
# df4.iloc[9691, 3] = 27.8
# df4.iloc[9743, 3] = 25.0
# df4.iloc[9824, 4] = 5.7
#
# print(df4.info())
# df4.to_csv('./rawdata/JeonBuk_4_BuAn.csv', index=False)

# df5 - 순창 2008년~ (평균 19개, 최고 2개, 최저 2개)
# df5.iloc[91, 3] = 17.4
# df5.iloc[2105, 3] = 15.5
# df5.iloc[2407, 3] = 2.2
# df5.iloc[2432, 3] = 7.3
# df5.iloc[2567, 3] = 26.8
# df5.iloc[2881, 3] = 19.3
# df5.iloc[3147, 3] = 1.6
# df5.iloc[3442, 3] = -0.4
# df5.iloc[3443, 3] = -0.6
# df5.iloc[3443, 4] = 2.9
# df5.iloc[3443, 6] = -4.2
# df5.iloc[3444, 3] = 0.6
# df5.iloc[3450, 3] = -3.2
# df5.iloc[3498, 3] = -1.2
# df5.iloc[3702, 3] = 22.3
# df5.iloc[3703, 3] = 22.8
# df5.iloc[4152, 3] = 3.9
# df5.iloc[4160, 3] = -1.3
# df5.iloc[4161, 3] = 0.9
# df5.iloc[4161, 4] = 7.1
# df5.iloc[4161, 6] = -5.2
# df5.iloc[4162, 3] = 3.1
# df5.iloc[4741, 3] = 27.5
#
# print(df5.info())
# df5.to_csv('./rawdata/JeonBuk_5_SunChang_2008.csv', index=False)

# df6 - 임실 (평균 5개)
# df6.iloc[7805, 3] = 16.3
# df6.iloc[7843, 3] = 22.8
# df6.iloc[9538, 3] = -4.6
# df6.iloc[10942, 3] = -5.9
# df6.iloc[10974, 3] = -3.8
#
# print(df6.info())
# df6.to_csv('./rawdata/JeonBuk_6_ImSil.csv', index=False)

# df7 - 장수 (평균 5개, 최고 1개, 최저 1개)
# df7.iloc[9149, 6] = -9.4
# df7.iloc[9872, 3] = -13.9
# df7.iloc[10540, 3] = 6.5
# df7.iloc[10541, 3] = 9.0
# df7.iloc[10541, 4] = 12.3
# df7.iloc[11261, 3] = 10.9
# df7.iloc[11304, 3] = -2.0
#
# print(df7.info())
# df7.to_csv('./rawdata/JeonBuk_7_JangSoo.csv', index=False)

# df8 - 전주 (최저 1개)
# df8.iloc[9823, 6] = 0.3
#
# print(df8.info())
# df8.to_csv('./rawdata/JeonBuk_8_JeonJu.csv', index=False)

# df9 - 정읍 (평균 2개, 최저 1개)
# df9.iloc[8753, 3] = -1.9
# df9.iloc[10795, 3] = 22.2
# df9.iloc[9692, 6] = 22.4
#
# print(df9.info())
# df9.to_csv('./rawdata/JeonBuk_9_JeongEub.csv', index=False)