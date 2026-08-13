# --------------------------------------------------------
# 실전 패턴 - 여러 건 중 일부만 실패할 때
# --------------------------------------------------------

# 데이터를 다룰 때 가장 자주 만나는 상황
# 1000건 중 3건이 이상해도 나머지 997건은 처리해야 함

# 잘못된 접근 : 이상한 데이터가 없게 만들자! -> 불가능 / 데이터는 항상 지저분

# 올바른 접근 : 이상한 것은 따로 모아두고 나머지는 처리
#             -> 총 10건 중 n건 실패, 목록 위치를 알려주기
# 이러한 방법이 실무에서 데이터를 다루는 기본 자세

# 실제 데이터는
raw_data = ["100", "200", "삼백", "400", "", "600", "700"]
numbers = []    # 성공한 값을 담을 리스트
errors = []   # 실패한 값을 담을 리스트

for item in raw_data:
    try:
      numbers.append(int(item.strip()))
    except ValueError:
       errors.append(item)
print("정상 처리 : ", numbers)
print("처리 실패 : ", errors)
print(f"총 {len(raw_data)}건 중 {len(numbers)}건 성공, {len(errors)}건 실패")
print("합계 : ", sum(numbers))

# 여기서 배울 점
# 1) for 안에 try문을 작성하면 한 건이 실패하더라도 다음 건으로 넘어간다.
# 2) 실패한 것을 버리지 않고 따로 모아둔다.
# 3) 마지막에 '몇 건 성공, 몇 건 실패'를 보고
# CSV에서 이 패턴을 그대로 사용!







# --------------------------------------------------------
# 실전 패턴 - 안전한 변환 함수 만들기
# --------------------------------------------------------

# 앞으로 계속 사용하게 될 함수
# 여기서 제대로 만들어 둘 것

# 변환에 실패하면 프로그램을 멈추는 대신 미리 정해둔 '기본값'을 리턴

def to_int(value, default=0):
    # 문자열을 정수로 바꾸는 함수
    # value : 바꿀 값
    # default : 실패 했을 때 돌려줄 값(기본 0)
    try:
        return int(str(value).strip())
        # str(value)로 한 번 감싼 이유 - value에 숫자나 None이 들어와도 에러 없이 처리하기 위해
        # None.stirp()은 에러가 나지만, str(None).stip()은 "None"을 리턴
        # strip() - 문자열의 양쪽 끝에 있는 불필요한 공백이나 지정한 문자를 제거하여 새로운 문자열을 돌려주는 기본 함수      
    except (ValueError, TypeError):
        # 괄호로 묶으면 여러 에러를 한꺼번에 잡을 수 있음
        return default 
print(to_int("100"))
print(to_int("삼백"))
print(to_int("삼백"), -1)

def to_float(value, default=0.0):
    # 문자열을 실수로 바꾸는 함수
    # value : 바꿀 값
    # default : 실패 했을 때 돌려 줄 값(기본 0.0)
    try:
        return float(str(value).strip())
            # str(value)로 한 번 감싼 이유 - value에 숫자나 None이 들어와도 에러 없이 처리하기 위해
            # None.stirp()은 에러가 나지만, str(None).stip()은 "None"을 리턴
            # strip() - 문자열의 양쪽 끝에 있는 불필요한 공백이나 지정한 문자를 제거하여 새로운 문자열을 돌려주는 기본 함수      
    except (ValueError, TypeError):
            # 괄호로 묶으면 여러 에러를 한꺼번에 잡을 수 있음
        return default
print(to_float("3.14"))
print(to_float(None))
print(to_float("3.14만원"))


# --------------------------------------------------------

# 지금까지는 에러를 잡는 방법을 배웠고 앞으로는 반대로 에러를 내는 방법에 대해 학습할 것

def set_age(age):
    if age < 0:
        raise ValueError("나이는 음수가 될 수 없습니다.")
    if age > 150:
        raise ValueError("범위 안에 해당하는 나이만 가능합니다.")
    return f"{age}세로 설정되었습니다."
print(" ", set_age(30))
# print(" ", set_age(-30))
# print(" ", set_age(-2))

# 잘못된 값을 넣으면?
try:
    print(set_age(-5))
except ValueError as e:
    print("설정 실패", e)

try:
    print(set_age(999))
except ValueError as e:
    print("설정 실패", e)

# raise를 만나면 그 즉시 함수가 끝나고 에러 발생
# 함수를 부른 쪽에서 try/except로 받아 처리할 것

# 정리
# raise : 에러를 던진다 (문제를 알린다)
# except : 에러를 받는다 (문제에 대응한다)






# --------------------------------------------------------
# try를 사용하지 않아야 하는 경우
# --------------------------------------------------------

# try/except가 만능은 아님에 유의!
# 남용하면 오히려 문제를 숨기게 된다.

# 나쁜 예시

# 1) 범위가 너무 넓음
# try:
#     data = read_file()
#     result = calculate(data)
#     save(result)
# except:
#     print("에러")
# try 안 세 줄 중 어느 부분에서 문제가 생겼는 지 알 수 없음
# try 안에는 '에러가 날 만한 최소한의 코드만 작성'할 것

# 2) 에러를 그냥 무시
# try:
#     중요한 작업()
# except:
#     pass      아무것도 하지 않음
# 문제가 생겨도 알 수 없으므로 '최소한의 기록'을 남길 것

# 3) if로 충분한데 try를 사용
# try:
#     print(my_list[0])
# except IndexError:
#     print("비었음")
# 이러한 경우에는 차라리
# if len(my_list) > 0:
#     print(my_list[0])
# else:
#     print("비었음")     처럼 작성하는 것이 낫다

# 미리 확인할 수 있는 것은 if로 확인할 것!
# try는 미리 예상은 가능하나 막을 수 없는 상황에 사용할 것!

# try 범위를 넓게 잡으면 어느 부분이 문제인지 알 수 없게 되므로 주의!
# except에서 pass를 사용하면 문제가 숨겨져 버리므로 주의! (사용하지 말 것)
# if로 확인 할 수 있으면 if를 사용할 것!

# --------------------------------------------------------

# 1. 위 리스트에서 숫자로 바꿀 수 있는 것만 골라 합계와 실패 개수를 돌려주는 함수를 만들기.
practice_data = ["10", "20", "삼십", "40", "", "60"]
numbers = []
errors = []
for item in practice_data:
    try:
      numbers.append(int(item.strip()))
    except ValueError:
       errors.append(item)
print("정상 처리 : ", numbers)
print("처리 실패 : ", errors)
print(f"총 {len(practice_data)}건 중 {len(numbers)}건 성공, {len(errors)}건 실패")
print("합계 : ", sum(numbers))

# 2. 두 수를 나누는 함수를 만들기. 단, 0으로 나눌 수 없고 숫자가 아니면 "숫자가 아님"을 리턴.
def divide(a, b):
    try:
        a = int(a)
        b = int(b)
        result = a / b
    except ValueError:
        return "숫자가 아님"
    except ZeroDivisionError:
        return "0으로 나눌 수 없음"
    else:
        return result


# 3. 점수 0 ~ 100을 받아 등급을 돌려주는 함수 만들기. 단, 범위를 벗어나면 raise로 ValueError를 리턴.
def get_grage(score):
    if score < 0 or score > 100:
        raise ValueError("점수는 0 ~ 100 사이!")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"


