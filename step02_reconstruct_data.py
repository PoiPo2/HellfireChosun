import os
import pandas as pd

FILE_PATH = './rawdata/'
NEW_FILE_PATH = './data/'
REGION = {'서울': 'Seoul', '부산': 'Busan', '대구': 'Daegu', '인천': 'Incheon', '광주': 'Gwangju', '대전': 'Daejeon',
          '울산': 'Ulsan', '세종': 'Sejong', '제주': 'Jeju', '경기': 'Gyeonggi', '강원': 'Gangwon', '충북': 'Chungbuk',
          '충남': 'Chungnam', '전북': 'Jeonbuk', '전남': 'Jeonnam', '경북': 'Gyeongbuk', '경남': 'Gyeongnam'}


def getCSVFiles(region_name):
    files_list = []
    """ FILE_PATH 경로에 있는 모든 파일들을 리스트 형태로 받아옵니다. """
    for file_name in os.listdir(FILE_PATH):
        if REGION[region_name] in file_name:
            files_list.append(file_name)

    return files_list


def reconstructDataFrame(files):
    count = 0
    for idx in range(len(files)):
        """ NaN 값이 제거된 csv 파일을 불러옵니다. """
        org_dataframe = pd.read_csv(f'{FILE_PATH}/{files[idx]}')
        """ 새로운 데이터프레임(dataframe)을 정의합니다. """
        dataframe = pd.DataFrame()
        dataframe['datetime'] = org_dataframe['일시']
        dataframe['avg_tmp'] = org_dataframe['평균기온(℃)']
        dataframe['min_tmp'] = org_dataframe['최저기온(℃)']
        dataframe['max_tmp'] = org_dataframe['최고기온(℃)']
        """ 생성될 데이터프레임의 파일명을 정의합니다. """
        data_length = len(dataframe['datetime'])
        file_name = f'{files[idx].split(".")[0]}_renew_{data_length}.csv'
        """ 데이터프레임의 인덱스(index)에 해당하는 컬럼(column)을 일시(datetime)로 정의합니다. """
        # dataframe.info()
        dataframe.set_index('datetime', inplace=True)
        """ 생성된 데이터프레임(dataframe)을 csv 형태로 저장합니다. """
        dataframe.to_csv(f'{NEW_FILE_PATH}/{file_name}', index='datetime')
        print(f'"{file_name}" is saved.')
        count += 1

    print(f'총 {count}개의 작업을 완료하였습니다.')


if __name__ == '__main__':
    """ 지역명에 맞는 .csv 파일만 찾아서 가져옵니다. """
    file_list = getCSVFiles(region_name='전남')
    """ 불러온 파일들(list type)을 새로운 데이터프레임으로 정의하기 위한 함수를 실행합니다. """
    reconstructDataFrame(files=file_list)
