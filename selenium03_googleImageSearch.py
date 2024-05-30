import pandas as pd
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # 태그 검색용 라이브러리
from selenium.webdriver.common.keys import Keys   # 사용자 조작 액션을 전달하기 위해 필요한 라이브러리
import openpyxl
import time
import urllib.request
import os   # 폴더, 파일 관리 라이브러리


opt = Options()  # 크롬드라이버를 제어하기 위한 옵션 설정
opt.add_experimental_option('detach', True)  # 브라우저 꺼짐 방지
#opt.add_argument('headless')  # 브라우저 띄우지 않고 진행

# 이미지 저장할 폴더 생성
save_dir = "googleImgs"
os.makedirs(save_dir, exist_ok=True)   # 폴더 생성. 이미 존재하면 무시

searchKey = input('이미지 검색 : ')

url = "https://www.google.com"
# 크롬 드라이브 개체 생성
driver = Chrome(options=opt)  # 옵션 설정.
driver.get(url)

# 검색어 입력
searchBox = driver.find_element(By.ID, 'APjFqb')
searchBox.send_keys(f'{searchKey} 일러스트 무료 png')
searchBox.submit()
time.sleep(1)

driver.find_element(By.LINK_TEXT, '이미지').click()
time.sleep(1)


# 이미지 검색 개수 및 다운로드
links = []

images = driver.find_elements(By.CSS_SELECTOR, 'g-img.mNsIhb>img.YQ4gaf')

# print(images[0].get_attribute('src'))
# print(len(images))

for img in images:
    if img.get_attribute('src') != None:
        links.append(img.get_attribute('src'))

print("이미지 갯수", len(links))
time.sleep(2)

for no, img in enumerate(links):
    urllib.request.urlretrieve(img, f'./{save_dir}/{searchKey}_{str(no)}.jpg')
    time.sleep(0.3)

driver.close()