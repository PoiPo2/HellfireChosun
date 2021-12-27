import pandas as pd

pd.set_option('display.max_columns', 20)

#################### 충청남도, 충청북도 ####################

# --------------------- 충청북도 ---------------------
# df1 = pd.read_csv('rawdata/ChungBuk_1_Boeun.csv', index_col=False)      # 보은 - clear
# df2 = pd.read_csv('rawdata/ChungBuk_2_JeCheon.csv', index_col=False)      # 제천 - 평균기온 4개 누락
# df3 = pd.read_csv('rawdata/ChungBuk_3_CheongJu.csv', index_col=False)      # 청주 - clear
# df4 = pd.read_csv('rawdata/ChungBuk_4_ChuPungRyeong.csv', index_col=False)      # 추풍령 - 평균기온 3개 누락
# df5 = pd.read_csv('rawdata/ChungBuk_5_ChungJu.csv', index_col=False)      # 충주 - 평균기온 1개 누락

# print(df1.info())
# print('-------------------------------------------------------------------------------------------------------------------')
# print(df2.info())
# print('-------------------------------------------------------------------------------------------------------------------')
# print(df3.info())
# print('-------------------------------------------------------------------------------------------------------------------')
# print(df4.info())
# print('-------------------------------------------------------------------------------------------------------------------')
# print(df5.info())

# print(df2[df2['평균기온(℃)'].isnull()])
# print(df4[df4['평균기온(℃)'].isnull()])
# print(df5[df5['평균기온(℃)'].isnull()])

# df1 - 보은
# df1.to_csv('./rawdata/ChungBuk_1_Boeun.csv', index=False)

# df3 - 청주
# df3.to_csv('./rawdata/ChungBuk_3_CheongJu.csv', index=False)

# df2 - 제천
# df2.iloc[6545, 3] = 5.0
# df2.iloc[8979, 3] = 24.7
# df2.iloc[10108, 3] = 22.8
# df2.iloc[11237, 3] = 16.8
#
# print(df2.info())
#
# df2.to_csv('./rawdata/ChungBuk_2_JeCheon.csv', index=False)

# df4 - 추풍령
# df4.iloc[9232, 3] = 9.6
# df4.iloc[10853, 3] = 18.7
# df4.iloc[10108, 3] = 20.7
# df4.iloc[10860, 3] = 16.8
#
# print(df4.info())
#
# df4.to_csv('./rawdata/ChungBuk_4_ChuPungRyeong.csv', index=False)

# df5 - 충주
# print(df5.isnull())
# df5.iloc[9989, 3] = 15.8
#
# print(df5.info())
#
# df5.to_csv('./rawdata/ChungBuk_5_ChungJu.csv', index=False)



# --------------------- 충청남도 ---------------------
# df1 = pd.read_csv('rawdata/ChungNam_1_GeumSan.csv', encoding='cp949', index_col=False)      # 금산 - 평균기온 1개
# df2 = pd.read_csv('rawdata/ChungNam_2_BoRyung.csv', encoding='cp949', index_col=False)      # 보령 - 평균기온 1개
# df3 = pd.read_csv('rawdata/ChungNam_3_BuYeo.csv', encoding='cp949', index_col=False)        # 부여 - 평균기온 5개
# df4 = pd.read_csv('rawdata/ChungNam_4_SeoSan.csv', encoding='cp949', index_col=False)       # 서산 - 평균기온 9개, 최고기온 2개, 최저기온 5개
# df5 = pd.read_csv('rawdata/ChungNam_5_CheonAn.csv', encoding='cp949', index_col=False)      # 천안 - 평균기온 2개, 최저기온 1개
#df6 = pd.read_csv('rawdata/ChungNam_6_HongSeong_2015.csv', encoding='cp949', index_col=False)       # 홍성 - 평균기온 3개

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

# print(df1[df1['평균기온(℃)'].isnull()])
# print(df1[df1['최고기온(℃)'].isnull()])
# print(df1[df1['최저기온(℃)'].isnull()])


# df1 - 금산
# df1.iloc[8872, 3] = 8.9
#
# print(df1.info())
# df1.to_csv('./rawdata/ChungNam_1_GeumSan.csv', index=False)

# df2 - 보령
# df2.iloc[10803, 3] = 24.6
#
# print(df2.info())
# df2.to_csv('./rawdata/ChungNam_2_BoRyung.csv', index=False)

# df3 - 부여
# df3.iloc[6801, 3] = 26.8
# df3.iloc[7547, 3] = 27.8
# df3.iloc[10048, 3] = 23.3
# df3.iloc[10049, 3] = 25.2
# df3.iloc[11286, 3] = 8.0
#
# print(df3.info())
# df3.to_csv('./rawdata/ChungNam_3_BuYeo.csv', index=False)

# df4 - 서산
# df4.iloc[9848, 3] = 0.9
# df4.iloc[9858, 3] = -5.0
# df4.iloc[9858, 4] = -2.2
# df4.iloc[9863, 3] = -3.0
# df4.iloc[9863, 4] = 2.0
# df4.iloc[9863, 6] = -6.5
# df4.iloc[9864, 3] = -3.4
# df4.iloc[9864, 6] = -6.6
# df4.iloc[10066, 3] = 28.2
# df4.iloc[10299, 3] = 2.6
# df4.iloc[10378, 3] = 17.2
# df4.iloc[10378, 6] = 12.5
# df4.iloc[10432, 3] = 25.2
# df4.iloc[10432, 6] = 24.5
# df4.iloc[10440, 3] = 28.4
# df4.iloc[10440, 6] = 24.6
#
# print(df4.info())
# df4.to_csv('./rawdata/ChungNam_4_SeoSan.csv', index=False)


# df5 - 천안
# df5.iloc[10555, 3] = 3.6
# df5.iloc[10556, 3] = 10.8
# df5.iloc[10556, 6] = 8.6
#
# print(df5.info())
# df5.to_csv('./rawdata/ChungNam_5_CheonAn.csv', index=False)

# df6 - 홍성
# df6.iloc[268, 3] = 25.3
# df6.iloc[657, 3] = 25.4
# df6.iloc[707, 3] = 17.0
#
# print(df6.info())
# df6.to_csv('./rawdata/ChungNam_6_HongSeong_2015.csv', index=False)