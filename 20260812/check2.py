# 7. 점수로 학점
#학생3명점수
#0~100 을 벗어나면 raise Exception("0~100 사이만 가능합니다")
#숫자아니어도예외
print("7번")
def get_grade(score):
    if score < 0 or score > 100:
        raise Exception("0~100 사이만 가능합니다")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"
for i in range(3):
    score = input("점수 : ")
    try:
        score = int(score)
        grade = get_grade(score)
    except ValueError:
        print("오류 : 숫자를 입력하세요")
    except Exception:
        print("오류 : 0~100 사이만 가능합니다")
    else:
        print(f"학점 : {grade}")




# 8. 간단 계산기
print("8번")
#숫자연산자숫자입력
#- + - * / 가 아닌 연산자면 raise Exception("모르는 연산자입니다")
#0나누기예외처리
#숫자아니면입력예외
def cal(n1, op, n2):
    if op == "-":
        return n1 - n2
    elif op == "+":
        return n1 + n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2
    else:
        raise Exception("모르는 연산자입니다.")
for i in range(3):
    
    n1 = input("숫자1 : ")
    op = input("연산자(+ - * /) : ")
    n2 = input("숫자2 : ")
    try:
        n1 = int(n1)
        n2 = int(n2)
        result = cal(n1, op, n2)
    except ZeroDivisionError:
        print("오류 : 0으로 나눌 수 없습니다")
    except ValueError:
        print("오류 : 숫자를 입력하세요")
    except Exception:
        print("오류 : 모르는 연산자 입니다")
    else:
        print(f"결과 : {result}")


# 9. 이름과 점수 나눠 담기
print("9번")
#이름,정수 문자열3개
#쉼표로나눠서값2개아니면레이즈익셉션
#점수숫자아니면예외
#정상데이터만딕셔너리에저장
#마지막저장된내용반복문
students = {}
def cut_data(info):
    data = info.split(",")
    if len(data) != 2:
        raise Exception("이름, 점수 형태로 입력하세요")
    name = data[0]
    score = int(data[1])
    return name, score
for i in range(3):
    info =  input("이름,점수 : ")
    try:
        name, score = cut_data(info)
    except ValueError:
        print("점수는 숫자여야 합니다")
    except Exception:
        print("이름, 정수 형태로 입력하세요")
    else:
        students[name] = score
for name in students:
    print(f"{name} : {students[name]}점")




# 10. 종합 - 성적관리
print("10번")
#학생3명이름과점수성적표
#이름비어있으면다시입력
#점수0~100허용잘못하면다시
#평군,최고점학생이름(반복문으로)
#프로그램멈추면안됨!!
students = {}
#점수하나올바르게받는함수
def get_score():
    while True:
        value = input("점수 : ")
        try:
            score = int(value)
        except ValueError:
            print("숫자를 입력하세요")
        else:
            if 0 <= score <= 100:
                return score
            else:
                print("0~100 사이만 가능합니다")
#이름과점수를받아성적표출력하는함수
def pg(name, score):
    print(f"{name} : {score}점")
#반복문3번으로
for i in range(3):
    while True:
        name = input("이름 : ")
        #공백이면또해야됨
        if name == "":
            print("이름을 입력하세요")
        else:
            break
    score = get_score()
    students[name] = score
s = 0
best_name = ""
best_score = -1
for name in students:
    pg(name, students[name])
    s += students[name]
    if students[name] > best_score:
        best_score = students[name]
        best_name = name
avg = s / len(students)
print(f"평균 : {avg:.2f}")
print(f"1등 : {best_name}")
