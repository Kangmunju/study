# --------------------------------------------------------
# 반복문
# --------------------------------------------------------

# 반복문이 필요한 이유
fruits = ["사과", "바나나", "포도"]
# 하나씩 작성하는 경우 개수가 늘 때마다 줄 추가 / 잘못 세면 Error

# 반복문을 사용하면 요소의 개수와 무관하게 2줄!
for fruit in fruits:
    print(fruit)

# 기본 구조
# for fruit in fruits:
#  |     |   |    |
#  |     |   |  꺼낼 대상
#  |     |   |
#  |     |  in 키워드
#  |     |
#  |  꺼낸 값을 담을 변수
# for 키워드

# 동작 : 값을 하나 꺼내서 fruits에 넣고 안쪽을 실행
#        -> 안쪽을 실행
#        -> 다음 값 꺼내기
#        -> 이하 반복
#        -> 꺼낼 것이 더 없으면 종료

for fruit in fruits:
    print(f"과일 : {fruit}")
print("반복문 마침")      # 들여쓰기 밖 -> 한 번만 실행

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    print("지금은", num)

for i in range(7):
    print(i)  # 0, 1, ...6

for i in range(1, 101):
    print(i)  # 1, 2, ... 100

name_list = {"name": "철수", "age": 25}
for i in name_list.values():
    print(i)
for i in name_list:
    print(f"{i}은 {name_list[i]}")

name_list = [
    {"name": "김덕배", "age": 25, "city": "서울"},
    {"name": "김춘식", "age": 23, "city": "인천"},
    {"name": "김춘삼", "age": 22, "city": "경기"},
]  # 출력하면 딕셔너리 그대로 나옴

for i in name_list:
    print(i)
    for x in i:
        print(x)


for ch in "파이썬":
    print(ch)     # "파", "이", "썬"


scores = {"국어":90, "영어":85}     # 딕셔너리는 기본적으로 키를 뽑음
for i in scores:
    print(i)      # 국어 영어

for i in scores.values():
    print(i)      # 90 85

for i, j in scores.items():
    print(f"{i} : {j}점")

for i in range(1, 11):
    print(i)          # 1부터 10까지 출력




