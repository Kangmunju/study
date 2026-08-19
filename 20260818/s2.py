# --------------------------------------------------------
# 클래스(class) - 데이터와 기능을 하나로 묶기
# --------------------------------------------------------

# [클래스가 필요한 이유]
# 데이터가 함수를 따라다님
# 지금까지 배운 방식으로 '은행 계좌' 프로그램을 만들 예정
# 함수와 딕셔너리만 사용한다면

def make_account(owner, balance):
    """계좌를 딕셔너리로 만들기"""
    return {"owner": owner, "balance": balance}

def deposit(account, amount):
    """입금하고 바뀐 계좌를 돌려준다"""
    account["balance"] = account["balance"] + amount
    return account

def withdraw(account, amount):
    """출금하고 바뀐 계좌를 리턴"""
    if amount > account["balance"]:
        print("잔액부족")
        return account
    account["balance"] = account["balance"] - amount
    return account

def show(account):
    """계좌 정보를 출력한다"""
    print(f"{account['owner']}님의 잔액 : {account['balance']:,}원")

acc = make_account("김철수", 10000)
acc = deposit(acc, 5000)
acc = withdraw(acc, 3000)
show(acc)

# deposit(account, amount)
# withdraw(account, amount)
# show(account)

# 모든 함수의 첫 번째 자리에 account가 들어감
# 함수가 5개면 5개 전부, 10개면 10개 전부
# 데이터(account)와 기능(함수)이 항상 붙어 다니므로 매번 같이 넘겨줘야 하는 것!

# 더 큰 문제 - 아무나 값을 바꿀 수 있다
acc2 = make_account("이영희", 10000)
show(acc2)

# withdraw 함수는 잔액을 확인하는데
acc2["balance"] = -99999    #  함수를 거치지 않고 직접 바꿔버림
show(acc2)

# withdraw 함수에 잔액 확인 로직을 넣어놨는데도 딕셔너리를 직접 건드리면 아무 소용이 없음
# 오타 등의 실수가 있으면 Error가 발생하는 대신 새로운 키가 추가






# --------------------------------------------------------
# 해결책 - 데이터와 기능을 한 덩어리로
# --------------------------------------------------------

# 클래스가 이 문제를 해결하는 방법
# 계좌라는 것이 무엇인지 설계도를 만들어 두고
# 거기에 데이터(주인, 잔액)와 기능(입금, 출금)을 함께 넣기
# 그러면 함수를 부를 때 계좌를 매번 넘길 필요가 없음 (함수가 이미 자기 계좌를 알고 있으므로)

class Account:
    """은행 계좌"""
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액 부족")
        self.balance = self.balance - amount
    def show(self):
        print(f"{self.owner}님의 잔액 : {self.balance:,}원")
my_acc = Account("김철수", 10000)
my_acc.deposit(5000)
my_acc.withdraw(3000)
my_acc.show()
# 계좌를 매번 넘기지 않음
# my_acc가 이미 자기 데이터를 알고 있기 때문!







# --------------------------------------------------------
# 클래스를 사용하는 경우
# --------------------------------------------------------

# 물론 모든 것을 클래스로 만들 필요가 없음을 염두에 둔다
# 아래 조건에 해당하면 클래스를 고려할 것!
# 1) 데이터와 기능이 항상 붙어 다니는 경우
#    - 계좌 + 입출금 / 학생 - 성적 계산 / 장바구니 + 담기,빼기
# 2) 같은 종류를 여러 개 만들어야 하는 경우
#    - 계좌 100개 / 학생 30명
# 3) 값이 계속 변하는 경우 (상태를 가짐)
#    - 잔액이 늘었다 줄었다 / 재고가 들어왔다 나갔다

# 함수로 충분한 상항
# - 값을 넣으면 결과만 나오는 단순한 계산
#   ex. 평균 구하기, 부가세 계산, 문자열 뒤집기
# - 한 번 쓰고 마는 작업

# 지금까지 만든 my_tools.py의 함수들을 참고하면
# to_int, get_average, make_bar와 같은 함수들은 클래스로 만들 이유가 없음
# 값을 넣으면 결과만 나오기 때문






# --------------------------------------------------------
# 기본 문법
# --------------------------------------------------------

# 클래스는 설계도, 객체는 실제 물건

# 가장흔한 비유 - 붕어빵 틀
# 클래스 = 붕어빵 틀 (설계도/하나만 있으면 됨)
# 객체 = 붕어빵 (틀로 찍어낸 실제 물건/여러개 가능)

# 붕어빵 틀 자체를 먹을 수 없고 찍어내야 먹을 수 있음
# 클래스도 마찬가지로 만들어서 사용해야 의미가 있다!

# [용어 정리]
# 클래스(class) : 설계도
# 객체(object) : 설계도로 만든 실제 물건
# 인스턴스(instance) : 객체와 거의 같은 말   ex. Account 클래스의 인스턴스
# 속성(attribute) : 객체가 가진 데이터    ex. owner, balance
# 메서드(metod) : 객체가 가진 기능    ex. deposit, withdraw
#                메서드는 '클래스 안에 있는 함수'를 가리킴 (이름만 다를 뿐 함수와 동일)

# 같은 클래스로 계좌 3개를 만들 수 있음
a = Account("김철수", 10000)
b = Account("이영희", 50000)
c = Account("박민수", 3000)
a.show()
b.show()
c.show()
# 3개가 완전히 독립적
# a의 잔액을 바꾸어도 b는 영향을 받지 않음
# 찍어낸 물건은 3개(a, b, c)






# --------------------------------------------------------
# __init__
# --------------------------------------------------------

# __init__은 객체를 만들 때 자동으로 실행되는 함수

# Account("김철수", 10000) <- 이렇게 작성하면 파이썬이 알아서 __init__을 호출
# 우리가 직접 호출하지 않음에 주의!

# __init__이 하는 일
# 객체가 처음 만들어질 때 필요한 값을 채워 넣음
# '이 계좌의 주인은 철수, 잔액은 10000' 라고 정하는 것

class Student:
    def __init__(self, name):
        print(f"__init__ 실행됨! {name}학생 생성")     # self는 자기 자신
        self.name = name
        print(self.name, "생성완료")
        self.scores = []    # 빈 리스트로 시작
print("s1 = Student('김철수') 실행 전")
s1 = Student("김철수")
print("실행 후\n")
print("s2 = Student('이영희') 실행 전")
s2 = Student("이영희")
print("실행 후\n")






# --------------------------------------------------------
# self
# --------------------------------------------------------

# 클래스를 배울 때 가장 헷갈리는 부분
# self는 '이 객체 자기 자신'을 가리킴

# [필요한 이유]
# 계좌가 100개 있다고 가정
# deposit 메서드를 호출할 때 '어느 계좌에 입금할지'를 알아야 함
# a.deposit(5000) -> a에 입금
# b.deposit(5000) -> b에 입금
# 점 앞에 있는 것이 self
# 위 두 예시에서는 a와 b가 self 자리에 들어옴

# [중요 : self는 우리가 넘기지 않는다!]
# def deposit(self, amount) <- 정의할 때는 self를 씀
# a.deposit(5000)을 호출할 때는 self를 쓰지 않음
# 파이썬이 알아서 a를 self 자리에 넣어준다
# 그래서 정의할 때는 인자가 2개인데 호출할 때는 1개!

# [self.balance 와 balance의 차이]
# self.balance : 이 객체의 잔액 (객체가 계속 기억)
# balance : 그냥 지역 변수 (메서드가 끝나면 사라짐)
# 앞서 배운 전역변수와 지역변수의 개념이 여기서도 적용

class Person:
    def __init__(self, name):
        self.name = name
    def who_am_i(self):
        print(f"self는 지금 {self.name}입니다.")
    def compare(self, other):
        """self와 다른 객체를 비교"""
        print(f"나는 {self.name}이고, 상대는 {other.name}입니다.")
p1 = Person("김철수")
p2 = Person("이영희")
p1.who_am_i()   # self 자리에 김철수가 들어감
p2.who_am_i()   # self 자리에 이영희가 들어감
p1.compare(p2)    # self = p1, other = p2





# --------------------------------------------------------
# self를 쓰지 않으면 발생하는 상황
# --------------------------------------------------------

# 초보자가 가장 많이 하는 실수

# 1) 메서드 정의할 때 self를 적지 않은 상황
#    def deposit(amount) <- self가 없음 TypeError!
# 2) 속성 앞에 self를 붙이지 않은 상황
#    def __init__(self, owner):
#         owner = owner   <- self.을 작성하지 않음
#                            지역변수만 만들고 사라짐 (객체에 저장되지 않음)

class Wrong:
    def __init__(self, value):
        value = value   # self.을 작성하지 않음 -> 그냥 지역변수
class Right:
    def __init__(self, value):
        self.value = value
w = Wrong(100)
r = Right(100)
try:
    print("Wrong 객체의 value : ", w.value)
except AttributeError as e:
    print("Wrong 객체의 value : 에러 발생!")
    print(" -> ", e)
    print(" -> self.을 빠트리면 객체에 저장이 되지 않음")
print("Right 객체의 value : ", r.value)





# --------------------------------------------------------
# 메서드는 클래스 안의 함수
# --------------------------------------------------------

# 메서드도 함수와 동일
# - 인자를 받는다
# - return으로 값을 돌려줄 수 있다
# - 기본값을 쓸 수 있다

# 차이점은 첫번째 인자가 self!

class ScoreBook:
    """학생 한 명의 성적을 관리한다"""
    def __init__(self, name):
        self.name = name
        self.scores = []    # 빈 리스트로 시작
    def add(self, score):
        """점수를 추가(return 값 없음)"""
        self.scores.append(score)
    def avg(self):
        """평균을 계산해서 return"""
        if not self.scores:
            return 0
        return round(sum(self.scores) / len(self.scores), 1)
    def grade(self):
        """등급 return"""
        avg = self.avg()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        else:
            return "D"
    def report(self, show_scores=True):
        """성적표 출력 (기본값 인자 사용)"""
        print(f"{self.name}님의 평균 : {self.avg()} 등급 : {self.grade()}")
        if show_scores:
            print(f"점수 : {self.scores}")
book = ScoreBook("김철수")
book.add(90)
book.add(85)
book.add(100)
book.report()
book2 = ScoreBook("이영희")
book2.add(70)
book2.add(75)
book2.add(68)
book2.report()






# --------------------------------------------------------
# 속성은 나중에 바뀔 수 있다
# --------------------------------------------------------
# 메서드는 클래스 안의 함수

# 객체가 가진 값(속성)은 계속 변화
# 이것을 '상태를 가진다' 라고 표현

# 함수를 부르고 나면 아무것도 남지 않지만, 객체는 값을 계속 기억 (가장 큰 차이)

class Counter:
    """숫자를 세는 도구"""
    def __init__(self):
        self.count = 0    # 인자 없이 0부터 시작
    def up(self):
        self.count = self.count + 1
    def down(self):
        self.count = self.count - 1
    def reset(self):
        self.count = 0
c1 = Counter()
c2 = Counter()
c1.up()
c1.up()
c1.up()
c2.up()
print("c1의 count : ", c1.count)    # 3
print("c2의 count : ", c2.count)    # 1
c1.reset()
print("c1 초기화 후 : ", c1.count)    # 0
print("c2는 그대로 : ", c2.count)     # 1

# 전역 변수를 배울 때
# count = 0
# def visit(count):
#   return count + 1
# count = visit(count)  <- 매번 주고받아야 함
# 클래스를 사용하면 객체가 알아서 기억!

# c = Counter()
# c.up()  <- 넘길 필요가 없음







# --------------------------------------------------------
# 속성에 직접 접근하기
# --------------------------------------------------------

# 객체의 속성은 점(.)으로 읽고 쓸 수 있음
# 읽기 : print(acc.balance)
# 쓰기 : acc.balance = 5000
# 다만 쓰기는 주의 필요
# 메서드를거치지 않으면 검증 로직을 건너뛰게 됨

acc = Account("최지은", 10000)
print("읽기", acc.owner, "/", acc.balance)
# 메서드를 통한 출금 -> 검증됨
acc.withdraw(50000)   # 잔액 부족 메시지가 뜸
# 직접 수정 -> 검증되지 않음
acc.balance = -9999
print("직접 바꾼 뒤 : ", acc.balance)

# 파이썬은 속성을 완전히 숨기는 기능이 존재하지 않음
# 대신 관례가 존재
# self.balance <- 누구나 써도 되는 값
# self._balance <- 내부용이니 건드리지 말라는 표시
#                  밑줄 하나를 앞에 붙여서 작성
# 밑줄이 있어도 기술적으로는 접근이 가능
# 약속일 뿐이지만 지키는 것을 권장