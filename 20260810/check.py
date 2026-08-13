
money = 5000
menu = {"콜라": 1500, "사이다": 1300, "물": 800}
bought = []
while True:
    print(f"메뉴 : {menu}")     #반복할때마다 잔액이랑메뉴보여줘야됨
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