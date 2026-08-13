# --------------------------------------------------------
# 함수 안에서 함수 부르기
# --------------------------------------------------------

def discount(p):
    # 20% 할인가
    return int(p * 0.8)
def buga(price):
    # 부가세 계산
    return price * 1.1
def f_price(p):
    # 할인 후 부가세를 붙이는 함수
    return buga(discount(p))      # 안쪽 discount()가 먼저 실행
p = 50000
print("원가 50000원")
print(f"할인만 적용 : {discount(p)}")
print(f"부가세만 적용 : {buga(p)}")
print(f"할인 후 부가세 적용 : {f_price(p)}")

# 안쪽에 있는 괄호부터 계산
# 작은 함수를 조합해서 큰 기능을 만드는 것
# 프로그램을 만드는 기본 방식





# --------------------------------------------------------
# 이게 무슨 조건이지?
# --------------------------------------------------------

# 한 줄로 복잡한 코드를 작성한 경우 쉽게 무슨 의미인지 파악이 불가능
def safe_pass(pw):
    # 8자 이상 + 숫자 포함 + 영문자 포함인 경우에만 True
    if len(pw) < 8:
        return False
    if not any(ch.isdigit() for ch in pw):      # pw 안에 숫자가 하나도 없으면 False
        return False
    if not any(ch.isalpha() for ch in pw):      # pw 안에 영문자가 하나도 없으면 False
        return False
    return True
pw = "abc12345"
print(safe_pass(pw))

print("8자 이상 + 숫자 포함 + 영문자 포함")
while True:
    pw = input("비밀번호 입력 : ")
    if safe_pass(pw):
        print("사용 가능한 비밀번호")
        break
    else:
        print("사용할 수 없는 비밀번호")





# --------------------------------------------------------
# 좋은 함수 이름 짓기
# --------------------------------------------------------

# 규칙
# 1) 동사로 시작            ex. get_, make_, send_, print_
# 2) True/False 반환한다면 is_, has_, can_으로 시작
# 3) 영어 소문자 + _get     ex. get_avg
# 4) 이름만 보고도 무슨 일을 하는 지 알 수 있도록
# 주석을 작성하지 않아도 되는 이름이 가장 좋은 이름!





# --------------------------------------------------------
# 함수 없이 학생 성적 처리
# --------------------------------------------------------

kor = [90, 85, 100]
eng = [70, 95, 80]
math = [60, 75, 88]

# 국어
avg = sum(kor) / len(kor)
print("국어 평균 : ", round(avg, 1))
if avg >= 90:
    print("A")
elif avg >= 80:
    print("B")
else:
    print("C")

# 영어
avg = sum(eng) / len(eng)
print("영어 평균 : ", round(avg, 1))
if avg >= 90:
    print("A")
elif avg >= 80:
    print("B")
else:
    print("C")

# 수학
avg = sum(math) / len(math)
print("수학 평균 : ", round(avg, 1))
if avg >= 90:
    print("A")
elif avg >= 80:
    print("B")
else:
    print("C")






# --------------------------------------------------------
# 함수를 사용해 학생 성적 처리
# --------------------------------------------------------

def get_avg(scores):
    # 점수 리스트의 평균(소수 첫째 자리)
    return round(sum(scores) / len(scores), 1)
def get_grade(sc):
    # 평균을 등급으로 교환
    if sc >= 90:
        return "A"
    elif sc >= 80:
        return "B"
    else:
        return "C"

def print_std(sub, scores):
    # 과목 성적표 한 줄 출력
    avg = get_avg(scores)
    grade = get_grade(avg)
    print(f"{sub} 평균 : {avg} 등급 : {grade}")

print_std("국어", kor)
print_std("영어", eng)
print_std("수학", math)







# --------------------------------------------------------
# 함수를 써야하는 순간
# --------------------------------------------------------

# 같은 코드를 2번 이상 복사한 경우 -> 반복 제거
# 계산 결과를 다른 곳에서 재사용 -> return
# 조건식이 길어서 뜻을 알 수 없는 경우 -> 함수 이름 짓기
# 코드 덩어리에 주석으로 제목을 작성한 경우 -> 그 제목이 함수의 이름

# 함수는 자판기
# 넣으면 나온다!
# 넣은 것 -> 매개변수(파라미터)
# 나오는 것 -> return

# 함수의 진정한 장점은 코드의 길이가 짧아지는 것이 아니라 수정할 부분이 한 곳이 되는 것!

# print -> 보여주기
# return -> 값 반환(다시 쓸 값이면 return 사용)