# coding=utf8
# REST API 호출에 필요한 라이브러리
import requests
import json

# [내 애플리케이션] > [앱 키] 에서 확인한 REST API 키 값 입력
REST_API_KEY = ''

# KoGPT API 호출을 위한 메서드 선언
# 각 파라미터 기본값으로 설정
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

# KoGPT에게 전달할 명령어 구성
prompt='''카카오의 임팩트 커머스 카카오메이커스와 카카오브레인이 '세계 동물의 날'을 맞아 멸종 위기 동물 보호에 힘을 보탠다. 

카카오메이커스와 카카오브레인은 4일 세계 동물의 날을 맞아, 카카오브레인의 AI 아티스트 '칼로' 와 현대미술가 고상우 작가가 협업한 제품을 오는 12일까지 카카오메이커스에서 단독 판매한다고 밝혔다. 판매 수익금 전액은 WWF(세계자연기금)에 기부할 예정이다. 

이번 프로젝트에 참여한 AI 아티스트 '칼로'는 'minDALL-E', 'RQ-Transformer' 등 카카오브레인의 초거대 이미지 생성 AI 모델을 발전시켜 하나의 페르소나로 재탄생한 AI 아티스트다. 1.8억 장 규모의 텍스트-이미지 데이터셋을 학습해 이해한 문맥을 바탕으로 다양한 화풍과 스타일로 이미지를 생성할 수 있다. 올해 6월에는 고상우 작가와의 공동 작업으로 생성한 1,000개의 호랑이 이미지를 조합한 디지털 작품으로 전시회를 진행한 바 있다. 

이번 프로젝트를 통해 선보이는 제품은 맨투맨과 머그컵이다. '칼로'가 생성한 호랑이 그림과 푸른색 사진 예술의 선구자인 고상우 작가 특유의 드로잉이 조화롭게 어우러져 완성된 500점의 호랑이 그림 모자이크 'Blue Tiger'가 새겨져 있다. 판매 수익금 전액은 WWF(세계자연기금)에 기부됨과 동시에, 낭비 없는 생산을 위해 주문 수량만큼 제품을 생산하는 카카오메이커스의 환경친화적 주문제작 방식(POD 생산)을 도입했다. 

카카오브레인 대표는 "AI 아티스트 칼로가 생성한 예술 작품으로 멸종 위기 동물 보호 활동에 동참하게 되어 기쁘다"며, "앞으로도 우리의 AI 기술을 통해 사회에 환원할 수 있는 의미 있는 프로젝트에 지속 참여하겠다"며 포부를 전했다. 

카카오 메이커스 실장은 "지난 8월 고양이의 날을 기념한 제품을 기획/판매해 기부한데 이어 사회의 다양한 구성원을 존중하고 배려하는 프로젝트를 이어가고 있다"며 "더 나은 세상을 만들기 위한 이용자들의 관심을 확인하고 있으며, 앞으로도 임팩트 커머스로서 다양한 가치를 담은 메이커스만의 제품을 선보일 것" 이라고 밝혔다.

한줄 요약:'''
response = kogpt_api(prompt, max_tokens=128, top_p=0.7)

# 파라미터를 전달해 kogpt_api()메서드 호출
response = kogpt_api(
    prompt = prompt,
    max_tokens = 100,
    temperature = 1.0,
    top_p = 1.0,
    n = 3
)

print(response)
#print(response['generations'][1]['text'])