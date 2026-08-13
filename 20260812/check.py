# 1. 계산 기록이 남는 나눗셈기
print("1번")
success = []
fail = []
def divide(a, b):     #나눗셈
    a = int(a)
    b = int(b)
    return a/ b
def s_rate(success, fail):      #성공률
    tl = len(success) + len(fail)     #일단전체길이구하고성공률만
    if tl == 0:
        return 0
    else:
        return (len(success) / tl) * 100
def result(success, fail):      #결과출력함수?
    print("[성공 기록]")
    for i in success:
        print(i)
    rate = s_rate(success, fail)
    print(f"성공률 : {rate:.1f}%")
while True:
    n1 = input("숫자1(종료: q) : ")
    if n1 == "q":
        break
    n2 = input("숫자2 : ")
    try:
        d_result = divide(n1, n2)
    except ValueError:
        print("실패 - 숫자를 입력하세요")
        fail.append("실패 - 숫자를 입력하세요")
    except ZeroDivisionError:
        print("실패 - 0으로 나눌 수 없습니다")
        fail.append("실패 - 0으로 나눌 수 없습니다")
    else:
        print(f"{n1} / {n2} = {d_result:.2f}")
        success.append(f"{n1} / {n2} = {d_result:.2f}")
result(success, fail)



# 2. 숫자만 골라서 더하기
print("2번")
def change_n(value):
    return int(value)
total = 0     #합계구해야됨
count = 0     #횟수구해야됨
for i in range(5):
    value = input("값 : ")
    try:
        num = change_n(value)
    except ValueError:
        print(f"{value}은(는) 숫자가 아닙니다.")
    else:
        total += num
        count += 1
print(f"유효한 값 : {count}개")
print(f"합계 : {total}")





# 3. 나이 확인기
print("3번")
def check_age(age):
    if age >= 19:
        return "성인입니다"
    else:
        return "미성년자입니다"
for i in range(3):
    age = input("나이 : ")
    try:
        age = int(age)
    except ValueError:
        print("숫자를 입력하세요")
    else:
        if age < 0:
            print("나이는 0보다 작을 수 없습니다")
        else:
            print(f"{check_age(age)}")


# 4. 리스트에서 값 꺼내기
# 리스트범위넘으면예외 엑셉 인덱스에러
# 숫자아니면예외 엑셉 밸류에러
print("4번")
data = [10, 20, 30, 40, 50]
def find_idx(data, n):
    return data[n]
count = 0     #성공횟수받아야됨
for i in range(3):
    n = input("번호(0~4) : ")
    try:
        n = int(n)
        idx = find_idx(data, n)
    except ValueError:
        print("숫자를 입력하세요")
    except IndexError:
        print("그 번호는 없습니다")
    else:
        print(f"값 : {find_idx(data, n)}")
        count += 1
print(f"성공 : {count}번")





# 5. 과일 가격표
# 없는과일이면 엑셉 키에러
# 아무것도입력안하면조건문으로거르기
# 찾은 가격 모두 더해서 출력
print("5번")
price = {"사과": 1000, "바나나": 1500, "포도": 3000}
def find_p(name):
    return price[name]
total = 0
for i in range(3):
    name = input("과일 이름 : ")
    if name == "":
        print("이름을 입력")
    else:
        try:
            f_p = find_p(name)
        except KeyError:
            print("그런 과일은 없습니다")
        else:
            print(f"{name} : {f_p}원")
            total += f_p
print(f"총 가격 : {total}원")




# 6. 제대로 넣을때까지 다시 묻기
print("6번")
# 1~10까지 숫자3개합
# 숫자아니면다시입력
# 범위밖이면다시입력
# 잘못넣은거카운트안함
num = []
def get_n():
    while True:
        value = input("숫자(1~10) : ")
        try:
            num = int(value)
        except ValueError:
            print("오류 : 숫자를 입력하세요")
        else:
            if num < 0 or num > 10:
                print("오류 : 1~10 사이만 가능합니다")
            else:
                return num
for i in range(3):
    n = get_n()
    num.append(n)
print(f"입려한 숫자 : {num}")
print(f"합계 : {sum(num)}")
