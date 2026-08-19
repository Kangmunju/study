# --------------------------------------------------------
# 상속이란?
# --------------------------------------------------------

# 이미 만들어 둔 클래스를 물려받아 새 클래스를 만드는 것

# class 자식 클래스 (부모 클래스)
# 부모의 속성과 메서드를 그대로 물려받고
# 필요한 것만 추가 하거나 바꾸면 된다

# [사용하는 이유]
# 비슷한 클래스를 여러 개 만들 때 중복을 피할 수 있음
# 예를 들어 일반계좌, 저축계좌, 마이너스통장을 개설한다고 가정
# 입금, 출금, 조회등의 기능은 셋 다 동일 (이자 개선이나 출금 한도 정도가 다른 점)
# 상속을 사용하면 공통 부분을 한 번만 쓰면 된다

# 부모
class Account:
    """은행 계좌"""

    def __init__(self, owner, balance):
        self.owner = owner  # 김철수 -> '김철수'가 들어감
        self.balance = balance  # 5000 -> self.balance 5000

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액 부족")
        self.balance = self.balance - amount

    def show(self):
        print(f"{self.owner}님의 잔액 : {self.balance:,}원")


# Account 상속
class SavingAccount(Account):
    """저축계좌, Account를 물려받는다"""

    def __init__(self, owner, balance, rate):
        # 부모의 __init__을 먼저 실행
        super().__init__(owner, balance)
        # 저축계좌만의 속성을 추가
        self.rate = rate  # 이자율

    def add_interest(self):
        """저축계좌에만 있는 기능 - 이자 붙이기"""
        interest = int(self.balance * self.rate)
        self.balance = self.balance + interest
        print(f"이자{interest:,}원이 붙었습니다.")


sa = SavingAccount("김철수", 100000, 0.03)
sa.deposit(50000)  # Account에서 물려받은 메서드
sa.add_interest()  # SavingAccount만의 메서드
sa.show()  # Account에서 물려받은 메서드

# SavingAccount에는 deposit과 show를 만들지 않았음에도 불구하고 사용 가능.
# Account에서 물려 받았기 때문!

# super().__init__(owner, balance)
# super() : 부모 클래스
# 부모의 __init__을 먼저 실행해 owner, balance를 세팅한 뒤
# 자기만의 rate를 추가


# --------------------------------------------------------
# 메서드 덮어쓰기 (오버라이딩)
# --------------------------------------------------------

# 물려받은 메서드를 그대로 쓰지 않고 자식 클래스에서 다시 정의하면 그것이 우선!
# -> '오버라이딩(overriding)'
# 덮어쓰기라고 생각해도 됨


class CreditAccount(Account):
    """마이너스 통장, 한도까지 마이너스 출금 가능"""

    def __init__(self, owner, balance, limit):
        super().__init__(owner, balance)
        self.limit = limit  # 마이너스 한도

    def withdraw(self, amount):
        """부모의 withdraw를 덮어씀"""
        # 잔액 + 한도까지 출금 가능
        if amount > self.balance + self.limit:
            print(f"한도초과(최대{self.balance + self.limit:,}원)")
            return
        self.balance = self.balance - amount

    def show(self):
        """출력 형식 바꾸기"""
        if self.balance < 0:
            print(f"{self.owner}님의 잔액 : {self.balance:,}원 (마이너스)")
        else:
            print(f"{self.owner}님의 잔액 : {self.balance:,}원")


ca = CreditAccount("이영희", 10000, 500000)
ca.withdraw(30000)  # 잔액보다 많은 금액이지만 한도 내의 금액이므로 성공
ca.show()
ca.withdraw(100000)  # 한도 초과
ca.show()

# 자식 클래스에 같은 이름의 메서드가 있으면 그게 우선!


# --------------------------------------------------------
# 같은 이름, 다른 동작
# --------------------------------------------------------

# 상속의 진짜 장점
# 여러 종류의 계좌를 같은 방식으로 다룰 수 있다!
# 각자 알아서 자기 방식대로 동작하기 때문

accounts = [
    Account("김철수", 50000),
    SavingAccount("이영희", 100000, 0.03),
    CreditAccount("박민수", 10000, 30000),
]

print("전체 계좌 현황")
for a in accounts:
    a.show()  # 각자 자기 방식대로 출력

print("[모두 20000원씩 출금 시도]")
for a in accounts:
    a.withdraw(20000)  # 각자 규칙대로 처리
    a.show()


# 같은 코드로 세 종류의 계좌를 다룬 상황
# a.withdraw(20000) 한 줄인데
# 일반계좌는 잔액 확인, 마이너스 통장은 한도가 확인되었음
# -> 각자 자기 방식대로 동작
# -> 이것을 '다형성'이라고 부른다!


# --------------------------------------------------------
# 사실 우리는 계속 클래스를 사용해왔다
# --------------------------------------------------------

# 클래스를 오늘 처음 배웠다고 생각할 수 있지만
# 사실 계속해서 사용해 온 것

# 파이썬의 거의 모든 것이 객체!

# "안녕".upper()  -> 문자열 객체의 메서드
# [1, 2, 3].append(4)  -> 리스트 객체의 메서드
# {"a":1}.get("a")  -> 딕셔너리 객체의 메서드
# Path("data").mkdir()  -> Path 객체의 메서드

# 점(.)을 찍고 무엇인가를 호출했다면 그건 전부 객체의 메서드를 호출한 것!

# 이미 쓰고 있던 객체들

text = "hello world"
print("  문자열 객체:", type(text).__name__)
print("    text.upper()      =", text.upper())
print("    text.split()      =", text.split())
print("    text.replace()    =", text.replace("world", "python"))

nums = [3, 1, 2]
print("\n  리스트 객체:", type(nums).__name__)
nums.append(4)
print("    append 후         =", nums)
nums.sort()
print("    sort 후           =", nums)

info = {"name": "김철수"}
print("\n  딕셔너리 객체:", type(info).__name__)
print("    info.get('name')  =", info.get("name"))
print("    info.keys()       =", list(info.keys()))

""" 전부 '객체.메서드()' 형태입니다.
    누군가 str 클래스, list 클래스를 만들어 뒀고
    우리는 그걸 가져다 쓰고 있었던 것
"""


# --------------------------------------------------------
# 처음 보는 객체를 탐색하는 법
# --------------------------------------------------------

# pandas, numpy 등을 배울 때 이런 코드들을 마주하게 될 것

# df = pd.read_csv("파일.csv")
# df.head()
# df.groupby("부서").mean()

# df가 무엇인지 확인하는 방법
# type(df)  -> 무슨 클래스인지
# dir(df)   -> 무엇을 할 수 있는지 목록
# help(df.head) -> 특정 메서드 설명

sa = SavingAccount("최지은", 100000, 0.05)
print("무엇을 출력하는가? type(sa) -> ", type(sa).__name__)
print("무엇을 하는가? dir(sa) ->")
methods = []
for name in dir(sa):
    if not name.startswith("_"):  # 밑줄로 시작하는 것은 내부용
        methods.append(name)
print(methods)
print("이 메서드는 무엇을 하는가? help() ->")
print(SavingAccount.add_interest.__doc__)

# pandas를 배울 때에도 동일
# type(df)  <- DataFrame 클래스
# dir(df) <- head, groupbym sum 등 가능
# help(df.groupby)  <- groupby의 사용법


# --------------------------------------------------------
# 클래스를 만들지 않아도 사용하는 것 가능
# --------------------------------------------------------

# 중요!

# pandas나 numpy를 쓸 때 우리는 클래스를 만들지 않고 쓰기만 함

# df = pd.read_csv("파일.csv")  <- 다른 사람이 만든 클래스로 객체 생성
# df.head() <- 다른 사람이 만든 메서드 사용

# 그래서 클래스를 직접 만들지 않더라도 pandas는 사용 가능

# 다만 이번에 배울 내용을 알고 있으면
# - df가 왜 점을 찍고 호출하는지
# - 왜 df.sort_values()는 원본을 변경하지 않는지
# - 왜 어떤 것은 ()를 붙이고 어떤 것은 붙이지 않는지
# 등의 것들이 이해된다


# --------------------------------------------------------
# 속성과 메서드 구분
# --------------------------------------------------------

sa = SavingAccount("정하늘", 50000, 0.02)

# 속성은 괄호 없이 그냥 값
print("속성 - 괄호 없음")
print("sa.onwer = ", sa.owner)
print("sa.balance = ", sa.balance)
print("sa.rate = ", sa.rate)

# 메서드는 괄호를 붙임 (실행)
print("메서드 - 괄호 있음")
print("sa.show()")
print(sa.show())
# 괄호를 작성하지 않으면 실행되지 않고 '함수 자체'가 나옴
# pandas에서도 동일

# 값을 그냥 꺼내오면 속성
# 무엇인가를 실행하면 메서드


# --------------------------------------------------------
# 객체지향과 캡슐화
# --------------------------------------------------------

# 객체지향이란
# 지금까지 배운 방식을 '객체지향 프로그래밍'이라고 부름

# [프로그램을 나누는 두 가지 방식]
# 1) 절차지향
#    - '무엇을 할 것인가'를 중심으로 나눈다
#    - 기능(함수) 단위로 쪼갠다
#    - deposit(account, amount)
#    - withdraw(account, amount)
#    - show(account)
#    - 데이터 따로, 기능 따로
# 2) 객체지향
#    - '무엇이 있는가'를 중심으로 나눈다
#    - 대상(객체) 단위로 쪼갠다
#    - 계좌를 예로 들면 계좌는 잔액을 가지고 있고 입금 및 출금이 가능
#    - 데이터와 기능이 한 덩어리

# 둘 중 더 좋은 것이 있는 것이 아니라 상황에 따라 다른 것!
# 단순한 계산, 짧은 스크립트  -> 함수로 충분
# 여러 대상이 각자 상태를 가짐   -> 객체지향이 편리

# 앞서 만든 my_tools.py의 to_int, get_average 같은 것들은
# 객체로 만들 이유가 굳이 없음 (값을 넣으면 결과만 나오기 때문)

# 반대로 계좌 100개, 학생 30명 처럼 각자 다른 상태를 가진 것이 여러개라면 객체지향이 편리

# 절차지향 '무엇을 할 것인가' -> 기능(함수) 단위로 나눔
# 객체지향 '무엇이 있는가'  -> 대상(객체) 단위로 나눔

# [객체지향의 4가지 특징]
# 캡슐화 : 데이터를 안전하게 감싸기
# 상속 : 기존 것을 돌려받기
# 다형성 : 같은 이름 다른 동작
# 추상화 : 복잡한 것을 단순하게 보여주기


# --------------------------------------------------------
# 캡슐화 - 캡슐화가 필요한 이유
# --------------------------------------------------------

# acc["balance"] = -9999

# withdraw 함수에 잔액 확인 로직을 넣어두었는데도
# 딕셔너리를 직접 건드는 경우에는 소용이 없었음
# 클래스로 만들어도 같은 문제가 발생

acc = Account("김철수", 10000)

# 메서드를 통하면 검증이 됨
acc.withdraw(50000)
print("메서드로 출금 시도 후 잔액 : ", acc.balance)

# 하지만 속성을 직접 건드리면 검증을 건너뜀
acc.balance = -9999
print("직접 바꾼 뒤 잔액 : ", acc.balance)

# withdraw 안의 잔액 확인이 아무런 소용이 없는 상황 발생
# 이러한 상황을 방지하는 것이 캡슐화
# 캡슐로 감싸듯 데이터를 안에 넣고 정해진 통로(메서드)로만 접근하게 하는 것!
# 알약을 손으로 아무 데나 담지 않고 캡슐에 넣는 것과 같은 원리로 이해
# 꺼내려면 정해진 방법으로 꺼내야 함!


# --------------------------------------------------------
# 언더 스코어(_) 한 개 - 약속으로 막기
# --------------------------------------------------------

# 파이썬에서는 속성을 완전히 숨기는 기능이 존재하지 않음
# 대신 관례가 존재!

# self.balance  <- 누구나 써도 되는 값
# self._balance <- '내부용이니 건드는 것 금지'라는 표시

# 밑줄 하나는 기술적으로는 접근이 되지만, 개발자들끼리의 약속으로 건드리지 않는다
# 대신 값을 읽고 쓰는 메서드를 따로 만들어준다


class SafeAccount:
    """캡슐화 1단계 - 언더스코어(_) 한 개"""

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # 언더 스코어 사용

    def get_balance(self):
        """잔액을 읽는 통로"""
        return self._balance

    def deposit(self, amount):
        """입금하는 통로(검증 포함)"""
        if amount <= 0:
            print("입금액은 0보다 커야 합니다.")
            return
        self._balance = self._balance + amount

    def withdraw(self, amount):
        """출금하는 통로(검증 포함)"""
        if amount > self._balance:
            print("잔액 부족")
            return
        self._balance = self._balance - amount


sa1 = SafeAccount("이영희", 10000)
sa1.deposit(5000)
print("입금 후 잔액 : ", sa1.get_balance())
sa1.deposit(-3000)  # 잘못된 입금 -> 막힘
print("음수 입금 시도 후 : ", sa1.get_balance())
sa1.withdraw(50000)  # 잔액 부족 -> 막힘
print("초과 출금 시도 후 : ", sa1.get_balance())

# 하지만 언더스코어를 사용한 변수라면 기술적으로 막지 못함
sa1._balance = -999
print("직접 건드린 후 : ", sa1.get_balance(), " <- 여전히 변경 가능")

# 밑줄은 하나의 '약속'일 뿐이기 때문에 직접 건드리는 것을 막을 수는 없음!
# 그러나 코드를 읽는 사람이 '이것을 건드리면 안 된다'고 알 수 있고
# VS Code에서 자동완성 목록에도 잘 뜨지 않음


# --------------------------------------------------------
# 언더스코어(__) 두 개 - 실제로 막기
# --------------------------------------------------------

# 언더 스코어를 두 개 붙이면 파이썬이 이름을 변경
# 밖에서 원래 이름으로 접근 불가능

# self.__balance
# '맹글링'이라고 부름


class SafeAccount2:
    """캡슐화 2단계 - 언더스코어(__) 두 개"""

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # 언더 스코어 사용

    def get_balance(self):
        """잔액을 읽는 통로"""
        return self.__balance

    def deposit(self, amount):
        """입금하는 통로(검증 포함)"""
        if amount <= 0:
            print("입금액은 0보다 커야 합니다.")
            return
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        """출금하는 통로(검증 포함)"""
        if amount > self._balance:
            print("잔액 부족")
            return
        self.__balance = self.__balance - amount


sa2 = SafeAccount2("박민수", 10000)
sa2.deposit(5000)
print("정상 입금 후 : ", sa2.get_balance())

# 직접 접근 시도
try:
    print(sa2.__balance)
except AttributeError as e:
    print("직접 접근 시도 -> 에러 발생")
    print(" -> ", e)

# 이렇게 해도 원래 값은 변하지 않음
sa2.__balance = -999
print("강제로 대입한 뒤 get_balance() : ", sa2.get_balance())

# 언더스코어 두 개를 붙이면 파이썬이 이름을 변경하기 때문에 밖에서 __balance라고 호출해도 찾지 못함
# 다만 이것이 완전한 보완 장치가 아님에 주의!
# 방법을 알면 우회할 수 있는 것
# 파이썬을 '믿고 쓰자'는 프로그래밍 언어이므로 강제로 막지 않음

# 실무에서는 언더스코어 하나를 더 많이 사용
# 언더스코어 두 개는 이름 충돌을 피해야 할 때 더 많이 사용


# --------------------------------------------------------
# property - 메서드를 속성처럼 쓰기
# --------------------------------------------------------

# get_balance()처럼 메서드를 부르는 것이 번거로울 수 있음
# @property를 사용하면 메서드를 속성처럼 사용하는 것 가능!
# 괄호 없이 호출하면서 검증은 그대로 동작

# @로 시작하는 것들을 '데코레이터'라고 부름
# 함수 위에 붙여서 성질을 바꾸는 표시라고 이해


class SafeAccount3:
    """캡슐화 3단계 - property"""

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance  # 언더 스코어 사용
        # 밑줄 있음 - 진짜 값을 담는 곳

    @property
    def balance(self):
        """읽을 때 실행 (괄호 없이)"""
        return self._balance

    # 밑줄 있음 - 진짜 값을 꺼냄

    @balance.setter
    def balance(self, value):
        """쓸 때 실행 (여기서 검증할 수 있음)"""
        if value < 0:
            print("잔액은 음수가 될 수 없습니다.")
            return
        self._balance = value

    def deposit(self, amount):
        self.balance = self.balance + amount  # setter를 거침

    def withdraw(self, amount):
        self.balance = self.balance - amount  # setter가 음수를 막아줌


sa3 = SafeAccount3("최지은", 10000)
print("잔액 읽기 (괄호 없이) : ", sa3.balance)
sa3.deposit(5000)
print("입금 후 : ", sa3.balance)
sa3.withdraw(50000)  # setter가 막아줌
print("초과 출금 시도 후 : ", sa3.balance)
sa3.balance = -100  # 직접 대입해도 막힘
print("음수를 직접 대입 후 : ", sa3.balance)


# --------------------------------------------------------
# 추상화 - 복잡한 걸 단순하게
# --------------------------------------------------------

# 추상화는 '안이 어떻게 돌아가는지 몰라도 쓸 수 있게 하는 것' 이다

# 자동차를 예로 들어보자
# 운전할 때 엔진이 어떻게 동장하는지 알지 못해도 됨
# 핸들, 페달, 기어만 알면 운전이 가능

# 우리가 만든 클래스도 마찬가지
# acc.deposit(5000)을 쓰는 사람은 안에서 어떤 검증을 하는 지 알지 못해도 괜찮음

# 사실 우리는 계속 추상화된 것을 사용해왔다
# "안녕".upper()나 dr.groupby("부서")등이 내부에서 어떻게 동작하는지 알지 못해도 괜찮음

# 좋은 클래스는 밖에서 봤을 때 단순!
# 복잡한 것은 안에 숨기고, 필요한 것만 보여준다!


class Coffee:
    """커피 머신 (사용하는 사람은 make()만 알면 됨)"""

    def __init__(self, water=1000, beans=200):
        self._water = water
        self._beans = beans

    def _heat_water(self):
        """내부 동작 1. 물 끓이기"""
        return "물을 90도로 데우기"

    def _grind_beans(self):
        """내부 동작 2. 원두 갈기"""
        return "원두를 곱게 갈기"

    def _extract(self):
        """내부 동작 3. 추출"""
        return "9기압으로 추출"

    def make(self):
        """커피 만들기 (이것만 알면 됨)"""
        steps = [self._heat_water(), self._grind_beans(), self._extract()]
        self._water = self._water - 150
        self._beans = self._beans - 18
        return steps


machine = Coffee()

print("쓰는 사람 입장 : ")
print("machine.make() <- 이 한 줄이면 끝")

print()
print("실제 내부 동작")

for step in machine.make():
    print(" - ", step)

# make()를 사용하는 사람은 _heat_water나 _extract를 몰라도 괜찮다
# 밑줄이 붙어 있으므로 '내부용'인 것을 파악만 하면 됨
# 밖으로 보여줄 것과 안에 숨길 것을 나누는 것이 추상화!


# --------------------------------------------------------
# 객체 지향의 4가지 특징
# --------------------------------------------------------

# [캡슐화]
# - 데이터를 안에 감추고 정해진 통로로만 접근하게 한다
# - _balance, __balance, @property
# - 아무나 값을 망가뜨리지 못하게 막는다

# [상속]
# - 기존 클래스의 기능을 물려받아 새 클래스 생성
# - class SavingAccount(Account)
# - 중복을 제거하고 확장하기 용이하도록

# [다형성]
# - 같은 이름의 메서드가 클래스마다 다르게 동작
# - account.withdraw()가 계좌 종류마다 다름
# - 여러 종류를 같은 코드로 다룰 수 있다

# [추상화]
# - 복잡한 내부를 숨기고 필요한 것만 보여준다
# - machine.make() 한 줄이면 커피가 나온다
# - 쓰는 사람이 편해진다
