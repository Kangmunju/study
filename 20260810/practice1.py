# 1. 숫자맞히기
num = 7
tries = 0
while True:
    n = int(input("숫자입력 : "))
    tries += 1
    if n == num:
        print(f"{tries}회")
        break
    elif n > num:
        print("더 작게!")
    else:
        print("더 크게!")

# 2. 장바구니
cart = []
count = 0
while True:
    x = input("상품 : ")
    if x == "그만":
        print(f"장바구니 : {cart} / 총 {count}개")
        break
    else:
        count += 1
        cart.append(x)



# 3. 점수 입력받아 통계
scores = []
while True:
    n = int(input("점수 : "))
    if n == -1:
        break
    elif n < 0 or n > 100:
        print("잘못된 점수입니다")
    else:
        scores.append(n)
print(f"평균 : {sum(scores) / len(scores):.1f} / 최고 : {max(scores)} / 최저 : {min(scores)}")


# 4. 단어 개수 세기
words = {}
while True:
    w = input("단어 입력(end: 종료): ")
    if w == "end":
        break
    if w in words:
        words[w] += 1
    else:
        words[w] = 1
for word, c in words.items():
    print(f"{word}: {c}번")



# 5. 자판기
money = 5000
menu = {"콜라": 1500, "사이다": 1300, "물": 800}
bought = []
while True:
    print(f"메뉴 : {menu}")     #반복마다잔액이랑메뉴보여줘야됨
    print(f"남은 돈 : {money}원")
    name = input("음료 : ")
    if name == "종료":
        break
    if name not in menu:
        print("그런 음료는 없습니다.")
        continue
    if money < menu[name]:
        print("잔액이 부족합니다.")
    else:
        bought.append(name)
        money -= menu[name]
    if money < 800:
        break
print(f"구매 목록 : {bought} / 남은 돈 : {money}원")