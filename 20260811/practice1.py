# 1. 체온 판정기
print("1번")
temps = [36.5, 38.2, 35.1, 37.0, 39.1]
def temp_state(temp):
    if temp >= 37.5:
        return "발열"
    elif 36.0 <= temp < 37.5:
        return "정상"
    else:
        return "저체온"
for i in temps:
    print(f"{i} -> {temp_state(i)}")

# 2. 가격에 부가세 붙이기
print("2번")
products = {"노트북": 1200000, "마우스": 25000, "키보드": 45000}
def buga(price):
    return round(price * 1.1)
def total_p(products):
    total = 0
    for price in products:
        price =  products[i]
        bu_price = buga(price)    # <- 이거 안쓰는 법 길어도 좋으니 더 단순
        total += bu_price
    return total
for i in products:
    print(f"{i} : {buga(products[i])}")
print(f"총합 : {total_p(products)}")


# 3. 글자수세기
print("3번")
sentences = ["안녕 하세요", "파 이 썬 좋 아", "hello world"]
#공백없애는함수
new_st = []
def del_blank(line):
    new_st = line.replace(" ", "")
    return new_st
def new_len(line):
    new_st = del_blank(line)
    return len(new_st)
for i in range(len(sentences)):
    print(f"{sentences[i]} -> {new_len(sentences[i])}")


# 4. 안전한 숫자 변환
print("4번")
raw = [" 100 ", "50", "", "삼십", "3.5"]
#문자열->숫자(공백빼야됨)->근데실패하면0
def change_num(text):
    text = text.replace(" ", "")
    if text.isdigit():
        return int(text)
    else:
        return 0
total = 0
for i in raw:
    total = total + change_num(i)
print(total)


# 5. 최댓값 직접 만들기
print("5번")
#숫자입력받아서그중에최댓값만찾으면됨
new_nstring = input("숫자 입력 : ").split()
def max_num(nstring):
    new_nstring = sorted(nstring)
    if new_nstring == []:
        return None
    else:
        return new_nstring[-1]
print(f"최댓값 : {max_num(new_nstring)}")

# 6. 평균과 등급
students = {

    "김철수": [90, 85, 100],

    "이영희": [70, 95, 70],

    "박민수": [80, 85, 90],

}
#   get_average(scores) : 리스트의 평균 (소수 첫째 자리 반올림)
#   get_grade(score)    : 점수 -> 등급 (90이상 A, 80이상 B, 70이상 C, 나머지 D)
def get_avg(scores):
    return round(sum(scores) / len(scores), 1)
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"
for i in students:
    print(f"{i} 평균 {get_avg(students[i])} 등급 {get_grade(get_avg(students[i]))}")




# 7. 급여 계산기
print("7번")
workers = [

    {"이름": "김철수", "기본급": 3000000, "초과시간": 5},

    {"이름": "이영희", "기본급": 3500000, "초과시간": 0},

]
#   get_overtime_pay(hours) : 초과근무수당 (시간당 20000원)
#   get_tax(amount)         : 세금 (총액의 10%, 정수)
#   get_final_pay(base, hours) : 실수령액
#                             = (기본급 + 초과수당) - 세금
def get_overtime_pay(hours):
    return hours * 20000
def get_tax(amount):
    return int(amount * 0.1)
def get_final_pay(base, hours):
    total_m = base + get_overtime_pay(hours)
    return total_m - get_tax(total_m)
for i in workers:
    print(f"{i['이름']} : 기본급 {i['기본급']}, 초과 {i['초과시간']} -> 실수령 {get_final_pay(i['기본급'], i['초과시간'])}")


# 8. 비밀번호검사
print("8번")
#   is_long_enough(pw)  : 8자 이상인가
#   has_number(pw)      : 숫자가 들어있는가
#   has_letter(pw)      : 영문자가 들어있는가
#   check_password(pw)  : 셋 다 만족하면 "안전",
#                         아니면 부족한 조건을 알려주는 문자열
def is_long_enough(pw):
    if len(pw) >= 8:
        return True
    else:
        return False
def has_number(pw):
    if not any(ch.isdigit() for ch in pw):
        return False
    else:
        return True
def has_letter(pw):
    if not any(ch.isalpha() for ch in pw):
        return False
    else:
        return True
def check_password(pw):
    if not is_long_enough(pw):
        return "8자 이상이어야 합니다"
    if not has_number(pw):
        return "숫자를 포함해야 합니다"
    if not has_letter(pw):
        return "영문자를 포함해야 합니다"
    return "안전"

while True:
    pw = input("비밀번호 입력 : ")
    result = check_password(pw)
    if result == "안전":
        print("안전")
        break
    else:
        print(result)



# 9. 별점 시각화
print("9번")
# 함수 두 개를 만드세요.
#   make_star(score)     : 점수(0~5)를 별 문자열로. 예) 3 -> "★★★☆☆"
#   show_review(name, score) : "상품명  ★★★☆☆ (3)" 형태로 출력
#                              (make_star 를 불러서 쓸 것)
reviews = {"노트북": 4, "마우스": 5, "키보드": 2}
def make_star(score):
    bs = 5 - score
    return ("★" * score) + ("☆" * bs)
def show_review(name, score):
    print(f"{name} {make_star(score)} ({score})")
for i in reviews:
    show_review(i, reviews[i])



# 10. 재고 관리
print("10번")
stock = {}
def add_stock(stock, name, count):
    if name in stock:
        stock[name] += count
    else:
        stock[name] = count
    return stock
def remove_stock(stock, name, count):
    if count > stock[name]:
        print(f"재고 부족: {name} (요청 {count}, 보유 {stock[name]})")
    else:
        stock[name] -= count
    return stock
def show_stock(stock):
    print("[재고 현황]")
    for i in stock:
        print(f"{i}: {stock[i]}개")
stock = add_stock(stock, "마우스", 10)
stock = add_stock(stock, "키보드", 5)
stock = remove_stock(stock, "마우스", 3)
stock = remove_stock(stock, "키보드", 10)
stock = add_stock(stock, "모니터")


# 11. 문자열 뒤집기와 회문 판정
print("11번")
words = ["level", "기러기", "python", "Never odd or even"]
def reverse_text(s):
    result = ""
    for i in s:
        result = i + result #읽은거뒤에앞에꺼붙임
    return result
#1회차에ㅣ 2회차에 e+l 3회차에 v+el
#1회차에p 2회차에 y+p 3회차에 t+yp 
def is_palindrome(s):
    s = s.replace(" ", "")
    s = s.lower()
    if s == reverse_text(s):
        return True
    else:
        return False
print(reverse_text("hello"))
for i in words:
    if is_palindrome(i):
        print(f"{i} -> 회문입니다")
    else:
        print(f"{i} -> 회문이 아닙니다")


# 12번. 단어개수 세기
print("12번")
# 함수를 만드세요.
#   count_words(text) : 단어별 등장 횟수를 딕셔너리로 돌려준다
#                       (소문자로 통일, 공백으로 구분)
#
# 그리고 가장 많이 나온 단어를 찾는 함수도 만드세요.
#   most_common(counter) : 가장 많이 나온 단어와 횟수를 함께 반환
#                          (return 단어, 횟수  -> 받을 때 w, c = most_common(...))

text = "Python is fun Python is easy Python"
def count_words(text):
    new_t = text.lower().split() #일단소문자로다바꾸고띄어쓰기기준으로자름
    cw = {}
    for word in new_t:
        if word in cw:
            cw[word] += 1
        else:
            cw[word] = 1
    return cw
def most_common(counter):
    max_word = ""   #제일많이나온단어
    max_count = 0   #제일많이나온단어의횟수초기값일단은
    for word in counter:
        if counter[word] > max_count:
            max_word = word
            max_count = counter[word]
    return max_word, max_count
cw = count_words(text)
print(cw)
w, c = most_common(cw)
print(f"가장 많이 나온 단어: {w} ({c}회)")



# 13. 계좌 입출금
print("13번")
balance = 10000
def withdraw(balance, amount):
    if amount > balance:
        print(f"잔액 부족 (요청 {amount}, 잔액 {balance})")
        return balance
    else:
        return balance - amount
def deposit(balance, amount):
    return balance + amount
balance = withdraw(balance, 3000)
print("출금 3000 -> 잔액", balance)
balance = deposit(balance, 5000)
print("입금 5000 -> 잔액", balance)
balance = withdraw(balance, 20000)
print("최종 잔액:", balance)




# 14. 장바구니(원본을 지키는 함수)
print("14번")
cart1 = ["사과"]
new_cart = cart1.copy()
def add_item(new_cart, name):
    new_cart.append(name)
    return new_cart
def remove_item(new_cart, name):
    if name not in new_cart:
        print("없는 상품입니다: ", name)
    else:
        new_cart.remove(name)
    return new_cart
#   장바구니1: ['사과']
print("장바구니1: ", new_cart)
#   장바구니2: ['사과', '우유']
add_item(new_cart, "우유")
print("장바구니2: ", new_cart)
#   장바구니3: ['사과', '우유', '빵']
add_item(new_cart, "빵")
print("장바구니3: ", new_cart)
#   없는 상품입니다: 라면
remove_item(new_cart, "라면")
#   장바구니4: ['사과', '빵']
remove_item(new_cart, "우유")
print("장바구니4: ", new_cart)
#   원본 확인 - 장바구니1: ['사과']
print("원본 확인- 장바구니1: ", cart1)


# 15. 원본을 지키는 함수
print("15번")
# 15. 원본을 지키는 함수
print("15번")
og = [3, 1, 2]
def sort_bad(data):
    data.sort()
    return data
def sort_good(data):
    new_data = sorted(data)
    return new_data
result = sort_good(og)
print("sort_good 결과 : ", result, "원본 : ", og)
result = sort_bad(og)
print("sort_bad 결과 : ", result, "원본 : ", og)




