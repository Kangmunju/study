# 1번
print("1번")
age = int(input("나이 입력 : "))
if age >= 20:
    print("성인")
else:
    print("미성년자")
print("\n")


# 2번
print("2번")
number = int(input("판별할 숫자 입력 : "))
if number % 2 == 0:
    print("짝수")
else:
    print("홀수")
print("\n")


# 3번
# 90 이상 A / 80 이상 B / 70 이상 C / 60 이상 D / 그 외 F
print("3번")
score = int(input("점수 입력 : "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
print("\n")


# 4번
# 아이디와 비밀번호를 입력받아,
# 아이디가 "admin"이고 비밀번호가 "1234"면 "로그인 성공"
# 아이디만 맞으면 "비밀번호가 틀렸습니다"
# 아이디가 틀리면 "존재하지 않는 아이디입니다"
print("4번")
user_id = input("ID 입력 : ")
user_pw = input("PASSWORD 입력 : ")
if user_id == "admin" and user_pw == "1234":
    print("로그인 성공")
elif user_id == "admin" and user_pw != "1234":
    print("비밀번호가 틀렸습니다")
elif user_id != "admin" and user_pw == "1234":
    print("존재하지 않는 아이디입니다")
else:
    pass
print("\n")

# 5번
# 세 개의 숫자를 입력받아 가장 큰 수를 출력
# (max() 함수를 쓰지 말고 조건문으로)
print("5번")
num1 = int(input("첫번째 숫자 입력 : "))
num2 = int(input("두번째 숫자 입력(첫번째 숫자와 동일한 수 X) : "))
num3 = int(input("세번째 숫자 입력(첫번째, 두번째 숫자와 동일한 수 X) : "))
if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
elif num2 > num3:
    print(num2)
else:
    print(num3)
print("\n")

# 6번
# 연도를 입력받아 윤년인지 판별
# 규칙: 4로 나누어떨어지면 윤년
# 단 100으로 나누어떨어지면 평년
# 단 400으로 나누어떨어지면 윤년
print("6번")
year = int(input("연도 입력 : "))
if year % 4 == 0:
    if year % 400:
        print("윤년")
    elif year % 100:
        print("평년")
else:
    print("평년")
