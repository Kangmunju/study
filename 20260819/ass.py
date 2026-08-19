print("[문제 1] 편의점 상품 관리")


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, count):
        if count > self.stock:
            print(f"재고 부족 : 현재 {self.stock}개")
            return
        self.stock = self.stock - count
        print(f"{self.name} {count}개 판매")

    def restock(self, count):
        self.stock = self.stock + count
        print(f"{self.name} {count}개 입고 (현재 {self.stock}개)")

    def total_value(self):
        return self.price * self.stock

    def show(self):
        print(f"{self.name}  {self.price:,}원  재고 {self.stock}개")


item1 = Product("삼각김밥", 1500, 10)
item1.show()
item1.sell(3)
item1.sell(100)
item1.restock(10)
item1.show()
print(f"재고 총액: {item1.total_value():,}원")
print()
item2 = Product("커피", 2000, 5)
item2.show()
item2.sell(5)
item2.show()
print(f"재고 총액: {item2.total_value():,}원")


print("\n[문제 2] 회원 등급 만들기 (상속)")


class Member:
    def __init__(self, name, point=0):
        self.name = name
        self.point = point

    def get_rate(self):
        return 0.01

    def buy(self, amount):
        j_point = int(amount * self.get_rate())
        self.point = self.point + j_point
        print(f"{self.name}님 {amount:,}원 구매 ({j_point}P 적립)")

    def show(self):
        print(f"{self.name}  일반회원  보유 {self.point}P")


print("2-2. VIP 회원 클래스 (상속)")


class VipMember(Member):
    def get_rate(self):
        return 0.05

    def show(self):
        print(f"{self.name}  VIP회원  보유 {self.point}P")


m1 = Member("김철수")
m1.show()
m1.buy(10000)
m1.show()
print()
m2 = VipMember("이영희")
m2.show()
m2.buy(10000)
m2.show()
print()
m3 = Member("박민수", 300)
print("[전체 회원]")
members = [m1, m2, m3]
for m in members:
    m.show()








