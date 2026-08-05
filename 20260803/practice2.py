print("-- VIP 통합 무인 키오스크 시스템 --")
print("--------------------------------")

price = int(input("1인 영화 관람료 입력(ex. 1000) : "))
count = int(input("총 예매 인원 수 입력(ex. 3) : "))
pop_set_p = int(input("팝콘 1개 세트 가격 입력(ex. 5000) : "))
pop_set_c = int(input("구매할 팝콘 세트 개수 입력(ex. 1) : "))

member = input("VIP 회원입니까? (y/n) : ")
is_member = member == "y"

money = int(input("보유한 현금 총 금액 입력(ex. 100000) : "))

movie_total = price * count
pop_total = pop_set_c * pop_set_p
price_total = movie_total + pop_total
discount = 3000 * is_member
order = money >= price_total

print("--------------------------------")
print("     [최종 정산 및 영수증]     ")
print("--------------------------------")

print(f"1. 영화 관람료 합계 : {movie_total}원")
print(f"2. 팝콘 세트 합계 : {pop_total}원")
print(f"3. 총 주문 금액 : {price_total}원")
print(f"4. VIP 할인 적용 : -3000원 (회원 여부 : {is_member})")

print("--------------------------------")

print(f"1. 최종 결제 금액 : {price_total - discount}")
print(f"2. 보유 현금 총액 : {money}원")
print(f"3. 거스름돈 : {money - price_total}원")

print("--------------------------------")
print(f"정상 예매 승인 : {order}")
print("--------------------------------")
