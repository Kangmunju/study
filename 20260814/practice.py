from pathlib import Path      
BASE = Path(__file__).parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)
import csv

# 실습용 매출 데이터를 만듭니다 (일부러 지저분하게)
sales_file = DATA / "sales.csv"
with open(sales_file, "w", encoding="utf-8", newline="") as f:
    f.write("날짜,지점,상품,수량,단가\n")
    f.write("2026-01-05,강남,노트북, 3 ,1200000\n")
    f.write("2026-01-05,홍대,키보드,10,45000\n")
    f.write("2026-01-06,강남,마우스,,25000\n")
    f.write("2026-01-06,부산,노트북,2,1200000\n")
    f.write("2026-01-07,홍대,모니터,4,350000\n")
    f.write("2026-01-07,강남,키보드,다섯,45000\n")
    f.write("2026-01-08,부산,마우스,15,25000\n")
    f.write("2026-01-08,홍대,노트북,1,1200000\n")

# sales.csv를 읽어 각 줄의 매출액(수량*단가)을 계산하고
# 정상 데이터 리스트와 문제 목록을 돌려주는 함수 만들기

def load_sales(path):
    rows = []   # 정상 리스트
    problem_rows = []   # 문제 목록
    with open(path, "r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            try:
                count = int(row["수량"])
                price = int(row["단가"])
            except ValueError:
                 problem_rows.append(row)
                 continue
            row["수량"] = count
            row["단가"] = price
            row["매출액"] = count * price
            rows.append(row)
    return rows, problem_rows

rows, problem_rows = load_sales(sales_file)
# for row in rows:
#     print(row)

total = 0
for s in rows:
    total += s["매출액"]
print(f"[정답1] 정상 {len(rows)}건 / 문제 {len(problem_rows)}건")
print(f"전체 매출 : {total:,}원")

# 지점별 매출 합계를 구해 막대그래프 출력
def sum_by(rows, group_key, value_key):
    # group_key 별로 value_key를 합산한 딕셔너리를 돌려줌
    # rows : 딕셔너리 리스트
    # group_key : 묶을 기준의 키 (ex. "지점")
    # value_key : 합산할 값의 키 (ex. "매출액")
    result = {}
    for row in rows:
        key = row[group_key]
        result[key] = result.get(key, 0) + row[value_key]
    return result
# 지점별 매출 합계
branch_sales = sum_by(rows, "지점", "매출액")
# 합계 출력
for branch in branch_sales:
    print(f"{branch} {branch_sales[branch]:,}")


# 상품 별 판매 수량
branch_file = DATA / "지점별매출.csv"
product_count = sum_by(rows, "상품", "수량")
print(product_count)
# 지점별 매출 결과를 'data/지점별매출.csv'로 저장
with open(branch_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    for branch in branch_sales:
        writer.writerow([branch, branch_sales[branch]])

product_count = sum_by(rows, "상품", "수량")
print(product_count)







    



with open(branch_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["지점", "매출액"])

    for branch in branch_sales:
        writer.writerow([branch, branch_sales[branch]])