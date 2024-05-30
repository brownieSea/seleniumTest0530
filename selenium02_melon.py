#from selenium import webdriver
import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # 태그 검색용 라이브러리
from selenium.webdriver.common.keys import Keys   # 사용자 조작 액션을 전달하기 위해 필요한 라이브러리
import openpyxl
import time

opt = Options()  # 크롬드라이버를 제어하기 위한 옵션 설정
opt.add_experimental_option('detach', True)  # 브라우저 꺼짐 방지
#opt.add_argument('headless')  # 브라우저 띄우지 않고 진행

# 검색어 input
singer = input("가수명 : ")


url = "https://www.melon.com/index.htm"
# 크롬 드라이브 개체 생성
driver = Chrome(options=opt)  # 옵션 설정.
driver.get(url)

# 검색어 입력
searchBox = driver.find_element(By.ID, 'top_search')
searchBox.send_keys(f'{singer}')
searchBox.send_keys(Keys.RETURN)
time.sleep(2)

# 앨범 탭 이동
driver.find_element(By.XPATH, '//*[@id="divCollection"]/ul/li[4]/a').click()
time.sleep(0.5)

# 앨범 클릭
driver.find_element(By.CLASS_NAME, 'thumb').click()
time.sleep(0.3)

# 변수 선언
songTitles = []
lyrics = []
song_data = pd.DataFrame()

# 앨범의 곡수 가져오기
albumLength = driver.find_elements(By.TAG_NAME, 'tr')

for i in range(1, len(albumLength)+1):
    try:
        # 노래 제목 저장
        xp_t = f'//*[@id="frm"]/div/table/tbody/tr[{i}]/td[4]/div/div/div[1]/span/a'
        song_title = driver.find_element(By.XPATH, xp_t).text
        songTitles.append(song_title)
        # 노래 가사 클릭 / 가져오기
        xp_s = f'//*[@id="frm"]/div/table/tbody/tr[{i}]/td[3]/div/a'
        driver.find_element(By.XPATH, xp_s).click()
        time.sleep(1)

        # 가사가 없을 때 처리
        try:
            lyricsBox = driver.find_element(By.ID, 'd_video_summary')
            lyric = lyricsBox.text.replace('\n', ' / ') if lyricsBox else "가사 준비중"
        except:
            lyric = "가사 준비중"

        lyrics.append(lyric)
        driver.back()
        time.sleep(1)
    except Exception as e:
        driver.back()
        time.sleep(0.5)

song_data['노래제목'] = songTitles
song_data['노래가사'] = lyrics

#print(song_data)
song_data.to_excel(f'{singer}_앨범.xlsx', engine='openpyxl')

driver.close()