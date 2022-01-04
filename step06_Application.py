from datetime import datetime, timedelta
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from selenium import webdriver
import pandas as pd
import sys
from step05_prediction_KMC import predict


def setDriverOptions():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('lang=ko_KR')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('disable-gpu')
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    print(f'[{datetime.now().strftime("%y-%m-%d %H:%M:%S")}] - Success to set driver options.')
    return webdriver.Chrome('./chromedriver', options=options)


class Application(QWidget):
    def __init__(self):
        super().__init__()
        # Initialize class constants
        self.widget_options = {}
        self.region_item = {'서울특별시': ['서울'], '부산광역시': ['부산'], '대구광역시': ['대구'],
                            '인천광역시': ['강화', '백령도', '인천'], '광주광역시': ['광주'], '대전광역시': ['대전'],
                            '울산광역시': ['울산'], '경기도': ['동두천', '수원', '양평', '이천', '파주'],
                            '강원도': ['강릉', '대관령', '동해', '북강릉', '북춘천', '삼척', '속초', '영월', '원주', '인제',
                                    '정선', '철원', '춘천', '태백', '홍천'],
                            '충청북도': ['보은', '제천', '청주', '추풍령', '충주'],
                            '충청남도': ['금산', '보령', '부여', '서산', '천안', '홍성'],
                            '전라북도': ['고창', '군산', '남원', '부안', '순창', '임실', '장수', '전주', '정읍'],
                            '전라남도': ['강진군', '고흥', '광양', '목포', '무안', '보성', '순천', '여수', '영광', '완도',
                                     '장흥', '주안', '진도', '진도군', '해남', '흑산도'],
                            '경상북도': ['경주', '구미', '문경', '봉화', '상주', '안동', '영덕', '영주', '영천', '울릉도',
                                     '울진', '울진', '의성', '청송', '포항'],
                            '경상남도': ['거제', '거창', '김해', '남해', '밀양', '북창원', '산청', '양산', '의령', '진주',
                                     '창원', '통영', '함양', '합천'],
                            '제주특별자치시': ['고산', '서귀포', '성산-B', '성산-A', '성산포', '제주'],
                            '세종특별자치시': ['세종']}
        self.region_code = {'서울': (108, 'Seoul'), '부산': (159, 'Busan'), '대구': (143, 'Daegu'),
                            '강화': (201, 'Ganghwa'), '백령도': (102, 'Baengnyeongdo'), '인천': (112, 'Incheon'),
                            '광주': (156,'Gwangju'), '대전': (133, 'Daejeon'), '울산': (152, 'Ulsan'),
                            '동두천': (98, 'Dongducheon'), '수원': (119, 'Suwon'), '양평': (202, 'Yangpyeong'),
                            '이천': (203, 'Icheon'), '파주': (99, 'Paju'), '강릉': (105, 'Gangneung'),
                            '대관령': (100, 'Daegwallyeong'), '동해': (106, 'Donghae'), '북강릉': (104, 'Northgangneung'),
                            '북춘천': (93, 'Northchuncheon'), '삼척': (214, 'Samcheok'), '속초': (90, 'Sokcho'),
                            '영월': (121, 'Yeongwol'), '원주': (114, 'Wonju'), '인제': (211, 'Inje'),
                            '정선': (217, 'Jeongseon'), '철원': (95, 'Cheorwon'), '춘천': (101, 'Chuncheon'),
                            '태백': (216, 'Taebaek'), '홍천': (212, 'Hongcheon'), '보은': (226, 'Boeun'),
                            '제천': (221, 'Jecheon'), '청주': (131, 'Cheongju'), '추풍령': (135, 'Chupungryeong'),
                            '충주': (127, 'Chungju'), '금산': (238, 'Geumsan'), '보령': (235, 'Boryung'),
                            '부여': (236, 'Buyeo'), '서산': (129, 'Seosan'), '천안': (232, 'Cheonan'),
                            '홍성': (177, 'Hongseong'), '고창': (172, 'Gochang'), '군산': (140, 'Gunsan'),
                            '남원': (247, 'Namwon'), '부안': (243, 'Buan'), '순창': (254, 'Sunchang'),
                            '임실': (244, 'Imsil'), '장수': (248, 'Jangsoo'), '전주': (146, 'Jeonju'),
                            '정읍': (245, 'Jeongeub'), '강진': (259, 'Gangjin'), '고흥': (262, 'Goheung'),
                            '광양': (266, 'Gwangyang'), '목포': (165, 'Mokpo'), '무안': (164, 'Muan'),
                            '보성': (258, 'Bosung'), '순천': (174, 'Suncheon'), '여수': (168, 'Yeosu'),
                            '영광': (252, 'Yeonggwang'), '완도': (170, 'Wando'), '장흥': (260, 'Jangheung'),
                            '주암': (256, 'Juam'), '진도': (175, 'Jindo'), '진도군': (268, 'Jindogun'),
                            '해남': (261, 'Haenam'), '흑산도': (169, 'Heuksando'), '경주': (283, 'Gyeongju'),
                            '구미': (279, 'Gumi'), '문경': (273, 'Mungyeong'), '봉화': (271, 'Bonghwa'),
                            '상주': (137, 'Sangju'), '안동': (136, 'Andong'), '영덕': (277, 'Yeongdeok'),
                            '영주': (272, 'Yeongju'), '영천': (281, 'Yeongcheon'), '울릉도': (115, 'Ulleung'),
                            '울진': (130, 'Uljin'), '의성': (278, 'Uiseong'), '청송': (276, 'Cheongsong'),
                            '포항': (138, 'Pohang'), '거제': (294, 'Geoje'), '거창': (284, 'Geochang'),
                            '김해': (253, 'Gimhae'), '남해': (295, 'Namhae'), '밀양': (288, 'Milyang'),
                            '북창원': (255, 'Bukchangwon'), '산청': (289, 'Sancheong'), '양산': (257, 'Yangsan'),
                            '의령': (263, 'Uiryeong'), '진주': (192, 'Jinju'), '창원': (155, 'Changwon'),
                            '통영': (162, 'Tongyeong'), '함양': (264, 'Hamyang'), '합천': (285, 'Hapcheon'),
                            '고산': (185, 'Gosan'), '서귀포': (189, 'Seogwipo'), '성산-B': (188, 'Seongsan-B'),
                            '성산-A': (187, 'Seongsan-A'), '성산포': (265, 'Seongsanpo'), '제주': (184, 'Jeju'),
                            '세종': (239, 'Sejong')}
        self.driver = setDriverOptions()
        self.predict_dataframe = pd.DataFrame()
        self.predict_result = []
        self.thread_prediction_flag = False
        self.province = None

        # Initialize Q-Objects
        self.label = {'current_time': QLabel(self), 'region': QLabel(self), 'province': QLabel(self),
                      'element': QLabel(self), 'notice': QLabel(self), 'exit': QLabel(self),
                      'result_frame': QLabel(self), 'result_header': QLabel(self), 'result': QLabel(self)}
        self.button = {'region': QPushButton(self), 'province': QPushButton(self), 'element': QPushButton(self),
                       'exit': QPushButton(self)}
        self.combobox = {'region': QComboBox(self), 'province': QComboBox(self), 'element': QComboBox(self)}

        # Setup widget environments
        self.initializeWindow(name='Proto-type: Application(1.1)', rgb=(255, 255, 255), w=1080, h=860)
        self.initializeStaticObjects()

        # Triggers
        self.button['region'].clicked.connect(self.clickedRegionButton)
        self.button['province'].clicked.connect(self.clickedProvinceButton)
        self.button['element'].clicked.connect(self.clickedElementButton)
        self.button['exit'].clicked.connect(self.clickedExitButton)

        # Launched QThread
        self.timer = ThreadTimer(self)
        self.timer.start()
        self.notice_thread = ThreadGetData(self)
        self.notice_thread.start()

    def initializeWindow(self, **kwargs):
        """
        name: window 이름 설정  (default: Window) (type: str)
        rgb: window 배경 색상 설정    (default: (255, 255, 255)) (type: tuple)
        w: window 가로 길이 설정  (default: 640) (type: int)
        h: window 세로 길이 설정  (default: 480) (type: int)
        m: window 시작 좌표 설정  (default: False) (type: bool)
        mx: window 시작 x좌표 설정    (default: 0) (type: int)
        my: window 시작 y좌표 설정    (default: 0) (type: int)
        """
        try:
            self.widget_options['name'] = kwargs['name'] if 'name' in kwargs else 'Window'
            self.widget_options['rgb'] = kwargs['rgb'] if 'rgb' in kwargs else (255, 255, 255)
            self.widget_options['width'] = kwargs['w'] if 'w' in kwargs else 640
            self.widget_options['width'] = 640 if self.widget_options['width'] < 640 else self.widget_options['width']
            self.widget_options['height'] = kwargs['h'] if 'h' in kwargs else 480
            self.widget_options['height'] = 480 if self.widget_options['height'] < 480 else self.widget_options['height']
            self.widget_options['move'] = kwargs['m'] if 'm' in kwargs else False
            self.widget_options['move_x'] = kwargs['mx'] if 'mx' in kwargs else 0
            self.widget_options['move_y'] = kwargs['my'] if 'my' in kwargs else 0

            self.setWindowTitle(self.widget_options['name'])
            if self.widget_options['move']:
                self.move(self.widget_options['move_x'], self.widget_options['move_y'])
            self.resize(self.widget_options['width'], self.widget_options['height'])
            # Window 크기 조절을 할 수 없도록 제한합니다.
            self.setFixedSize(self.widget_options['width'], self.widget_options['height'])
            # 애플리케이션의 아이콘을 설정합니다.
            self.setWindowIcon(QtGui.QIcon('./app_icon/main.png'))
            # 애플리케이션의 배경화면을 구성합니다.
            palette = QtGui.QPalette()
            palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap('./app_icon/background_1.jpeg')))
            self.setPalette(palette)
        except Exception as E:
            print(f'[{datetime.now().strftime("%y-%m-%d %H:%M:%S")}] - Unknown error occurred in "{sys._getframe().f_code.co_name}()"\n\t\t\t\t\t  {E}')
            self.driver.close()
            self.close()
        else:
            print(f'[{datetime.now().strftime("%y-%m-%d %H:%M:%S")}] - Success to initialize widget settings.')

    def initializeStaticObjects(self):
        self.label['current_time'].setGeometry(self.widget_options['width'] - 200, 10, 200, 20)
        self.label['current_time'].setFont(QtGui.QFont('Ariel', 12, QtGui.QFont.Bold))
        self.label['current_time'].setText('2022-01-03 10:30:00')
        self.label['current_time'].setAlignment(Qt.AlignCenter)
        self.label['current_time'].setStyleSheet('color: rgb(255, 255, 255)')

        self.combobox['region'].setGeometry(50, 150, 250, 50)
        self.combobox['region'].setFont(QtGui.QFont('Ariel', 15, QtGui.QFont.Bold))
        self.button['region'].setGeometry(310, 155, 50, 40)
        self.button['region'].setStyleSheet('background-color: rgb(255, 200, 0)')
        self.button['region'].setFont(QtGui.QFont('Ariel', 12, QtGui.QFont.Bold))
        self.button['region'].setText('선택')

        self.combobox['province'].setGeometry(390, 150, 250, 50)
        self.combobox['province'].setFont(QtGui.QFont('Ariel', 12, QtGui.QFont.Bold))
        self.button['province'].setGeometry(650, 155, 50, 40)
        self.button['province'].setEnabled(False)
        self.button['province'].setStyleSheet('color: rgb(0, 0, 0); background-color: rgb(120, 120, 120)')
        self.button['province'].setFont(QtGui.QFont('Ariel', 12, QtGui.QFont.Bold))
        self.button['province'].setText('선택')

        self.combobox['element'].setGeometry(730, 150, 250, 50)
        self.combobox['element'].setFont(QtGui.QFont('Ariel', 12, QtGui.QFont.Bold))
        self.button['element'].setGeometry(990, 155, 50, 40)
        self.button['element'].setStyleSheet('color: rgb(0, 0, 0); background-color: rgb(120, 120, 120)')
        self.button['element'].setFont(QtGui.QFont('Ariel', 12, QtGui.QFont.Bold))
        self.button['element'].setText('선택')
        self.button['element'].setEnabled(False)

        self.label['notice'].setGeometry((self.widget_options['width'] / 2) - 200, 220, 400, 30)
        self.label['notice'].setFont(QtGui.QFont('Ariel', 12, QtGui.QFont.Bold))
        self.label['notice'].setAlignment(Qt.AlignCenter)
        self.label['notice'].setStyleSheet('color: rgb(255, 255, 255)')

        # 애플리케이션 하단 아이콘 및 라벨
        self.button['exit'].setGeometry(self.widget_options['width'] - 80, self.widget_options['height'] - 80, 60, 60)
        self.button['exit'].setStyleSheet('background: rgba(255, 255, 255, 0.8)')
        self.button['exit'].setIcon(QtGui.QIcon('./app_icon/exit.png'))
        self.button['exit'].setIconSize(QSize(30, 30))
        self.button['exit'].setToolTip('애플리케이션을 종료합니다.')
        self.label['exit'].setText('EXIT')
        self.label['exit'].setGeometry(self.widget_options['width'] - 80, self.widget_options['height'] - 125, 60, 60)
        self.label['exit'].setStyleSheet('color: rgb(255, 255, 255)')
        self.label['exit'].setAlignment(Qt.AlignCenter)
        self.label['exit'].setFont(QtGui.QFont('Ariel', 10, QtGui.QFont.Bold))

        for region in self.region_item:
            self.combobox['region'].addItem(region)

        # 결과 라벨
        self.label['result_frame'].setGeometry(50, 250, self.widget_options['width'] - 100, 200)
        self.label['result_frame'].setStyleSheet('border-radius: 20px; border: 3px; border-style: solid; border-color: rgb(255, 255, 255)')
        self.label['result_header'].setGeometry((self.widget_options['width'] / 2) - 200, 270, 400, 30)
        self.label['result_header'].setStyleSheet('color: rgb(255, 255, 255)')
        self.label['result_header'].setFont(QtGui.QFont('Ariel', 15, QtGui.QFont.Bold))
        self.label['result_header'].setAlignment(Qt.AlignCenter)
        self.label['result'].setGeometry((self.widget_options['width'] / 2) - 200, 325, 400, 50)
        self.label['result'].setAlignment(Qt.AlignCenter)
        self.label['result'].setFont(QtGui.QFont('Ariel', 50, QtGui.QFont.Bold))

    # Not usage
    def selectRegion(self):
        # print(f'선택 완료 -> {self.combobox["region"].currentText()}')
        self.combobox['province'].clear()
        for province in self.region_item[self.combobox['region'].currentText()]:
            self.combobox['province'].addItem(province)
        print('---------')
            # self.combobox['province'].addItem(province)

    def clickedRegionButton(self):
        self.combobox['province'].clear()
        self.combobox['element'].clear()
        self.combobox['province'].setEnabled(True)
        self.button['province'].setStyleSheet('color: rgb(0, 0, 0); background-color: rgb(255, 200, 0)')
        self.button['province'].setEnabled(True)
        self.button['element'].setStyleSheet('color: rgb(0, 0, 0); background-color: rgb(120, 120, 120)')
        self.button['element'].setEnabled(False)
        for province in self.region_item[self.combobox['region'].currentText()]:
            self.combobox['province'].addItem(province)

    def clickedProvinceButton(self):
        self.combobox['element'].clear()
        self.combobox['element'].addItem('평균기온(℃)')
        self.combobox['element'].addItem('최저기온(℃)')
        self.combobox['element'].addItem('최고기온(℃)')
        self.combobox['element'].setEnabled(True)
        self.button['element'].setStyleSheet('color: rgb(0, 0, 0); background-color: rgb(255, 200, 0)')
        self.button['element'].setEnabled(True)

    def clickedElementButton(self):
        self.label['notice'].setVisible(True)
        self.button['region'].setStyleSheet('color: rgb(0, 0, 0); background-color: rgb(120, 120, 120)')
        self.button['region'].setEnabled(False)
        self.combobox['region'].setEnabled(False)
        self.button['province'].setStyleSheet('color: rgb(0, 0, 0); background-color: rgb(120, 120, 120)')
        self.button['province'].setEnabled(False)
        self.combobox['province'].setEnabled(False)
        self.button['element'].setStyleSheet('color: rgb(0, 0, 0); background-color: rgb(120, 120, 120)')
        self.button['element'].setEnabled(False)
        self.combobox['element'].setEnabled(False)
        self.label['notice'].setText(f'"{self.combobox["province"].currentText()}"지역 데이터 수집 중입니다.. (1 / 3)')

        self.province = self.combobox['province'].currentText()
        # 데이터 수집을 위한 기준시간 설정
        current_time = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        before_time = (datetime.now() - timedelta(days=31)).strftime('%Y-%m-%d')
        base_time = datetime.now() - timedelta(days=31)

        # 현재시간 기준, 지난 달 데이터를 수집하여 데이터프레임 생성
        previous_df = pd.DataFrame()
        date_time, avg_tmp, min_tmp, max_tmp = [], [], [], []
        url = f'https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-day.do?stn={self.region_code[self.province][0]}&yy={before_time.split("-")[0]}&mm={before_time.split("-")[1]}&obs=1'
        self.driver.get(url)
        try:
            for i in range(1, 12, 2):
                for j in range(1, 8):
                    x_path = f'/html/body/div[2]/section/div/div[2]/div[2]/div[3]/div/table/tbody/tr[{i}]/td[{j}]'
                    title = self.driver.find_element_by_xpath(x_path).text
                    # 가져온 타이틀의 길이가 1(공백)인 경우 다음 회차로 넘어간다.
                    if len(title) == 1:
                        continue
                    # 가져온 타이틀의 길이가 있는 경우(날짜가 포함되어 있음) 이하 스크립트를 실행한다.
                    else:
                        title = title.replace('일', '')
                        if int(before_time.split('-')[2]) < int(title):
                            base_time += timedelta(days=1)
                            x_path = f'/html/body/div[2]/section/div/div[2]/div[2]/div[3]/div/table/tbody/tr[{i + 1}]/td[{j}]'
                            content = self.driver.find_element_by_xpath(x_path).text
                            # 데이터 추가
                            date_time.append(base_time.strftime('%Y-%m-%d'))
                            avg_tmp.append(content.split('\n')[0].split(':')[-1].replace('℃', ''))
                            min_tmp.append(content.split('\n')[1].split(':')[-1].replace('℃', ''))
                            max_tmp.append(content.split('\n')[2].split(':')[-1].replace('℃', ''))


        except Exception as E:
            pass

        previous_df['datetime'] = date_time
        previous_df['avg_tmp'] = avg_tmp
        previous_df['min_tmp'] = min_tmp
        previous_df['max_tmp'] = max_tmp
        # print('---------')

        # 현재시간 기준, 오늘을 제외한 이전 일자 까지의 데이터를 수집하여 데이터프레임 생성
        current_df = pd.DataFrame()
        date_time, avg_tmp, min_tmp, max_tmp = [], [], [], []
        url = f'https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-day.do?stn={self.region_code[self.province][0]}&yy={current_time.split("-")[0]}&mm={current_time.split("-")[1]}&obs=1'
        self.driver.get(url)
        try:
            for i in range(1, 12, 2):
                for j in range(1, 8):
                    x_path = f'/html/body/div[2]/section/div/div[2]/div[2]/div[3]/div/table/tbody/tr[{i}]/td[{j}]'
                    title = self.driver.find_element_by_xpath(x_path).text
                    if len(title) == 1:
                        continue
                    else:
                        title = title.split('일')[0]
                        if int(current_time.split('-')[2]) >= int(title):
                            base_time += timedelta(days=1)
                            x_path = f'/html/body/div[2]/section/div/div[2]/div[2]/div[3]/div/table/tbody/tr[{i + 1}]/td[{j}]'
                            content = self.driver.find_element_by_xpath(x_path).text
                            # 데이터 추가
                            date_time.append(base_time.strftime('%Y-%m-%d'))
                            avg_tmp.append(content.split('\n')[0].split(':')[-1].replace('℃', ''))
                            min_tmp.append(content.split('\n')[1].split(':')[-1].replace('℃', ''))
                            max_tmp.append(content.split('\n')[2].split(':')[-1].replace('℃', ''))

        except Exception as E:
            pass

        current_df['datetime'] = date_time
        current_df['avg_tmp'] = avg_tmp
        current_df['min_tmp'] = min_tmp
        current_df['max_tmp'] = max_tmp
        # print(current_df.tail(3))

        # 두 개의 데이터프레임 합치기
        self.predict_dataframe = pd.concat([previous_df, current_df], ignore_index=True)
        self.predict_dataframe.set_index('datetime', inplace=True)

        self.thread_prediction_flag = True
        if self.combobox['element'].currentText() == '평균기온(℃)':
            self.label['result_frame'].setStyleSheet('border-radius: 20px; border: 3px; border-style: solid; border-color: rgb(51, 255, 51)')
            text = ''.join([self.combobox['province'].currentText(), ' 지역의 예상 평균기온(℃)'])
            self.label['result_header'].setText(text)
        elif self.combobox['element'].currentText() == '최저기온(℃)':
            self.label['result_frame'].setStyleSheet('border-radius: 20px; border: 3px; border-style: solid; border-color: rgb(0, 128, 255)')
            text = ''.join([self.combobox['province'].currentText(), ' 지역의 예상 최저기온(℃)'])
            self.label['result_header'].setText(text)
        else:
            self.label['result_frame'].setStyleSheet('border-radius: 20px; border: 3px; border-style: solid; border-color: rgb(255, 51, 51)')
            text = ''.join([self.combobox['province'].currentText(), ' 지역의 예상 최고기온(℃)'])
            self.label['result_header'].setText(text)

    def clickedExitButton(self):
        print(f'[{datetime.now().strftime("%y-%m-%d %H:%M:%S")}] - Exit.')
        self.driver.close()
        self.close()


class ThreadTimer(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        while True:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.parent.label['current_time'].setText(current_time)
            self.sleep(1)


class ThreadGetData(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        while True:
            if self.parent.thread_prediction_flag:
                self.parent.thread_prediction_flag = False
                self.parent.label['notice'].setText(f'"{self.parent.combobox["province"].currentText()}"지역 데이터 예측 중입니다.. (2 / 3)')
                self.parent.predict_result = predict(province=self.parent.region_code[self.parent.province][1], data=self.parent.predict_dataframe)
                self.parent.label['notice'].setText(f'"{self.parent.combobox["province"].currentText()}"지역 예측 결과를 그리는 중입니다.. (3 / 3)')
                self.sleep(1)
                self.parent.label['notice'].setVisible(False)
                if self.parent.combobox['element'].currentText() == '평균기온(℃)':
                    try:
                        data = self.parent.predict_result[0][0]
                        self.parent.label['result'].setText(str(round(data, 1)))
                        if float(data) > float(self.parent.predict_dataframe.iloc[-1, 0]):
                            self.parent.label['result'].setStyleSheet('color: rgb(255, 51, 51)')
                        elif float(data) < float(self.parent.predict_dataframe.iloc[-1, 0]):
                            self.parent.label['result'].setStyleSheet('color: rgb(0, 128, 255)')
                        else:
                            self.parent.label['result'].setStyleSheet('color: rgb(255, 255, 255)')
                    except Exception as E:
                        print(f'[{datetime.now().strftime("%y-%m-%d %H:%M:%S")}] - Unknown error occurred in "{sys._getframe().f_code.co_name}()"\n\t\t\t\t\t  {E}')
                        self.parent.label['result'].setText('NaN')
                    else:
                        print(f'[{datetime.now().strftime("%y-%m-%d %H:%M:%S")}] - 평균기온: {data:.1f}')
                elif self.parent.combobox['element'].currentText() == '최저기온(℃)':
                    try:
                        data = self.parent.predict_result[0][1]
                        self.parent.label['result'].setText(str(round(data, 1)))
                        if float(data) > float(self.parent.predict_dataframe.iloc[-1, 1]):
                            self.parent.label['result'].setStyleSheet('color: rgb(255, 51, 51)')
                        elif float(data) < float(self.parent.predict_dataframe.iloc[-1, 1]):
                            self.parent.label['result'].setStyleSheet('color: rgb(0, 128, 255)')
                        else:
                            self.parent.label['result'].setStyleSheet('color: rgb(255, 255, 255)')
                    except Exception as E:
                        print(f'[{datetime.now().strftime("%y-%m-%d %H:%M:%S")}] - Unknown error occurred in "{sys._getframe().f_code.co_name}()"\n\t\t\t\t\t  {E}')
                        self.parent.label['result'].setText('NaN')
                    else:
                        print(f'[{datetime.now().strftime("%y-%m-%d %H:%M:%S")}] - 최저기온: {data:.1f}')
                else:
                    try:
                        data = self.parent.predict_result[0][2]
                        self.parent.label['result'].setText(str(round(data, 1)))
                        if float(data) > float(self.parent.predict_dataframe.iloc[-1, 2]):
                            self.parent.label['result'].setStyleSheet('color: rgb(255, 51, 51)')
                        elif float(data) < float(self.parent.predict_dataframe.iloc[-1, 2]):
                            self.parent.label['result'].setStyleSheet('color: rgb(0, 128, 255)')
                        else:
                            self.parent.label['result'].setStyleSheet('color: rgb(255, 255, 255)')
                    except Exception as E:
                        print(f'[{datetime.now().strftime("%y-%m-%d %H:%M:%S")}] - Unknown error occurred in "{sys._getframe().f_code.co_name}()"\n\t\t\t\t\t  {E}')
                        self.parent.label['result'].setText('NaN')
                    else:
                        print(f'[{datetime.now().strftime("%y-%m-%d %H:%M:%S")}] - 최고기온: {data:.1f}')
                print(self.parent.predict_dataframe.iloc[-1, 0])
                print(self.parent.predict_dataframe.iloc[-1, 1])
                print(self.parent.predict_dataframe.iloc[-1, 2])

                # 콤보박스 초기화

                self.parent.combobox['region'].setEnabled(True)
                self.parent.combobox['province'].setEnabled(True)
                self.parent.combobox['element'].setEnabled(True)
                self.parent.combobox['province'].clear()
                self.parent.combobox['element'].clear()
                self.parent.combobox['province'].setEnabled(False)
                self.parent.combobox['element'].setEnabled(False)
                # 버튼 활성화
                self.parent.button['region'].setStyleSheet('color: rgb(0, 0, 0); background-color: rgb(255, 200, 0)')
                self.parent.button['region'].setEnabled(True)
                # self.parent.button['province'].setStyleSheet('color: rgb(0, 0, 0); background-color: rgb(255, 200, 0)')
                # self.parent.button['province'].setEnabled(True)
                # self.parent.button['element'].setStyleSheet('color: rgb(0, 0, 0); background-color: rgb(255, 200, 0)')
                # self.parent.button['element'].setEnabled(True)

            self.sleep(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Application()
    mainWindow.show()
    sys.exit(app.exec_())
