import pandas as pd

pd.set_option('display.max_columns', 20)


#--------------------- 전라남도 ---------------------
# df1 = pd.read_csv('rawdata/Jeonnam_1_Gangjin_2009.csv', encoding='cp949', index_col=False)      # 강진2009 - 평균 15개, 최고 3개, 최저 3개
# df2 = pd.read_csv('rawdata/Jeonnam_2_Goheung.csv', encoding='cp949', index_col=False)       # 고흥 - 평균 2개, 최고 2개
# df3 = pd.read_csv('rawdata/Jeonnam_3_Gwangyang_2011.csv', encoding='cp949', index_col=False)        # 광양2011 - 평균 11개
# df4 = pd.read_csv('rawdata/Jeonnam_4_Mokpo.csv', encoding='cp949', index_col=False)         # 목포 - 최고 1개, 최저 1개
# df5 = pd.read_csv('rawdata/Jeonnam_5_Muan_1993.csv', encoding='cp949', index_col=False)     # 무안1993 - clear
# df6 = pd.read_csv('rawdata/Jeonnam_6_Bosung_2010.csv', encoding='cp949', index_col=False)       # 보성2010 - 평균 4개
# df7 = pd.read_csv('rawdata/Jeonnam_7_Suncheon_2011.csv', encoding='cp949', index_col=False)     # 순천2011 - 평균 10개
# df8 = pd.read_csv('rawdata/Jeonnam_8_Yeosu.csv', encoding='cp949', index_col=False)         # 여수 - clear
# df9 = pd.read_csv('rawdata/Jeonnam_9_Younggwang_2008.csv', encoding='cp949', index_col=False)       # 영광2008 - 평균 17개, 최고 1개

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

# print(df1[df1['평균기온(℃)'].isnull()])
# print(df1[df1['최고기온(℃)'].isnull()])
# print(df1[df1['최저기온(℃)'].isnull()])

# 평균기온 - 3, 최고기온 - 4, 최저기온 - 6

# df1 - 강진 2009년~ (평균 15개, 최고 3개, 최저 3개)
# df1.iloc[6, 3] = 3.2
# df1.iloc[1388, 3] = 25.9
# df1.iloc[2805, 3] = 25.1
# df1.iloc[2806, 3] = 27.6
# df1.iloc[2806, 4] = 29.7
# df1.iloc[2806, 6] = 25.6
# df1.iloc[2807, 3] = 27.6
# df1.iloc[2807, 4] = 29.7
# df1.iloc[2807, 6] = 25.6
# df1.iloc[2808, 3] = 30.1
# df1.iloc[2809, 3] = 29.3
# df1.iloc[2810, 3] = 29.9
# df1.iloc[2812, 3] = 28.9
# df1.iloc[2813, 3] = 26.6
# df1.iloc[2813, 4] = 29.6
# df1.iloc[2813, 6] = 23.7
# df1.iloc[2814, 3] = 24.5
# df1.iloc[2962, 3] = 1.1
# df1.iloc[3218, 3] = 25.7
# df1.iloc[3571, 3] = 27.5
# df1.iloc[4103, 3] = 2.0
#
# print(df1.info())
# df1.to_csv('./rawdata/Jeonnam_1_Gangjin_2009.csv', index=False)

# df2 - 고흥 (평균 2개, 최고 2개)
# df2.iloc[7812, 3] = 20.5
# df2.iloc[7812, 4] = 28.2
# df2.iloc[7937, 3] = 21.0
# df2.iloc[7937, 4] = 27.2
#
# print(df2.info())
# df2.to_csv('./rawdata/Jeonnam_2_Goheung.csv', index=False)

# df3 - 광양군 2011년~ (평균 11개)
# df3.iloc[857, 3] = 27.7
# df3.iloc[858, 3] = 27.6
# df3.iloc[859, 3] = 28.3
# df3.iloc[2315, 3] = 24.4
# df3.iloc[2327, 3] = 27.5
# df3.iloc[2328, 3] = 27.8
# df3.iloc[2677, 3] = 23.6
# df3.iloc[2678, 3] = 28.6
# df3.iloc[2684, 3] = 24.3
# df3.iloc[2731, 3] = 27.0
# df3.iloc[3584, 3] = 7.6
#
# print(df3.info())
# df3.to_csv('./rawdata/Jeonnam_3_Gwangyang_2011.csv', index=False)

# df4 - 목포 (최고 1개, 최저 1개)
# df4.iloc[9148, 4] = 1.9
# df4.iloc[9147, 6] = 3.1
#
# print(df4.info())
# df4.to_csv('./rawdata/Jeonnam_4_Mokpo.csv', index=False)

# df5 - 무안 1993년~ (clear)

# print(df5.info())
# df5.to_csv('./rawdata/Jeonnam_5_Muan_1993.csv', index=False)

# df6 - 보성 2010년~ (평균 4개)
# df6.iloc[1819, 3] = 1.4
# df6.iloc[1820, 3] = 3.9
# df6.iloc[1846, 3] = 1.9
# df6.iloc[3138, 3] = 21.8
#
# print(df6.info())
# df6.to_csv('./rawdata/Jeonnam_6_Bosung_2010.csv', index=False)

# df7 - 순천 2011년~ (평균 10개)
# df7.iloc[550, 3] = 17.6
# df7.iloc[1429, 3] = -0.7
# df7.iloc[2482, 3] = 4.8
# df7.iloc[2566, 3] = 11.2
# df7.iloc[2647, 3] = 21.1
# df7.iloc[2958, 3] = 11.8
# df7.iloc[3049, 3] = 27.9
# df7.iloc[3105, 3] = 20.4
# df7.iloc[3162, 3] = 6.5
# df7.iloc[3214, 3] = 1.2
#
# print(df7.info())
# df7.to_csv('./rawdata/Jeonnam_7_Suncheon_2011.csv', index=False)

# df8 - 여수 (clear)

# print(df8.info())
# df8.to_csv('./rawdata/Jeonnam_8_Yeosu.csv', index=False)

# df9 - 영광 2008년~ (평균 17개, 최고 1개)
# df9.iloc[206, 3] = 27.3
# df9.iloc[301, 3] = 14.6
# df9.iloc[533, 3] = 23.2
# df9.iloc[550, 3] = 23.5
# df9.iloc[796, 3] = 6.6
# df9.iloc[1153, 3] = 10.5
# df9.iloc[2127, 3] = 10.0
# df9.iloc[2128, 3] = 15.0
# df9.iloc[2547, 3] = -0.1
# df9.iloc[3520, 3] = 27.4
# df9.iloc[3690, 3] = -8.1
# df9.iloc[3885, 3] = 26.5
# df9.iloc[4030, 3] = 1.8
# df9.iloc[4150, 3] = 18.1
# df9.iloc[4287, 3] = 22.8
# df9.iloc[4858, 3] = 12.2
# df9.iloc[4985, 3] = 26.6
# df9.iloc[4075, 4] = 11.9
#
#
# print(df9.info())
# df9.to_csv('./rawdata/Jeonnam_9_Younggwang_2008.csv', index=False)