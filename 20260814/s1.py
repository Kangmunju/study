# ---------------------------------------------------------
# 그룹별로 묶기
# ---------------------------------------------------------

# 데이터 분석의 기본 동작

# [하고 싶은 일]
# 부서 별로 인원, 연봉 합계, 평균

# [방법]
# 딕셔너리를 '누적 통'으로 사용
# 처음 보는 부서면 0으로 시작
# 이미 본 부서면 기존 값에 더하기

e_list = [
    {"이름": "홍길동", "부서": "개발", "연봉": 5000},
    {"이름": "김철수", "부서": "개발", "연봉": 4000},
    {"이름": "이영희", "부서": "인사", "연봉": 3500},
    {"이름": "박민수", "부서": "영업", "연봉": 4500},
    {"이름": "최지수", "부서": "영업", "연봉": 5500},
]

dept_total = {}   # {부서 : 연봉합계}
dept_count = {}   # {부서 : 인원 수}
for e in e_list:
    dept = e["부서"]
    pay = e["연봉"]
    # .get(키, 0)은 키가 없으면 0을 돌려줌
    dept_total[dept] = dept_total.get(dept, 0) + pay
    dept_count[dept] = dept_count.get(dept, 0) + 1
print(f"{'부서':<6}{'인원':>4}{'합계':>9}{'평균':>10}")
print(dept_total)
print(dept_count)

for dept in dept_total:
    avg = dept_total[dept] / dept_count[dept]
    print(f"{dept:<6}{dept_count[dept]:>4}{dept_total[dept]:9}{avg:>10.1f}")










# --------------------------------------------------------
# 집계 함수 만들기
#  ---------------------------------------------------------

# 같은 코드를 상품별, 지점별에도 쓸 수 있도록 함수로 뺌

def sum_by(rows, group_key, value_key):
    # group_key 별로 value_key를 합산한 딕셔너리를 돌려줌
    # rows : 딕셔너리 리스트
    # group_key : 묶을 기준의 키 (ex. "부서")
    # value_key : 합산할 값의 키 (ex. "연봉")
    result = {}
    for row in rows:
        key = row[group_key]
        result[key] = result.get(key, 0) + row[value_key]
    return result

def count_by(rows, group_key):
    # group_key 별 개수를 센 딕셔너리를 돌려줌
    result = {}
    for row in rows:
        key = row[group_key]
        result[key] = result.get(key, 0) + 1
    return result