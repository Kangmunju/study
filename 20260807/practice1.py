# 1. 점수 통계
scores = [88, 92, 79, 95, 67, 84]
print("1번")
print(f"최고 {max(scores)} / 최저 {min(scores)} / 평균 {sum(scores) / len(scores):.1f}")


# 2. 평균 이상만 골라내기
scores = [88, 92, 79, 95, 67, 84]
avg = sum(scores) / len(scores)
new = []
for i in range(len(scores)):
    if scores[i] >= avg:
        new.insert(i, scores[i])
print("2번")
print(f"기대 출력 : 평균 {avg:.1f} 이상 : {new}")


# 3. 등급별 인원수
scores = [88, 92, 79, 95, 67, 84, 55, 73]
a = 0
b = 0
c = 0
d = 0
f = 0
for i in range(len(scores)):
    if scores[i] >= 90:
        a += 1
    elif 80 <= scores[i] <= 89:
        b += 1
    elif 70 <= scores[i] <= 79:
        c += 1
    elif 60 <= scores[i] <= 69:
        d += 1
    else:
        f += 1
print("3번")
print(f"A:{a}명 / B:{b}명 / C : {c}명 / D : {d}명 / F : {f}명")


# 4. 두번째로 큰 수
numbers = [45, 82, 17, 93, 60]
first = max(numbers)
new_numbers = numbers.copy()
new_numbers.remove(first)
# print(new_numbers)
m = new_numbers[0]
for i in range(len(new_numbers)):
    if m < new_numbers[i]:
        m = new_numbers[i]
print("4번")
print(f"{m}")


# 5. 중복 찾기
data = [3, 7, 2, 7, 9, 3, 5, 3]
result = []
for i in data:
    if data.count(i) > 1:
        if i not in result:
            result.append(i)
print("5번")
print(result)


# 6. 연속 상승 구간
temps = [12, 14, 15, 13, 16, 18, 19, 17]
count = 0
mc = 0
for i in range(len(temps) - 1):
    if temps[i] < temps[i + 1]:
        count += 1
        if count > mc:
            mc = count
    else:
        count = 0
print("6번")
print(mc)


# 7. 리스트 뒤집기
numbers = [1, 2, 3, 4, 5]
l = len(numbers)
new = []
for i in range(l - 1, -1, -1):
    new.append(numbers[i])
print("7번")
print(new)


# 8. 재고 출력 #items()아니면회차에 해당하는키:값
stock = {"사과": 5, "바나나": 0, "포도": 12}
print("8번")
for i in stock:
    if stock[i] == 0:
        print(f"{i} : 품절")
    else:
        print(f"{i} : {stock[i]}")


# 9. 최고 매출 상품
sales = {"노트북": 1200, "마우스": 340, "키보드": 780}
sell = 0
product = ""
for i in sales:
    if sales[i] > sell:
        sell = sales[i]
        product = i
print("9번")
print(f"{product} : {sales[product]}")


# 10. 총액 계산
cart = {"사과": 3, "우유": 2, "빵": 1}
price = {"사과": 1500, "우유": 2800, "빵": 3200}
total_price = 0
for i in cart:
    total_price += cart[i] * price[i]
print("10번")
print(
    f"사과 {cart['사과']}개 = {cart['사과'] * price['사과']:,}원 _ 총액 : {total_price:,}원"
)
