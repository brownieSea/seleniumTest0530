#from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # 태그 검색용 라이브러리
from selenium.webdriver.common.keys import Keys   # 사용자 조작 액션을 전달하기 위해 필요한 라이브러리
import time

opt = Options()  # 크롬드라이버를 제어하기 위한 옵션 설정
#opt.add_experimental_option('detach', True)  # 브라우저 꺼짐 방지
opt.add_argument('headless')  # 브라우저 띄우지 않고 진행

url = "https://www.naver.com"
# 크롬 드라이브 개체 생성
driver = Chrome(options=opt)  # 옵션 설정.
driver.get(url)

# 검색어 입력
searchBox = driver.find_element(By.ID, 'query')
searchBox.send_keys('인공지능')
searchBox.send_keys(Keys.RETURN)
time.sleep(1)

# 뉴스탭 클릭
#searchBox.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[3]/a').click()
driver.find_element(By.LINK_TEXT, '뉴스').click()
time.sleep(1)

# 화면 스크롤링
scroll = driver.find_element(By.TAG_NAME, 'body')
#scroll = driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
for i in range(40):
    scroll.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)

# 뉴스 제목 텍스트 추출
news_titles = driver.find_elements(By.CLASS_NAME, 'news_tit')
count = 1
for title in news_titles:
    print(f"저장중 : {count}")
    # print(f"{count}. {title.text}")
    with open('goolgleNews.csv', 'a', encoding='utf-8') as f:  # 'w' 새로 쓰기, 'a' 기존 파일에 추가하기
        f.write(f"{str(count)}. {title.text}\n")
    count +=1

driver.quit()
