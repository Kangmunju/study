print("[문제 1] 강아지")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.count = 0  # 먹은간식개수기억하는값(받을값아니라고써있음) 기본값0

    def bark(self):
        print(f"멍멍! 나는 {self.name}야")

    def eat(self, count):
        self.count += count
        print(f"{self.name}가 간식 {count}개 먹었다 (총 {self.count}개)")

    def birthday(self):
        self.age += 1
        print(f"{self.name}의 생일! 이제 {self.age}살")

    def is_puppy(self):
        if self.age <= 2:
            return True
        else:
            return False

    def show(self):
        if self.is_puppy():
            print(f"{self.name} ({self.age}살, 강아지)  간식 {self.count}개")
        else:
            print(f"{self.name} ({self.age}살, 성견)  간식 {self.count}개")


d1 = Dog("초코", 3)
d1.show()
d1.bark()
d1.eat(2)
d1.eat(3)
d1.birthday()
d1.show()
print()
d2 = Dog("콩이", 1)
d2.show()
print("콩이는 강아지인가?", d2.is_puppy())

print("\n[문제 2] 성적표")


class Report:
    def __init__(self, name):
        self.name = name
        self.scores = {}

    def add(self, subject, score):
        if score < 0 or score > 100:
            print(f"잘못된 점수: {score}")
            return
        self.scores[subject] = score
        print(f"{subject} {score}점 등록")

    def average(self):
        if len(self.scores) == 0:
            return 0
        else:
            return round(sum(self.scores.values()) / len(self.scores), 1)

    def grade(self):
        if self.average() >= 90:
            return "A"
        elif self.average() >= 80:
            return "B"
        elif self.average() >= 70:
            return "C"
        else:
            return "D"

    def best(self):
        if len(self.scores) == 0:
            return None
        maxsb = ""
        maxsc = 0
        for s in self.scores:  # 과목키값돌기
            if self.scores[s] > maxsc:
                maxsb = s
                maxsc = self.scores[s]  # 키에해당하는점수찾기
        return maxsb, maxsc

    def show(self):
        print(f"[{self.name} 성적표]")
        for s in self.scores:
            print(f"{s} {self.scores[s]}점")
        print(f"평균 {self.average()} ({self.grade()})")
        bestsc = self.best()  # 과목,점수순서
        if bestsc is not None:
            maxsb, maxsc = bestsc
            print(f"최고 과목: {maxsb} {maxsc}점")
        else:
            print("최고 과목: 없음")


r = Report("김철수")
r.add("국어", 90)
r.add("영어", 85)
r.add("과학", 150)
r.add("수학", 100)
r.show()
print()
r2 = Report("이영희")
r2.show()

print("\n[문제 3] 자판기")


class VendingMachine:
    def __init__(self):
        self.inmoney = 0
        self.drink = {
            "콜라": {"가격": 1500, "재고": 3},
            "사이다": {"가격": 1300, "재고": 2},
            "물": {"가격": 800, "재고": 5},
        }

    def insert(self, money):
        self.inmoney += money
        print(f"{money:,} 투입 ({self.inmoney}원)")

    def buy(self, name):
        if name not in self.drink:
            print(f"그런 음료는 없습니다: {name}")
            return
        if self.drink[name]["재고"] == 0:
            print(f"품절입니다: {name}")
            return
        if self.inmoney < self.drink[name]["가격"]:
            fail = self.drink[name]["가격"] - self.inmoney  # 부족한금액
            print(f"금액이 부족합니다 (부족액 {fail}원)")
            return
        # 안되는거다처리했으니까이제구매가능한거
        change = self.inmoney - self.drink[name]["가격"]
        self.drink[name]["재고"] -= 1
        self.inmoney = 0
        print(f"{name} 나왔습니다 (거스름돈 {change}원)")

    def show(self):
        print("[자판기]")
        for d in self.drink:
            print(f"{d} {self.drink[d]['가격']:,}원 (재고 {self.drink[d]['재고']}개)")
        print(f"투입 금액 : {self.inmoney:,}원")


v = VendingMachine()
v.show()
v.insert(1000)
v.buy("콜라")
v.insert(1000)
v.buy("콜라")
v.buy("커피")
v.show()

print("\n[문제 4] 도서 대출")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.state = True  # 대출가능
        self.name = ""  # 처음에는이름없음
        self.count = 0  # 총대출횟수처음0

    def borrow(self, who):
        if self.state != True:
            print(f"이미 대출 중입니다 (대출자: {self.who})")
            return
        self.state = False  # 이제내who가빌릴거니까F로바꿔야됨
        self.who = who
        self.count += 1
        print(f"{self.title} 대출 완료 (대출자: {self.who})")

    def give_back(self):
        if self.state == True:
            print("대출 중이 아닙니다")
            return
        print(f"{self.title} 반납 완료 (반납자: {self.who})")
        self.who = ""
        self.state = True

    def show(self):
        if self.state == True:
            print(f"{self.title} / {self.author} / 대출가능 / 누적 {self.count}회")
        else:
            print(
                f"{self.title} / {self.author} / 대출중 ({self.who}) / 누적 {self.count}회"
            )


b = Book("사피엔스", "유발 하라리")
b.show()
b.give_back()
b.borrow("김철수")
b.show()
b.borrow("이영희")
b.give_back()
b.borrow("박민수")
b.show()

print("\n[문제 5] 직원과 관리자 (상속)")


class Employee:
    def __init__(self, name, base_pay, years):
        self.name = name
        self.base_pay = base_pay
        self.years = years

    def get_position(self):
        return "사원"

    def get_bonus_rate(self):
        return 0.1

    def get_bonus(self):
        bonus = int(self.base_pay * self.get_bonus_rate() + (100000 * self.years))
        return bonus

    def get_total(self):
        return self.base_pay + self.get_bonus()

    def show(self):
        print(
            f"{self.name} ({self.get_position()}, {self.years}년)  기본급 {self.base_pay:,}원  보너스 {self.get_bonus():,}원  실수령 {self.get_total():,}원"
        )


class Manager(Employee):
    def get_position(self):
        return "팀장"

    def get_bonus_rate(self):
        return 0.3


e1 = Employee("김철수", 3000000, 3)
e1.show()
m1 = Manager("이영희", 3000000, 7)
m1.show()
print()
print("[전체 명단]")
staff = [e1, m1, Employee("박민수", 2500000, 1)]
total = 0
best = staff[0]
for s in staff:
    s.show()
    total = total + s.get_total()
    if s.get_total() > best.get_total():
        best = s
print(f"총 인건비: {total:,}원")
print(f"최고 실수령: {best.name}")

print("\n[문제 6] 계좌와 저축계좌 (상속 + 캡슐화)")


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self.ac_change = []  # 계좌내역따로만드는처음엔비어있음

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("입금액은 0보다 커야 합니다")
            return
        self._balance += amount
        print(f"{amount:,}원 입금 (잔액 {self._balance:,}원)")
        self.ac_change.append(f"입금 {amount}")

    def withdraw(self, amount):
        if self._balance < amount:
            print(f"잔액 부족 (현재 {self._balance:,}원)")
            return
        self._balance -= amount
        print(f"{amount:,}원 출금 (잔액 {self._balance:,}원)")
        self.ac_change.append(f"출금 {amount}")

    def history(self):
        print("[거래 내역]")
        for i in range(len(self.ac_change)):
            print(f"{i + 1}, {self.ac_change[i]}")

    def show(self):
        print(
            f"{self.owner}님 계좌  잔액 {self._balance:,}원  거래{len(self.ac_change)}건"
        )


class SavingsAccount(Account):
    def __init__(self, owner, balance, rate):
        self.owner = owner
        self._balance = balance
        self.ac_change = []
        self.rate = rate

    def add_interest(self):
        interest = int(self._balance * self.rate)
        print(f"이자 {interest:,}원 지급")
        self.deposit(interest)

    def withdraw(self, amount):
        if self._balance < amount + 1000:
            print(f"잔액 부족 (현재 {self._balance:,}원)")
            return
        self._balance -= amount + 1000
        print(f"출금 수수료 {1000:,}원")
        print(f"{amount:,}원 출금 (잔액 {self._balance:,}원)")
        self.ac_change.append(f"출금 {amount}")


a = Account("김철수", 50000)
a.show()
a.deposit(10000)
a.deposit(-5000)
a.withdraw(20000)
a.withdraw(999999)
a.show()
a.history()
print()
s = SavingsAccount("이영희", 100000, 0.05)
s.show()
s.add_interest()
s.withdraw(20000)
s.show()
