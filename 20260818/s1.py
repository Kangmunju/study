# -----------------------------------------------------
# import란 무엇인가
# --------------------------------------------------------

# '이미 누군가 만들어 놓은 코드를 가져다 쓰겠다'는 의미

# 필요한 이유
# 프로그래밍에는 '바퀴를 다시 발명하지 말라'는 원칙이 있음

# 제곱근 계산, 날짜 처리, 무작위 숫자 뽑기 등
# 이미 전 세계 개발자들이 만들어 둔 것이 있음
# 우리는 그것을 그대로 가져다 쓸 것

# 가져올 수 있는 코드는 3 종류
# 1) 표준 라이브러리
#    - 파이썬을 설치하면 자동으로 딸려 오는 코드
#    - math, random, csv, datetime, os, pathlib 등
#    - import를 작성해두면 바로 사용 가능
# 2) 외부 패키지
#    - 따로 설치 필요
#    - pandas, numpy, matplotlib, requests 등
#    - pip install로 설치한 뒤 import
# 3) 내가 만든 파일
#    - 같은 폴더에 있는 내 .py 파일   ex. my_tools.py
#    - 파일 이름으로 import
# 세 가지 모두 import 하는 방법 동일

# 만약 math 없이 제곱근을 직접 구하려면 복잡한 계산식이 필요
# 하지만 import 한 줄이면 간단하게 구현 가능

# --------------------------------------------------------

# 방법 1) 통째로 가져오기
# import 모듈이름
# 쓸 때는 항상 '모듈이름.함수이름'으로 작성
import math
print("16의 제곱근 : ", math.sqrt(16))
print("원주율 : ", round(math.pi, 4))
print("2의 10제곱 : ", math.pow(2, 10))
print("올림 : ", math.ceil(3.2))
print("내림 : ", math.floor(3.8))

# --------------------------------------------------------

# 방법 2) 별칭 붙이기
# import 모듈이름 as 짧은 이름
# 모듈 이름이 길 때 짧게 줄여 쓰기 가능
import math as m
print(m.sqrt(16))

# --------------------------------------------------------

# 방법 3) 특정 함수만 집어 오기
# from 모듈이름 import 함수이름
# 모듈 이름 없이 바로 쓸 수 있습니다.
from math import sqrt, pi
print(sqrt(36))
print(round(pi, 4))








# --------------------------------------------------------
# 3가지 방법 중 사용해야 할 것
# --------------------------------------------------------

# import math -> math.sqrt()    안전/명확/기본
# import pandas as pd -> pd.read_csv    이름이 긴 경우
# import from math import sqrt -> sqrt()    짧지만 위험

# [from . . . import]가 위험한 이유
# from math import pow
# pow = 100   <- 실수로 같은 이름의 변수를 만들 가능성 존재
# pow(2, 3)   <- Error! 숫자를 함수처럼 부르게 됨

# 모듈 이름을 붙여 쓰면 (math.pow)와 같은 충돌 발생하지 않음
# 코드를 읽을 때에도 차이가 남
# sqrt(16)    <- 어디서 온 함수인지 파악 불가
# math.sqrt(16)   <- math에서 온 것임을 파악 가능

# [별칭(as)을 사용하는 경우]
# 데이터 분석에서는 별칭이 사실상 표준!
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# 전 세계가 쓰는 관례이므로 다르게 작성하지 말 것!
# 모두가 알고 있어야 소통이 가능

import random as rd
print("주사위 굴리기 : ", rd.randint(1, 6)) 
print("무작위 선택 : ", rd.choice(["김밥", "라면", "돈가스"]))
my_list = [1, 2, 3, 4, 5]
rd.shuffle(my_list)
print("섞은 리스트 : ", my_list)
print("중복 없이 3개 : ", rd.sample(range(1, 46), 3))






# --------------------------------------------------------
# import를 사용하게 되면 정확히 어떤 일이 일어나는가
# --------------------------------------------------------

# import my_tools를 실행한 경우 파이썬의 동작
# 1) my_tools.py 파일 찾기
#    찾는 순서 : 현재 폴더 -> 파이썬 설치 폴더 -> 패키지 폴더
# 2) 그 파일을 위에서 아래로 한 번 실행
#    def문들이 실행되면서 함수가 메모리에 등록
# 3) my_tools 라는 이름으로 사용할 수 있게 됨

# 가장 중요한 순서는 2) 그 '파일을 위에서 아래로 한 번 실행'
# 따라서 my_tools.py 안에 print문이 있으면 실행
# 추후 이 문제를 어떻게 해결해야하는 지 학습






# --------------------------------------------------------
# 설치 없이 바로 쓰는 것들
# --------------------------------------------------------

import datetime
import os
today = datetime.date.today()
now = datetime.datetime.now()
print("날짜와 시간")
print("오늘 날짜 : ", today)
print("현재 시각 : ", now.strftime("%H시 %M분"))
print("현재 시각 : ", now)

# 요일 구하기 (0 = 월요일, 6 = 일요일, 각 숫자가 인덱스)
week = ["월", "화", "수", "목", "금", "토", "일"]
print(today.weekday())
print("요일 : ", week[today.weekday()] + "요일")

# 날짜 계산
tomorrow = today + datetime.timedelta(days=1)
next_week = today + datetime.timedelta(days=7)
print(tomorrow)
print(next_week)







# --------------------------------------------------------
# 같은 폴더의 내 파일 불러오기
# --------------------------------------------------------

# 같은 폴더에 있는 my_tools.py를 가져오기
# .py는 빼고 파일 이름만 쓸 것!
# import my_tools     (O)
# import mt_tools.pt  (X)

import my_tools

# 모듈 안의 변수도 가져다 쓸 수 있음!
print("모듈 버전 : ", my_tools.VERSION)
print("작성자 : ", my_tools.AUTHOR)

print("\n[숫자 변환 함수들]")
print("to_int(' 4500 ') = ", my_tools.to_int(" 4500 "))
print("to_int('사천오백') = ", my_tools.to_int("사천오백"))
print("to_int('사천오백', -1) = ", my_tools.to_int("사천오백", -1))
print("clean_number('4,500원') = ", my_tools.clean_number("4,500원"))

print("\n[통계 함수들]")
print("get_average([90, 85, 100]) = ", my_tools.get_average([90, 85, 100]))
print("find_max([3, 9, 1]) = ", my_tools.find_max([3, 9, 1]))
print("find_min([3, 9, 1]) = ", my_tools.find_min([3, 9, 1]))

# pandas를 사용하는 것과 동일!
# 다른 파일에 있는 함수를 가져와서 사용한 것 뿐
# pandas 또한 결국 누군가 만들어 둔 .py 파일 묶음







# --------------------------------------------------------
# 내 모듈에도 별칭과 골라오기 가능
# --------------------------------------------------------

import my_tools as mt

print("[별칭] import my_tools as mt")
print("mt.get_average([1, 2, 3, 4]) = ", mt.get_average([1, 2, 3, 4]))

from my_tools import make_bar, format_money
print("\n [골라오기] from my_tools import make_bar, format_money")
print("make_bar(5000) = ", make_bar(5000))
print("format_money = ", format_money(12345))







# --------------------------------------------------------
# __name__의 정체
# --------------------------------------------------------

# import하면 그 파일이 한 번 실행됨
# 그런데 my_tools.py 맨 아래에 테스트 코드가 잔뜩 있었음
# 그게 전부 실행되면 곤란한 상황이 발생
# 그것을 방지하는 것이 이 블록

# if __name__ == "__main__":
#      테스트 코드

# [원리]
# 파이썬 파일마다 __name__ 이라는 변수를 자동으로 생성
# 직접 실행한 파일 -> __name__은 "__main__"
# import된 파일 -> __name은 파일 이름("my_tools")
# 그래서 __name__ == "__main__"인지 확인하면 '지금 내가 직접 실행'된 것인지 확인 가능
# 앞 뒤 밑줄 두개의 의미 : 파이썬이 특별하게 다루는 이름이라는 표시
# 우리가 직접 만들 일은 거의 없고 있는 걸 읽기만 하면 됨

print("이 파일의 __name__ : ", __name__)
print("my_tools의 __name__ : ", my_tools.__name__)

# 지금 실행 중인 파일은 -> "__main__"
# my_tools는 import된 것 -> "my_tools"

# my_tools.py 안의 if __name__ == "__main__":
#                     print("자체 테스트")
# 블록은 현재 실행되지 않았음!

# 터미널에서 my_tools.py를 실행하면 테스트 출력이 나온다






# --------------------------------------------------------
# 모듈을 만들 때의 규칙
# --------------------------------------------------------

# 1) 관련이 있는 함수끼리 모아두기
#    - 숫자 변환/통계/파일 처리 등으로
# 2) 각 함수에 설명 달기
#    - def 바로 아래에 설명 작성 (docstring)
# 3) 실행 코드는 if __name__ = "__main__": 안에 넣기
# 4) 파일 맨 위에는 이 파일에 대한 설명 작성

# [docstring]이 좋은 이유
# help()로 설명 보기 가능
# VS Code에서 함수 이름에 마우스를 올리면 설명 보기 가능





# --------------------------------------------------------
# pip 외부 패키지 설치하기
# --------------------------------------------------------

# pandas, numpy는 파이썬에 딸려오지 않음. 직접 설치해야 함
# 설치는 파이썬 코드가 아니라 터미널에서 하는 것

# [자주 쓰는 pip 명령어]
# pip install pandas -> 설치
# pip install pansdas numpy -> 여러 개 한 번에
# pip install pandas== 2.0.0 -> 특정 버전 설치
# pip list -> 설치된 목록 보기
# pip show pandas -> 정보 보기
# pip install --upgrade pandas -> 최신으로 업데이트
# pip uninstall pandas -> 삭제

# [윈도우에서 pip가 동작하지 않을 때]
# python -m pip install pandas (작성 시 대부분 해결)
# '지금 실행 중인 파이썬의 pip를 쓰겠다'는 의미
# 파이썬이 여러 개 깔려 있을 때 특히 중요

# [회사 컴퓨터에서 설치가 되지 않을 때]
# 사내망 방화벽 때문일 수 있음
# IT팀에 문의하거나 프록시 설정 필요




# --------------------------------------------------------
# 가상환경 - 개념 파악
# --------------------------------------------------------

# [문제 상황]
# A 프로젝트는 pandas 1.5 버전이 필요하고
# B 프로젝트는 pandas 2.0 버전이 필요한 경우라면
# 컴퓨터 한대에 하나만 설치할 수 있어 충돌 발생

# [해결책 : 가상환경]
# 프로젝트마다 별도의 작은 파이썬 환경 생성
# 각 환경은 서로 완전히 독립적
# python -m  venv venv    -> 가상환경 만들기
# venv\Scripts\acticate   -> 윈도우 켜기
# source venv/bin/activate    -> 맥, 리눅스 켜기
# deactivate -> Rmrl

# 켜지면 터미널 앞에 (venv)가 붙는다
# 그 상태에서 pip install 하면 이 프로젝트에만 설치됨

# 지금 당장은 완벽하게 숙지하지 않아도 괜찮고 pip install만 사용해도 문제 없음
# 다만 나중에 회사에서 프로젝트를 받으면 반드시 만나게 될 것이므로
# 이런 것이 있다는 것만 기억해 둘 것
# README 파일에 "가상환경을 만들고..." 라고 적혀있을 것






# --------------------------------------------------------
# import 가 동작하지 않을 때의 체크 리스트
# --------------------------------------------------------

# ModuleNotFoundError : No module named 'pandas'
# 이 에러를 만났다면 위에서부터 순서대로 확인할 것!

# 1) 설치가 되어 있는가
#    - 터미널에서 pip list로 목록을 확인할 것
# 2) 이름을 정확히 썼는가 (대소문자 구분)
# 3) 내 파일 이름이 패키지 이름과 동일한가
#    - 자주 발생하는 실수
#    - 내 파일을 random.py로 저장해 놓고 import random 하게 되면
#      파이썬이 내 파일을 가져옴
#    - csv.py, json.py, math.py 등도 마찬가지
#    - 파일 이름을 파꿀 것!
# 4) 같은 폴더에 있는가
#    - 내가 만든 모듈일 때 해당
#    - my_tools.py가 이 파일과 같은 폴더에 있어야 함
# 5) 파이썬이 여러 개 설치되어 있지 않은가 (가장 흔한 원인)
#    - A 파이썬에 설치했는데 B 파이썬으로 실행하는 경우

# 해결 방법
# VS Code 오른쪽 아래에서 파이썬 버전 확인
# Ctrl + Shift + P -> "Python: Select Interpreter"를 선택
# 설치할 때 python -m pip install pandas 작성







# --------------------------------------------------------
# 파이썬 모듈을 어디서 찾는가
# --------------------------------------------------------

# import를 하면 파이썬은 정해진 순서대로 폴더를 뒤져 정보를 찾는다
# 그 목록이 sys.path에 들어있음
# 맨 앞이 현재 폴더
# 그래서 내가 만든 my_tools.py를 가장 먼저 찾는 것!
# 반대로 말하면 내 파일 이름이 random.py인 경우 진짜 random모듈보다 내 파일이 먼저 발견
# 위의 문제 3번이 이 때문에 발생






# -------------------------------------------------------------
# 정리
# -------------------------------------------------------------

# [import 문법]
#
#     import math                 표준 라이브러리
#     import my_tools             내가 만든 파일 (.py 는 뺀다)
#     import pandas as pd         외부 패키지 + 별칭
#     from math import sqrt       함수만 골라오기
#
#
#   [모듈 만들 때 규칙]
#
#     - 관련 있는 함수끼리 한 파일에 모은다
#     - 각 함수에 docstring 으로 설명을 단다
#     - 실행 코드는 if __name__ == "__main__": 안에 넣는다
#
#
#   [pip 명령어]
#
#     pip install 패키지명         설치
#     pip list                    목록 확인
#     python -m pip install ...   안 될 때 이렇게
#
#
#   [기억할 것 5가지]
#     1. import 는 남이 만든 코드 가져오기. 내 파일도 똑같이 가져온다
#     2. import 하면 그 파일이 한 번 실행된다
#     3. 그래서 테스트 코드는 if __name__ == "__main__": 로 감싼다
#     4. 외부 패키지는 터미널에서 pip install 로 설치한다
#     5. import 가 안 되면 5-1 의 5번(파이썬이 여러 개)부터 의심하라
