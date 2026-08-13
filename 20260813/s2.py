#  ---------------------------------------------------------
# 파일 쓰기 - open과 with
#  ---------------------------------------------------------

from pathlib import Path

BASE = Path(__file__).parent
DATA = BASE / "data"

# 기본 문법
# with open(경로, 모드, encoding="utf-8") as f:
#     f.write("내용")

# 모드
# r : 읽기(read) -> 파일을 읽기만 함, 기본값
# w : 쓰기(write) -> '파일이 있으면 내용을 전부 지우고' 새로 씀
# a : 추가(append) -> 기존 내용 뒤에 이어 붙임

# w 주의점!
# 중요한 파일을 w로 여는 순간 내용이 전부 사라지고 되돌릴 수 없음!
# 이어 붙이려면 반드시 a를 쓸 것

# encoding="utf-8" 을 반드시 사용할 것!
# 컴퓨터는 글자를 숫자로 저장 -> 이러한 변환 규칙이 '인코딩'
# 규칙이 다양함 ex. utf-8 : 전 세계 표준(한글 가능), cp949 : 옛날 윈도우 한국어 방식
# 쓸 때와 읽을 때 규칙이 다른 경우 글자가 깨지는 상황 발생 -> 항상 utf-8으로 통일!
# encoding을 쓰지 않으면 파이썬이 알아서 정하지만, 윈도우에서는 cp949를 고르는 경우가 있어 문제 발생

# with를 사용하는 이유
# 파일을 열면 반드시 닫아야 한다!
# 닫지 않는 경우 - 다른 프로그램이 그 파일 불가
#                작성한 내용이 저장되지 않는 경우 발생
# with를 사용하면 블록이 끝날 때 자동으로 닫힘 (중간에 에러 발생해도 닫힘)

# with를 쓰지 않는 경우(단, 권장하지 않음)
# f = open(경로, "w", encoding="uft-8")
# f.write("내용")
# f.close()       <- 반드시 파일을 닫을 것!

# as f의 의미
# 열런 파일을 f라는 이름으로 부르겠다는 뜻
# f 대신 다른 이름 사용 가능하나, 간례 상 f를 가장 많이 씀

print("\n" + "=" * 60)
print("2. 파일 쓰기")
print("=" * 60)

memo = DATA/"memo.txt"

with open(memo, "w", encoding="utf-8") as f:
    f.write("1번째 줄 입니다\n")
    f.write("2번째 줄 입니다\n")
    f.write("3번째 줄 입니다\n")
    # print와 달리 write는 자동 줄바꿈을 제공하지 않음!

print(f" '{memo.name}' 파일을 만들었습니다")
print("VS Code 왼쪽 탐색기에서 data 폴더를 열어 확인해 보세요")






#  ---------------------------------------------------------
# 파일 읽기 - 3가지 방법
#  ---------------------------------------------------------

# 1) read() : 파일 전체를 하나의 문자열로
with open(memo, "r", encoding="utf-8") as f:
    content = f.read()
print("방법1. read()")
print(content)
print("자료형 : ", type(content).__name__)
#.__name__ 없이 작성하면 <class 'str'>로 반환
print("파일 전체가 문자열 하나로 들어옵니다")

# 2) readlines() : 줄 단위 리스트로
with open(memo, "r", encoding="utf-8") as f:
    lines = f.readlines()
print("\n방법2. readlines()")
print(lines)
print("각 줄 끝에 \\n이 그대로 붙어 있는 것에 주의!")
# 없애고 싶으면 반복문 + replace 등 작성
print("줄 수 : ", len(lines))

# 3) for문으로 한 줄 씩 <- 실무에서 가장 많이 사용
print("방법3. for문")
with open(memo, "r", encoding="utf-8") as f:
    line_no = 1
    for line in f:
        print(f"{line_no}번째 줄 : {line.strip()}")
        line_no += 1

# 방법 3이 좋은 이유
# 파일이 아무리 커도 한 줄씩만 메모리에 올림
# read()로 큰 용량의 파읽을 읽는 경우 메모리에 용량 전부를 통째로 올려서 컴퓨터가 멈추는 상황 발생 가능

# strip() : 문자열 앞뒤의 공백과 줄바꿈 삭ㄱ제
# .strip() : 앞뒤 모두 삭제
# .lstrip() : 왼쪽(앞)만 삭제
# .rstrip() : 오른쪽(뒤)만 삭제







#  ---------------------------------------------------------
# 이어쓰기 모드 - "a"
#  ---------------------------------------------------------

with open(memo, "a", encoding="utf-8") as f:
    f.write("나중에 추가한 줄\n")
with open(memo, "r", encoding="utf-8") as f:
    print(f.read())
print("""'w'와 'a'의 차이""")
print("w로 열면 기존 내용이 전부 사라지고 새로 작성")
print("a로 열면 기존 내용 뒤에 이어붙임")
# 실무 예시
# 로그 파일에 기록을 쌓을 때 -> a
# 결과 파일을 새로 만들 때 -> w







#  ---------------------------------------------------------
# 파일이 없을 때
#  ---------------------------------------------------------

# 존재하지 않는 파일을 열려고 하면 FileNotFoundError 발생

ghost = DATA / "없는파일.txt"

# 1) 미리 확인
print("방법 1. exist()로 미리 확인")
if ghost.exists():
    with open(ghost, "r", encoding="utf-8") as f:
        print(f.read())
else:
    print(f"{ghost.name}은(는) 없습니다")

# 2) try / except
print("방법 2. try / except")
try:
    with open(ghost, "r", encoding="uft-8") as f:
        print(f.read())
except FileNotFoundError:
    print(f"{ghost.name}을(를) 찾을 수 없습니다")

# 둘 중 보통 2번의 방법을 권장
# 확인하는 순간과 여는 사이에 파일이 사라질 수도 있기 때문
# 권한 문제 등은 exist()로 잡지 못하는 상황이 발생하기도 함
# 다만, '있으면 읽고 없으면 새로 만든다'와 같은 경우라면 exist()로 미리 확인하는 것이 좋음








#  ---------------------------------------------------------
# 안전하게 읽는 함수 만들기
#  ---------------------------------------------------------

def read_text(path, default=""):
    # 파일을 읽어 문자열로 돌려주고 없으면 default 반환
    try:
        with open(path, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        return default

def read_lines(path):
    # 파일을 읽어줄 리스트로 반환(줄바꿈 제거, 없으면 빈 리스트)
    try:
        with open(path, "r", encoding="utf-8") as f:
            result = []
            for line in f:
                result.append(line.strip())
            return result
    except FileNotFoundError:
        return []

# input("리스트를 입력해 주세요 (end 입력시 종료) : ")
# 노래제목 가수 <- 10개 입력
# end 입력시 종료


def write_lines(path, lines):
    # 줄 리스트를 파일로 저장
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line+"\n")
    return path







#  ---------------------------------------------------------
# 여러 파일을 한 번에 처리
#  ---------------------------------------------------------

total_lines = 0
success = 0
failed = []
for p in sorted(DATA.glob("*txt")):
    try:
        lines = read_lines(p)     #한줄씩(리스트로)반환하는함수
        total_lines += len(lines)
        success += 1
        print(f"{p.name} : {len(lines)}줄")
    except Exception as e:
        # 모든 에러를 잡아서 기록 후 다음 파일로
        failed.append(p.name, str(e))
print(f"\n 총 {success}개 파일, {total_lines}줄")
if failed:      # 실패목록이 있으면
    print("실패한 파일 : ")
    for name, reason in failed:
        print(f"{name} : {reason}")

# 핵심 패턴
# for 안에 try를 넣으면 파일 하나가 깨져 있어도 나머지는 정상처리








#  ---------------------------------------------------------
# 파일 정리 - 이름 변경과 삭제
#  ---------------------------------------------------------

temp = DATA / "임시파일.txt"

# 파일 만들기
with open(temp, "w", encoding="utf-8") as f:
    f.write("곧 지워질 파일\n")
print("생성 완료 : ", temp.name)

# 이름 바꾸기
renamed = DATA / "이름변경.txt"
temp.rename(renamed)
print("이름을 바꿨습니다 : ", renamed.name)

# 삭제하기
renamed.unlink()
print("삭제했습니다")
# unlink()는 휴지통을 거치지 않고 곧바로 영구 삭제 -> 복구되지 않음!
# 실무에서는 삭제 코드를 작성하기 전에 경로를 print해서 확인할 것
# 백업을 만들고 그 다음 실행

# rename은 '옮기기'로도 쓸 수 있음
# 단, 대상 폴더가 미리 있어야 한다!






#  ---------------------------------------------------------
# CSV
#  ---------------------------------------------------------

# CSV = Comma Seperated Values(쉼표로 구분된 값)
# 텍스트 파일
# 지금까지 배운 내용으로 열면 내용 전부 확인 가능

# 생긴 모습
# 이름,부서,연봉
# 김철수,영업,4500
# 이영희,개발,5200

# 첫 줄은 보통 '헤더' (열 이름)
# 한 줄이 한건의 데이터 (엑셀에서의 한 행)
# 쉼표가 칸 구분 (엑셀에서의 셀 경계)

# 엑셀 파일과 다른 점
# xlsx : 서식, 수식, 차트, 여러 시트가 들어간 복잡한 압축 파일
#        메모장으로 열면 깨진 글자만 나옴
# csv : 그냥 글자 -> 서식, 수식 존재하지 않음
#       가볍고 어떤 프로그램에서든 읽는 것 가능
# 프로그램끼리 데이터를 주고 받을 때 CSV를 사용
# 엑셀에서도 "다른 이름으로 저장 > CSV"로 생성 가능

e_file = DATA / "e.csv"
rows = [
    "이름,부서,연봉,입사년도",
    "김철수,영업,4500,2019",
    "이영희,개발,5200,2020",
    "박민수,개발,4800,2021",
    "최지은,영업,5100,2018",
    "정하늘,인사,4200,2022"
]
with open(e_file, "w", encoding="utf-8") as f:
    for row in rows:
        f.write(row + "\n")
print(f"-{e_file.name}- 생성 완료")

# 첫 줄은 헤더
with open(e_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
header = lines[0].strip().split(",")
print(header)     # 열 이름

# 2번째 줄부터 데이터
for line in lines[1:]:
    parts = line.strip().split(",")
    print(parts)

# strip()으로 줄바꿈을 매번 지워야함
# lines[1:]처럼 헤더를 직접 건너뛰어야 함
# 모든 값이 문자열 -> 연산이 필요한 경우 각각 int() 변환
# parts[2]처럼 '번호'로 접근해야 함

# 값 안에 쉼표가 포함된 경우 CSV 규칙에서 값을 따옴표로 묶음
# 그러나 split(",")은 따옴표를 이해하지 못한다!
# -> 파이썬에 CSV 모듈이 있는 이유

# csv 모듈의 reader
# 문법
import csv

with open(e_file, "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# newline="" : csv 모듈을 쓸 때의 약속
#              쓰지 않으면 윈도우에서 빈 줄이 하나씩 끼어 들어가는 문제 발생

# split과의 비교
# - strip()을 쓰지 않아도 줄바꿈이 알아서 처리
# - 따옴표 안의 쉼표를 제대로 인식
# - 각 줄이 자동으로 리스트가 됨

# DictReader
# csv.reader는 각 줄을 '리스트'로 준다 ex. row[0], row[1], row[2] ...
# -> 순서를 기억해야 함
# 그러나 csv.DictReader는 각 줄을 '딕셔너리'로 준다! ex. row["이름"], row["부서"] . . .
# -> 읽기 쉽고 열 순서가 바뀌어도 안전
# 첫 줄을 자동으로 헤더 인식하여 키로 사용
with open(e_file, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['이름']} / {row['부서']} / {row['연봉']}만원")

# 한 줄이 실제로 어떻게 생겼는 지 확인
with open(e_file, "r", encoding="utf-8", newline="") as f:
    blank_list = []
    for row in csv.DictReader(f):
        blank_list.append(row)
        print(row)
        print("자료형 : ", type(row).__name__)
print(blank_list)
# 여기서 딕셔너리를 사용하기 위해 지금까지 학습한 것

# CSV의 모든 값은 문자열!
# CSV 파일에는 자료형 정보가 없음 -> 그냥 글자만
# 파이썬은 전부 문자열로 읽어옴
# 계산하려면 반드시 int나 float으로 변환!





# ---------------------------------------------------------
# 읽고 변환하는 함수 만들기
# ---------------------------------------------------------

# 매번 파일 열고 변환하는 코드를 쓰면 번거로움.
# 함수로 만들어 두면 한 줄로 끝난다!

employees_file = DATA / "employees.csv"

def to_int(value, default=0):
    #문자열을 정수로 바꾼다. 실패하면 default 를 돌려준다
    try:
        return int(str(value).strip())
    except (ValueError, TypeError):
        return default

def read_csv(path, encoding="utf-8"):
    #CSV 를 읽어 딕셔너리 리스트로 돌려준다. 없으면 빈 리스트
    rows = []
    try:
        with open(path, "r", encoding=encoding, newline="") as f:
            for row in csv.DictReader(f):
                rows.append(row)
    except FileNotFoundError:
        pass
    return rows

def load_employees(path):
    #직원 CSV 를 읽고 숫자 항목을 변환해서 돌려준다
    rows = read_csv(path)
    for row in rows:
        row["연봉"] = to_int(row["연봉"])
        row["입사년도"] = to_int(row["입사년도"])
    return rows

employees = load_employees(employees_file)

print(f"  {len(employees)}명의 데이터를 읽었습니다")
print("  첫 번째 사람:", employees[0])
print("  연봉의 자료형:", type(employees[0]["연봉"]).__name__, " <- 이제 숫자!")







# ---------------------------------------------------------
# 집계하기 - 합계, 평균, 최대, 최소
# ---------------------------------------------------------

salaries = []
for e in employees:
    salaries.append(e["연봉"])

print("  연봉 목록:", salaries)
print("  인원     :", len(salaries), "명")
print("  합계     :", sum(salaries), "만원")
print("  평균     :", round(sum(salaries) / len(salaries), 1), "만원")
print("  최고     :", max(salaries), "만원")
print("  최저     :", min(salaries), "만원")

# 필터링도 해봅시다
print("\n  [개발팀만]")
for e in employees:
    if e["부서"] == "개발":
        print(f"     {e['이름']} - {e['연봉']}만원")

print("\n  [연봉 5000 이상]")
for e in employees:
    if e["연봉"] >= 5000:
        print(f"     {e['이름']} - {e['연봉']}만원")
