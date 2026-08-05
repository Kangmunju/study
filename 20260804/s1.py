# --------------------------------------------------------
# 1. 산술 연산자
# --------------------------------------------------------

# //와 %는 자주 쓰임
print(10 % 2 == 0)  # True -> 짝수 판별(나머지가 0인 경우)
print(130 // 60, 130 % 60)  # 2 10 -> 130초 = 2분 10초

# 문자열에서 쓰이는 연산자
print("파이" + "썬")  # 파이썬 이어 붙이기
print("-" * 20)  # 구분선 만들 때 유리함


# --------------------------------------------------------
# 2. 대입 연산자
# --------------------------------------------------------

x = 10  # 기본 대입 : 오른쪽 값을 왼쪽에 넣기

# 자기 자신을 이용해 값을 바꾸는 축약형
x += 5  # x = x + 5 -> 15
x -= 3  # x = x - 3 -> 12
x *= 2  # x = x * 2 -> 24
x /= 4  # x = x / 4 -> 6.0
x //= 2  # x = x // 2 -> 3.0
x **= 2  # x = x ** 2 -> 9.0
print(x)  # 9.0

# 문자열에서도 가능
message = "안녕"
message += "하세요"
print(message)  # 안녕하세요


# --------------------------------------------------------
# 3. 비교 연산자 - 조건문의 핵심
# --------------------------------------------------------

# 두 값을 비교해서 True/False 반환

print(10 > 5)  # True
print(10 < 5)  # False
print(10 >= 10)  # True
print(10 <= 9)  # False
print(10 == 10)  # True
print(10 != 10)  # False

# =와 ==는 다른 것임에 주의!
age = 20  # 대입(값을 넣음)
print(age == 20)  # 비교

# 비교의 결과는 bool
result = 10 > 5
print(result)  # True
print(type(result))  # bool

# 문자열도 비교 가능
print("abc" == "abc")  # True
print("abc" == "ABC")  # False -> 대소문자를 구분
print("apple" < "banana")  # True -> 사전 순서로 비교

# 자료형이 달라서 비교가 되지 않는 경우
print(10 == "10")  # False -> 숫자와 문자열은 절대 같지 않음
print(10 > "5")  # TypeError -> 크기 비교는 아예 불가

# 파이썬만의 편한 문법 : 범위를 한번에
score = 85
print(60 <= score <= 100)  # True


# --------------------------------------------------------
# 4. 논리 연산자 - 조건문의 핵심
# --------------------------------------------------------

# 여러 조건을 묶을 때 사용

# and : 둘 다 참인 경우
print(True and True)  # True
print(True and False)  # False
print(False and False)  # False

# or : 하나라도 참인 경우
print(True or False)  # True
print(False or False)  # False
print(False or True)  # True

# not : 결과물 뒤집기
print(not True)  # False
print(not False)  # True
print(not (10 > 5))  # False

# 실제 사용
age = 25
has_ticket = True

print(age >= 20 and has_ticket)  # True
print(age < 20 or age > 80)  # False
print(not has_ticket)  # False

# and : '전부 만족'해야 가능
# or : '하나만 만족'해도 가능

# 자주 하는 실수
day = "토"
print(day == "토" or "일")  # True 의도한 대로 동작하지 않음

# 짧은 회로 평가
# and는 앞이 False면 뒷부분을 판단하지 않음 -> 전부 True여야 하기 때문
# or는 앞이 True면 뒷부분을 판단하지 않음 -> 하나라도 True이면 되기 때문
value = ""
print(
    value != "" and int(value) > 0
)  # False -> 앞부분에서 False로 걸러냈기 때문에 뒷부분을 판단하지 않아 Error가 나지 않음


# --------------------------------------------------------
# 5. 멤버십 연산자(in / not in)
# --------------------------------------------------------

# 어떤 값이 안에 들어있는 지 확인

# 문자열
text = "python programing"
print("python" in text)  # True
print("java" in text)  # False
print("java" not in text)  # True

# 리스트
fruits = ["사과", "바나나", "포도"]
print("사과" in fruits)  # True
print("딸기" in fruits)  # False

# 실제 활용
answer = "y"
print(answer in ["y", "Y", "yes"])  # True -> 여러가지 값 중 하나인지 한번에 확인
# answer == "y" or answer == "Y" or answer == "yes"로 작성하지 않아도 된다(더욱 간편)


# --------------------------------------------------------
# 6. 식별 연산자(is/ is not)
# --------------------------------------------------------

# '같은 값'이 아닌 '완전히 같은 것'인지를 확인

# 주로 None 확인할 때 사용
result = None
print(result is None)  # True -> 권장되는 방식
print(result is not None)  # False
print(result == None)  # True -> 동작은 하지만 is를 쓰는 것이 관례

# 값 비교에는 is를 쓰지 않음에 주의!
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True -> 내용이 같음
print(a is b)  # False -> 서로 다른 리스트이기 때문

# 값 비교는 ==
# None 확인은 is

# 연산자 우선 순위
# 위에 있을 수록 먼저 계산
# 1. () 괄호
# 2. ** 거듭제곱
# 3. * / // % 계열
# 4. + -
# 5. > < >= <= == != in is 비교 계열
# 6. not
# 7. and
# 8. or

# 비교가 논리보다 먼저!
print(3 > 1 and 5 > 2)  # True

# and가 or 보다 우선!
print(True or False and False)  # True
print((True or False) and False)  # False -> () 괄호 사용을 권장

# 조건문 맛보기
age = 25
if age >= 20:
    print("성인")
else:
    print("미성년")

# 연산자를 알아야 조건문을 작성할 수 있다!
