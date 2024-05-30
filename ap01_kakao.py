#660cc1204baad91f47bd93694cfdde5b
import requests
import json

url = "https://dapi.kakao.com/v2/search/web"
#url_get = "https://dapi.kakao.com/v2/search/web?query=인공지능"
rest_api_key = ''
hearders = {'Authorization': f'KakaoAK {rest_api_key}'}
params = {'query':'인공지능', 'page':1, 'size':50, 'sort':'accuracy'}
res = requests.get(url, params=params, headers=hearders)  # API를 사용했기에 json 형태로 응답이 온다.
contents = res.json()
print(len(contents['documents']))

for content in range(len(contents['documents'])):
    print(contents['documents'][content]['contents'],'\n')