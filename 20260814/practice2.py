from pathlib import Path
import csv
BASE = Path(__file__).parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)

orders_file = DATA / "orders.csv"
with open(orders_file, "w", encoding="utf-8", newline="") as f:
    f.write("주문일,시간대,매장,메뉴,분류,수량,단가,포장\n")
    f.write("2026-03-02,오전,강남점,아메리카노,커피,3,4500,N\n")
    f.write("2026-03-02,오후,강남점,카페라떼,커피, 2 ,5000,Y\n")
    f.write("2026-03-02,오전,홍대점,녹차라떼,논커피,1,5500,N\n")
    f.write("2026-03-03,오후,강남점,치즈케이크,디저트,2,6500,Y\n")
    f.write("2026-03-03,오전,부산점,아메리카노,커피,5,4500,N\n")
    f.write("2026-03-03,오후,홍대점,아메리카노,커피,,4500,N\n")
    f.write("2026-03-04,오전,강남점,크로플,디저트,3,6000,Y\n")
    f.write("2026-03-04,오후,부산점,카페라떼,커피,4,5000,N\n")
    f.write("2026-03-05,오전,홍대점,아메리카노,커피,2,4500,Y\n")
    f.write("2026-03-05,오후,강남점,녹차라떼,논커피,3,사천,N\n")
    f.write("2026-03-06,오전,부산점,치즈케이크,디저트,1,6500,N\n")
    f.write("2026-03-06,오후,홍대점,카페라떼,커피,6,5000,Y\n")
# print("orders.csv 준비 완료")
# print("data 폴더에서 직접 열어보고, 이상한 값이 몇 개인지 세어 보세요.\n")

# 1. 파일 읽어서 그대로 출력
print("--- 문제 1 ---")
with open(orders_file, "r", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        print(row)

# 2. 값을 정리하는 함수 만들기
print("\n--- 문제 2 ---")
def clean_number(value):
    try:
        return int(value.strip())
    except ValueError:
        return None
print("clean_number(3) -> ", clean_number("  3  "))
print("clean_number(4500) -> ", clean_number("4500"))
print("clean_number('') -> ", clean_number(""))
print("clean_number(사천) -> ", clean_number("사천"))

# 3. 데이터를 읽고 금액을 계산하는 함수 만들기
print("\n--- 문제 3 ---")
def load_orders(path):
    rows = []
    problem_rows = []
    with open(path, "r", encoding="utf-8", newline="") as f:
        for line_num, row in enumerate(csv.DictReader(f), start=2):
            count = clean_number(row["수량"])
            price = clean_number(row["단가"])
            if count is None:
                problem_rows.append(
                    (line_num, row["메뉴"], f"수량 이상 '{row['수량']}'")
                )
                continue
            if price is None:
                problem_rows.append(
                    (line_num, row["메뉴"], f"단가 이상 '{row['단가']}'")
                )
                continue
            row["수량"] = count
            row["단가"] = price
            row["금액"] = count * price
            rows.append(row)
    return rows, problem_rows
rows, problem_rows = load_orders(orders_file)
print(f"정상 {len(rows)}건 / 문제 {len(problem_rows)}건")
for line_num, menu, reason in problem_rows:
    print(f"{line_num}번째 줄 {menu}: {reason}")
total = 0
for row in rows:
    total += row["금액"]
print(f"전체 매출: {total:,}원")


# 4. 집계 함수 두 개 만들기 (앞에 것 긁어온거라 수정해야됨)
print("\n--- 문제 4 ---")
def sum_by(rows, group_key, value_key):
    # group_key 별로 value_key를 합산한 딕셔너리를 돌려줌
    # rows : 딕셔너리 리스트
    # group_key : 묶을 기준의 키
    # value_key : 합산할 값의 키
    result = {}
    for row in rows:
        key = row[group_key]
        result[key] = result.get(key, 0) + row[value_key]
    return result
def count_by(rows, group_key):
    result = {}
    for row in rows:
        key = row[group_key]
        result[key] = result.get(key, 0) + 1
    return result
#매장별매출합
store_sum = sum_by(rows, "매장", "금액")
print(store_sum)
#매장별주문건수
store_count = count_by(rows, "매장")
print(store_count)


# 5. 매장별 매출과 막대그래프
#문제4번의 썸바이함수사용
#막대그래프출력-1만원당네모하나 "■" * (금액 // 10000)
print("\n--- 문제 5 ---")
for store in store_sum:
    money = store_sum[store]
    sq = "■" * (money // 10000)
    print(f"{store:<6}{money:>10,}원 {sq}")

# 6.분류별 집계표
print("\n--- 문제 6 ---")
group_count = count_by(rows, "분류")   #분류별주문건수
group_sum = sum_by(rows, "분류", "금액")    #분류별매출합
print(f"{'분류':<6}{'건수':>8}{'합계':>12}{'평균':>12}")
print("-" * 38)
for g in group_count:
    count = group_count[g]
    total = group_sum[g]
    avg = total / count
    print(f"{g:<6}{g:>8}{total:>12,}{avg:>12.1f}")

# 7. 조건으로 걸러내기
print("\n--- 문제 7 ---")
#1.포장주문(포장열이"y")의건수와매출합계
#2.오전매출합 오후매출합
po_count = 0    #포장건수
po_sum = 0    #포장매출합
m_sum = 0   #오전매출합
n_sum = 0   #오후매출합
for r in rows:
    if row["포장"] == "Y":
        po_count += 1
        po_sum += row["금액"]
    if row["시간대"] == "오전":
        m_sum += row["금액"]
    if row["시간대"] == "오후":
        n_sum += row["금액"]
print(f"포장주문: {po_count}건, {po_sum:,}원")
print(f"오전 매출: {m_sum:,}원")
print(f"오후 매출: {n_sum:,}원")

# 8. 가장 많이 팔린 메뉴 찾기
print("\n--- 문제 8 ---")
def best_menu(rows):    #가장잘팔리는메뉴찾는함수
    menu_count = sum_by(rows, "메뉴", "수량")
    bm_name = ""
    best_count = 0
    for m in menu_count:
        if menu_count[m] > best_count:
            bm_name = m
            best_count = menu_count[m]
    return bm_name, best_count
menu_count = sum_by(rows, "메뉴", "수량")
print("메뉴별 판매 수량")
for m in menu_count:
    print(f"{m} {menu_count[m]}개")
name, best_count = best_menu(rows)
print(f"가장 많이 팔린 메뉴: {name} ({best_count}개)")


# 9. 결과를 csv로 저장
print("\n--- 문제 9 ---")
group_count = count_by(rows, "매장")
group_sum = sum_by(rows, "매장", "금액")
store_file = DATA / "매장별_매출.csv"   #sig엑셀에서열csv파일
with open(store_file, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["매장", "주문건수", "매출합계"])
    for s in group_sum:
        writer.writerow([
            s,
            group_count[s],
            group_sum[s]
        ])

# 10. 보고서만들기
# csv아니고 그냥텍스트파일
print("\n--- 문제 10 ---")
re_file = DATA / "일일보고서.txt"
s_sum = sum_by(rows, "매장", "금액")    #매장합
group_sum = sum_by(rows, "분류", "금액")  #가게별합
total_c = len(rows)
total_s = 0
for r in rows:
    total_s += r["금액"]
name, best_count = best_menu(rows)
with open(re_file, "w", encoding="utf-8") as f:
    f.write("=" * 30 + "\n")
    f.write("카페 매출 보고서\n")
    f.write("=" * 30 + "\n")
    f.write(f"총 주문: {total_c}건\n")
    f.write(f"총 매출: {total_s}원\n")

    f.write("\n[매장별]\n")
    for s in s_sum:
        f.write(f"{s} {store_sum[s]:,}원\n")
    f.write("\n[분류별]\n")
    for g in group_sum:
        f.write(f"{g} {group_sum[g]:,}원\n")
    f.write(f"\n가장 많이 팔린 메뉴: {name}\n")
    f.write("-" * 30 + "\n")
    f.write(f"처리 실패: {len(problem_rows)}건 (오류목록.csv참고)\n")

with open(re_file, "r", encoding="utf-8") as f:
    print(f.read())






