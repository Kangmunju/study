# 30. 장바구니 갱신
menu = {"아메리카노": 4500, "라떼": 5000, "케이크": 6500}
order = ["아메리카노", "케이크", "라떼", "아메리카노"]
# 주문내역을수량과함께정리
# 각항목소개와총액출력
# 총액이만원이상십퍼할인
# 최종금액천단위
c = {}
# c = {'k':'v'}
# c['새로운키'] = '새로운키의 밸류
# 개수
for i in order:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
# 소계총액
total = 0
for i in c:
    price = menu[i] * c[i]
    total += price
    print(f"{i} {c[i]}개 = {price:,}원")
# 합계
print(f"합계: {total:,}원")
# 10%할인
if total >= 20000:
    print("10% 할인 적용")
    total = total * 0.9
# 최종
print(f"최종: {total:,.0f}원")
