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
print("반복문 마침")  # 들여쓰기 밖 -> 한 번만 실행

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
    print(ch)  # "파", "이", "썬"


scores = {"국어": 90, "영어": 85}  # 딕셔너리는 기본적으로 키를 뽑음
for i in scores:
    print(i)  # 국어 영어

for i in scores.values():
    print(i)  # 90 85

for i, j in scores.items():
    print(f"{i} : {j}점")

for i in range(1, 11):
    print(i)  # 1부터 10까지 출력


# 1. 기본 문법
# for 변수 in 반복할_대상:
#     실행할 코드

# for i in [1, 2, 3]:
#     print(i)

# for : 반복
# i : 하나씩 저장할 변수
# in : ~ 안에서 하나씩 꺼내라
# [1, 2, 3] : 반복 대상


# 2. 문자열 반복
# word = "python"
# for ch in word:
#     print(ch)
# 각 알파벳이 한 줄 씩 출력
# ch 에는 한 글자씩 저장


# 3. 리스트 반복
# fruits = ["사과", "바나나", "포도"]
# for fruit in fruits:
#     print(fruit)
# 각 요소 하나씩 각 줄에 출력


# 4. range() 사용
# for i in range(5):
#     print(i)
# 0부터 4까지 각각 한 줄씩 출력


# 5. 시작과 끝 지정
# for i in range(1, 6):
#     print(i)
# 1부터 5까지(마지막 포함하지 않음)


# 6. 증가값 지정
# for i in range(2, 11, 2):
#     print(i)
# 2 4 6 ... 10 <- 한 줄 씩 출력


# 7. 딕셔너리 반복

# - 키만 출력
# student = {"국어": 90, "영어": 80, "수학": 100}
# for key in student:
#     print(key)
# 국어 영어 수학 <- 한 줄 씩 출력

# - 값 출력
# for value in student.values():
#     print(value)
# 90 80 100 <- 한 줄 씩 출력

# - 키와 값 출력
# for key, value in student.items():
#     print(key, value)


# 8. 리스트 안 딕셔너리
# students = [{"name":"민수", "국어": 95},
#             {"name":"철수", "국어": 75}
# ]
# for s in students:
#     print(s["name"])
# 민수 철수 <- 한 줄 씩 출력

# +) 응용
# students = [
#    {"name": "민수", "국어": 95},
#    {"name": "철수", "국어": 75},
#    {"name": "영희", "국어": 88},
#    {"name": "지훈", "국어": 92}
# ]
# for i in range(len(students)):
#     if i % 2 == 0:
#         print(studens[i]["name"])
# 민수 영희 <- 한 줄 씩 출력


# 9. 합계 / 평균 구하기
# numbers = [10, 20, 30]
# total = 0
# for n in numbers:
#     total += n
# avg = total / len(numbers)
# print(total)
# print(avg)


# 10. 조건문과 함께 사용
# scores = [90, 45, 88, 60]
# for score in scores:
#   if score >= 90:
#       print("합격")
#   else :
#       print("불합격")


# 11. 최대값 찾기
# numbers = [4, 8, 2, 10]
# max_num = numbers[0]
# for n in numbers:
#     if n > max_num:
#         max_num = n
# print(max_num)


# 12. 최소값 찾기
# numbers = [4, 8, 2, 10]
# min_num = numbers[0]
# for n in numbers:
#     if n < min_num:
#         min_num = n
# print(min_num)


# 13. 횟수 세기
# numbers = [1, 2, 2, 3, 2]
# count = 0
# for n in numbers:
#     if n == 2:
#         count += 1
# print(count)


# 14. 많이 쓰는 패턴

# - 리스트 출력
# for x in numbers:

# - 횟수 반복
# for i in range(10)

# - 인덱스 사용
# for i in range(len(numbers)):
#     print(numbers[i])

# - 딕셔너리
# for key in dic:

# - 키와 값
# for key, val in dic.items():


# 구구단
# gu = int(input("단 입력 : "))
# for i in range(1, 10):
#     print(f"{dan} x {i} = {dan * i}")

# 가로 별 출력
# for i in range(5):
#     print("*", end="")

# 왼쪽 직각 삼각형
# for i in range(1, 6):
#     print("*" * i)
# for i in range(1, 6):
#     for j in range(i) :
#         print("*", end="")
#     print()

# 오른쪽 직각 삼각형
# for i in range(1, 6):
#     print(" " * (5 - i) + "*" * i)

# 역삼각형
# for i in range(5, 0, -1):
#     print("*" * i)

# 피라미드
# for i in range(1, 6):
#     print(" " * (5 - i) + "*" * (2 * i - 1))

# 역피라미드
# for i in range(5, 0, -1):
#     print(" " * (5 - i) + "*" * (2 * i - 1))

# 피라미드 출력하고 역 피라미드(n // 2, 0, -1)로 출력하면 다이아몬드

# 속 빈 사각형
# for i in range(5):
#     if i == 0 or i == 4:
#         print("*" * 5)
#     else:
#         print("*" + " " * 3 + "*")

# 숫자 삼각형
# for i in range(1, 6):
#   for j in range(1, i + 1):
#       print(j, end="")
#   print()
# 1
# 1 2
# 1 2 3 ... 의 형태로 출력
