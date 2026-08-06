# 8. 온도 변환과 날씨 안내
sub = int(input("섭씨 온도 : "))
fe = sub * 9 / 5 + 32

print(f"섭씨 {sub:.1f}도 = 화씨 {fe:.1f}도")

if sub >= 28:
    print("무더위입니다.")
elif 15 <= sub < 28:
    print("활동하기 좋은 날씨입니다.")
else:
    print("쌀쌀합니다.")


# 9. 요일 조회
week = {
    1: {"name": "월요일", "weekend": False},
    2: {"name": "화요일", "weekend": False},
    3: {"name": "수요일", "weekend": False},
    4: {"name": "목요일", "weekend": False},
    5: {"name": "금요일", "weekend": False},
    6: {"name": "토요일", "weekend": True},
    7: {"name": "일요일", "weekend": True},
}

date = int(input("숫자 입력 : "))
if week[date]["weekend"]:
    print("주말입니다.")
else:
    print("평일입니다.")


#  10. 학생 성적 조회
scores = {"김철수": [90, 85, 100], "이영희": [70, 65, 80]}

student_name = input("이름 입력 : ")
print(f"{student_name} 점수 : {scores[student_name]}")
print(f"1과목 점수 : {scores[student_name][0]}")

scores_sum = sum(scores[student_name])
scores_avg = scores_sum / 3
top_score = max(scores[student_name])
bottom_score = min(scores[student_name])
print(f"총점 : {scores_sum} / 평균 : {scores_avg:.1f}")
print(f"최고점 : {top_score} / 최저점 : {bottom_score}")


if scores_avg >= 80:
    print("합격")
else:
    print("불합격")


vending = {
    "콜라": {"price": 1500, "stock": 2},
    "사이다": {"price": 1400, "stock": 0},
    "물": {"price": 800, "stock": 5},
}

drink_name = input("음료 이름 : ")
loan = int(input("투입 금액 : "))

if drink_name not in vending:
    print("다른 음료 선택")
else:
    if vending[drink_name]["stock"] == 0:
        print("재고가 0인 상품")
    elif vending[drink_name]["price"] > loan:
        print(f"금액 부족 : {vending[drink_name]['price'] - loan}")
    else:
        vending[drink_name]["stock"] -= 1

        print(f"{drink_name} 구매 완료 / 거스름돈 {loan - vending[drink_name]['price']}")
        print(f"{drink_name} 남은 재고 : {vending[drink_name]['stock']}")


# 12번. 로그인과 권한 확인
accounts = {
    "alice": {"pw": "1234", "roles": ["admin", "user"]},
    "bob": {"pw": "abcd", "roles": ["user"]},
}

# 없는 아이디인 경우
# 아이디는 있는데 비밀번호가 불일기
# 다 맞으면 성공
user_id = input("아이디 : ")
user_pw = input("비밀번호 : ")

if not user_id in accounts:
    print("없는 아이디")
elif user_id in accounts and user_pw != accounts[user_id]["pw"]:
    print("비밀번호 불일치")
else:
    print(f"{user_id}님 로그인 성공")

print(f"권한 목록 : {accounts[user_id]['roles']}")

if "admin" in accounts[user_id]["roles"]:
    print("대표 권한 : admin")
    print("관리자 페이지 접근 가능")
else:
    print("일반 사용자 안내")


# 13. 재고 차감 주문
stock = {
    "사과": {"qty": 10, "price": 1500},
    "바나나": {"qty": 0, "price": 3000},
    "포도": {"qty": 5, "price": 8000},
}

# 아예 취급하지 않음
# 취급은 하는데 재고 0
# 취급은 하고 재고도 있는데 재고보다 많이 주문
# 전부 통과

buy = input("구매 : ")
many = input("수량 : ")

remain_qty = int(stock[buy]["qty"])
final_price = int(stock[buy]["price"]) * int(many)
remain_stock = int(stock[buy]["qty"]) - int(many)

if not buy in stock:
    print("취급하지 않는 상품")
else:
    if stock[buy]["qty"] == 0:
        print("재고 없음")
    elif int(stock[buy]["qty"]) < int(many):
        print(f"현재 재고 : {remain_qty}")
    else:
        print(f"{buy} {many} 주문 / 결제금액 {final_price}원")
        print(f"{buy} 남은 재고 : {remain_stock}개")


# 14. 자료형 변환 확인
score = int(input("점수 : "))
print(f"입력값 타입 : {type(score)}")
print(f"문자열로 변환 : {str(score)}")
print(f"실수로 변환 : {score:.1f}")

if score >= 90:
    print("등급 : A")
elif score >= 80:
    print("등급 : B")
else:
    print("등급 : C")


# 15. 한 줄 입력을 데이터로 바꾸기
line = input("이름,나이,도시 : ")
new_line = line.split(",")
line_dic = {}
line_dic["name"] = new_line[0]
line_dic["age"] = int(new_line[1])
line_dic["city"] = new_line[2]

print(line_dic)
print(f"10년 뒤 나이 : {line_dic['age'] + 10}")
if line_dic["city"] == "서울":
    print("수도권 거주자")
else:
    print("지방 거주자")


# 16. 장바구니 상품 조회
cart = {
    "items": ["티셔츠", "양말", "모자"],
    "prices": [15000, 3000, 12000],
}

num = int(input("번호 : "))

if num > 3:
    print("없는 번호")
else:
    print(f"{num}번 상품 : {cart['prices'][num - 1]}원")
    print(f"전체 합계 : {sum(cart['prices'])}")


# 17. 통신 요금 계산
plans = {
    "basic": {"기본요금": 12000, "무료통화": 100, "초과요금": 50},
    "premium": {"기본요금": 25000, "무료통화": 300, "초과요금": 30},
}

rank = input("요금제 : ")
call_minutes = int(input("통화 시간 : "))
call_over = int(plans[rank]["무료통화"])
basic_charge = (
    int(plans["basic"]["초과요금"]) * call_over + plans["basic"]["기본요금"] - 1000
)
pre_charge = (
    int(plans["premium"]["초과요금"]) * call_over + plans["premium"]["기본요금"]
)

if rank == "basic":
    print(
        f"요금제 : {rank} / 사용량 : {call_minutes} / 초과 : {call_minutes - call_over}"
    )
    print(f"이번 달 요금 : {basic_charge}")
else:
    print(
        f"요금제 : {rank} / 사용량 : {call_minutes} / 초과 : {call_minutes - call_over}"
    )
    print(f"이번 달 요금 : {pre_charge}")


# 18. 설문 응답 기록
survey = {"질문": "개인정보 수집에 동의하십니까?", "응답": [], "동의수": 0}

question = input("개인정보 수집에 동의하십니까? : ")
if question == "y":
    survey["응답"] = "동의"
    survey["동의수"] = int(survey["동의수"]) + 1
    print("동의해주셔서 감사합니다.")
else:
    print("비동의")

print(survey)
print(f"마지막 응답 : {survey['응답']}")


# 19. 영화관 요금 계산
ticket = {
    "성인": {"price": 12000, "학생할인": 2000},
    "청소년": {"price": 9000, "학생할인": 1000},
    "어린이": {"price": 6000, "학생할인": 0},
}

# 신분이 학생(성인, 청소년)이면서 학생할인 금액이 0이상이면 할인 적용
age = int(input("나이 : "))
who = input("신분 : ")
adult_charge = int(ticket["성인"]["price"]) - int(ticket["성인"]["학생할인"])
middle_charge = int(ticket["청소년"]["price"]) - int(ticket["청소년"]["학생할인"])

if age >= 20 and who == "학생":
    print(f"학생 할인 : {ticket['성인']['학생할인']}원 적용")
    print(f"구분 : 성인 / 최종 요금 : {adult_charge}원")
elif 13 <= age < 20:
    print(f"학생 할인 : {ticket['청소년']['학생할인']}원 적용")
    print(f"구분 : 성인 / 최종 요금 : {middle_charge}원")
else:
    print("학생 할인 적용되지 않음")
    print(f"구분 : {who} / 최종요금 : {ticket['어린이']['price']}")


# 20. 학급 명단 조회

school = {
    "3학년": {
        "1반": {"teacher": "박선생", "students": ["김철수", "이영희", "박민수"]},
        "2반": {"teacher": "최선생", "students": ["정수진", "한동훈"]},
    }
}

class_name = input("반 : ") + "반"  # 숫자만 입력
class_num = int(input("번호 : "))

student_num = len(school["3학년"][class_name]["students"])

print(f"3학년 {class_name} 담임 : {school['3학년'][class_name]['teacher']}")
print(f"학생 수 : {student_num}")
print(f"{class_num}번 학생 : {school['3학년'][class_name]['students'][class_num - 1]}")
