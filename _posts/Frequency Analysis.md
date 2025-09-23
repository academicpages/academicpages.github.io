---
title: ' Frequency Analysis'
date: 2025-09-23
permalink: /Other_Study/
tags:
  - SWUFOCE
  - SuNiNaTaS_26
  - Forensics
  - Crypto
---
## Frequency Analysis(빈도분석)
특정 변수의 데이터 값들이 얼마나 자주 나타나는지와 전체에서 차지하는 비율을 파악하는 통계 분석 방법.   
특히, 암호학에서의 빈도분석은 평문과 암호문에 사용되는 문자 또는 문자열의 출현빈도를 단서로 이용하는 암호 해독을 의미함.

주로 문자 빈도 파악, 언어별 빈도 비교, 대응 관계 추론 등의 방식으로 접근할 수 있음.

## 사용되는 툴
주로 사용되는 툴로는 quip quip이 있음.   

## 실습
어떤 실습을 할지 고민하다가 직접 암호문을 만들고, 위에서 소개한 툴로 다시 복호화 하는 실습을 해보려고 한다.  
우선, 파이썬을 이용해 평문을 입력 받고 단일 암호화 하는 코드를 작성한다.  
```import random

# 알파벳 키와 값 생성
key = [chr(i) for i in range(ord('a'), ord('z') + 1)]
value = key.copy()
random.shuffle(value)

# 암호화용 딕셔너리 생성
E = {k: v for k, v in zip(key, value)}    

def Encryption(text):
    table = text.maketrans(E)
    return text.translate(table)  

plaintext = input("평문 : ").lower()
ciphertext = Encryption(plaintext)
print("암호문:", ciphertext)'''  

코드는 위와 같다.
내가 암호화하고자한 평문은  아래와 같다.
'''Hello, I'm ojeon, Department of Information Protection, Seoul Women's University.  
Nice to meet you. I'm currently studying forensics with interest.  
Among forensics, I'm especially interested in mobile forensics.  
If you'd like to talk with me, please contact me through the email linked to my blog.  
I'll always look forward to it!'''  

위에서 소개한 코드로 해당 평문을 돌려 보면 아래와 같은 결과를 확인할 수 있다.  
<img width="1168" height="323" alt="image" src="https://github.com/user-attachments/assets/07c030c2-068d-4cd3-8180-2eef246126cd" />
위의 암호문을 quip quip을 이용해 복호화하면 아래와 같이 복호화 됨을 확인할 수 있다.
<img width="1117" height="238" alt="image" src="https://github.com/user-attachments/assets/5a74e760-20d3-47d3-932b-88e1334f0498" />



------
{% include base_path %}

{% for post in site.Other_Study reversed %}
  {% include archive-single.html %}
{% endfor %}
