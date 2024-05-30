import pandas as pd
from bs4 import BeautifulSoup
import requests
import lxml
import json

REST_API_KEY = ''
def kogpt_api(prompt, max_tokens = 1, temperature = 1.0, top_p = 1.0, n = 1):
    r = requests.post(
        'https://api.kakaobrain.com/v1/inference/kogpt/generation',
        json = {
            'prompt': prompt,
            'max_tokens': max_tokens,
            'temperature': temperature,
            'top_p': top_p,
            'n': n
        },
        headers = {
            'Authorization': 'KakaoAK ' + REST_API_KEY,
            'Content-Type': 'application/json'
        }
    )
    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    return response




headers = {'User-Agent': 'Mozilla/5.0'}
categoris = ['259', '268', '261', '771', '263', '260']
news_list = []

for cate in categoris:
    url = f'https://news.naver.com/breakingnews/section/101/{cate}'
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')

    # 뉴스 제목과 링크 가져오기
    tag3 = soup.find('ul', {'class':'sa_list'}).find_all('li', limit=2)
    for li in tag3:
        news_info = {"title":li.find('strong', 'sa_text_strong').text,
                     "link":li.find('a')['href'],
                     }
        news_list.append(news_info)
# 뉴스 상세 페이지 이동
for news in news_list:
    d_url = news['link']
    d_html = requests.get(d_url, headers=headers)
    d_soup = BeautifulSoup(d_html.text, 'lxml')
    print(f'{d_url}')

    body = d_soup.find('article', {'class':'go_trans _article_content'})
    news_contnets = body.text.replace('\n', '').strip()
    news['news_contnets'] = news_contnets
#    print(news_list)
df = pd.DataFrame(news_list)

# KorGpt에게 전달할 명령어
for i in range(len(df['news_contnets'])):
    try:
        prompt = df['news_contnets'].iloc[i]    # i번째 행의 df['news_contnets'] 텍스트 데이터 가져오기
        print(f"기사내용 - {prompt}")
        response = kogpt_api(prompt, max_tokens=200, top_p=0.7)
        summ = response['generations'][0]['text']

        if summ == "":
            summ = "요약 내용 없음"
        else:
            print(summ)

        print(f"요약내용 - {summ}")
        df.at[i,'summary'] = summ
    except:
        pass
print(df)