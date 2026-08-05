print(" -- 스마트 무인 카페에 오신 것을 환영합니다! --")
print(" -----------------------------------------")

# input()의 결과는 항상 문자열
price = int(input("아메리카노 1잔의 가격을 입력(ex. 4000) : "))
cup = int(input("주문할 잔 수를 입력(ex. 3) : "))
discount = float(input("오늘의 할인율(ex. 10.5) : "))
money = int(input("계산할 현금 총액 입력(ex. 15000) : "))

total_price = price * cup
discount_money = int(total_price * discount / 100)
final_price = int(total_price - discount_money)
order = money >= final_price

print(" -----------------------------------------")
print("       [영수증 및 결제 내역]     ")
print(" -----------------------------------------")

print(f"1. 메뉴 가격 : {price}원")
print(f"2. 주문 수량 : {cup}잔")
print(f"3. 총 주문액 : {total_price}원")
print(f"4. 할인 금액 : {discount_money}원")

print(" -----------------------------------------")
print(f"1. 최종 결제 : {final_price}원")
print(f"2. 투입 금액 : {money}원")
print(" -----------------------------------------")

print(f"1. 결제 가능 여부 : {order}")
print(f"2. 거스름돈 : {money - final_price}원")

print(" -----------------------------------------")
print("이용해 주셔서 감사합니다. 좋은 하루 보내세요!")
