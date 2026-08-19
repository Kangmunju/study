print("--- 문제 1 ---")
import random
books = ["사피엔스", "코스모스", "총균쇠", "이기적 유전자", "데미안", "토지"]
print("오늘의 추천 도서 : ", random.choice(books)) 
 
print("\n--- 문제 2 ---")
import random as rd
bn = rd.sample(range(1000, 10000), 5)
print("발급된 도서번호: ", bn)

print("\n--- 문제 3 ---")
import datetime
print("대출일 : ", datetime.date.today())
print("반납 예정일 : ", (datetime.date.today()) + (datetime.timedelta(days=14)))

print("\n--- 문제 4 ---")
book_counts = [8, 10, 3, 17]
from math import ceil
print("8권 -> ", ceil(8/4))
print("10권 -> ", ceil(10/4))
print("3권 -> ", ceil(3/4))

print("\n--- 문제 5 ---")
import random, datetime
for i in range(3):
    print(f"[{i+1}] {random.choice(books)} (번호 {random.sample(range(1000, 9999), 1)})")
    print(f"{datetime.date.today()} {(datetime.date.today()) + (datetime.timedelta(days=14))}")

print("\n--- 문제 6 ---")
import library_tools
print("반납 예정일 : ", library_tools.get_due_date())
print("5일 연체료 : ", library_tools.get_late_fee(5, 500))

print("\n--- 문제 7 ---")
import library_tools
print("[대출 규정]")
print("대출 기간 : ", library_tools.LOAN_DAYS)
print("연체료 : ", library_tools.FEE_PER_DAY)
print("최대 대출 : ", library_tools.MAX_BOOKS)

print("\n--- 문제 8 ---")
import library_tools as lt
print("별칭으로 : ", lt.get_late_fee(3), "원")
from library_tools import get_late_fee
print("골라오기로 : ", library_tools.get_late_fee(3), "원")

print("\n--- 문제 9 ---")
print("이 파일의 __name__ : ", __name__)
print("library_tools의 __name__ : ", library_tools.__name__)

print("\n--- 문제 10 ---")
import library_tools
#library_tools안에서쓸수있는것들목록(밑줄시작뺌)
#dir(모듈)(그모듈이가진것들목록) 함수.__doc__(함수아래적은설명)
lt_list  = []
for l in dir(library_tools):
    if not l.startswith("_"):
        lt_list.append(l)   #밑줄시작아닌거만추가
print("사용 가능한 것들 : ")
print(lt_list)
#get_due_date함수설명
print("get_due_date 설명 : ")
print(library_tools.get_due_date.__doc__)