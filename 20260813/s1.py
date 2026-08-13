# --------------------------------------------------------
# 파일 다루기 - 경로부터 CSV까지
# --------------------------------------------------------

# 필요한 도구를 가져오기
# pathilb : 경로를 다루는 도구 (파이썬 기본 내장)
# csv : CSV 파일을 다루는 도구 (파이썬 기본 내장)
# os : 운영체제 관련 도구
# 이 셋은 설치가 필요하지 않음
# import를 사용하면 바로 사용이 가능

from pathlib import Path
import csv 
import os





# --------------------------------------------------------
# 경로란 무엇인가
# --------------------------------------------------------

# 경로(path)는 '파일이 어디 있는 지' 알려주는 주소
# C:\Users\hong\Documents\보고서.txt
# 드라이브  폴더              파일이름

# 2가지 종류

# 1) 절대 경로 - 처음부터 끝까지 전부 적은 것
#               C:\Users\hong\Documents\보고서.txt
#               장점 : 어디서 실행하든 항상 같은 파일을 가리킴
#               단점 : 다른 컴퓨터에서는 사용자 이름이 다르므로 사용 불가

# 2) 상대 경로 - 지금 있는 위치를 기준으로 적은 것
#               data\보고서.txt
#               장점 : 짧은 길이, 편리, 다른 컴퓨터에서도 작동
#               단점 : 지금 있는 위치가 어디냐에 따라 달라짐 <- 이 부분에서 문제 발생

# 대부분 상대경로 사용
# '지금 있는 위치'란? - 초보자가 가장 많이 막히는 지점

# '현재 위치'는 내 파일의 위치가 아닐 수도 있다는 점을 염두
# 파이썬이 "data.txt 열어줘" 라는 말을 들으면 '어느 폴더에서' 찾아야 할 지 선택해야 함
# 그 기준이 되는 곳을 '현재 작업 폴더' 라고 한다!
# current working directory 줄여서 CWD

# 주의할 사항
# 현재 작업 폴더는 '내 .py 파일이 있는 폴더'가 아닐 수 있다!
# VS Code에서 어떤 폴더를 열었는지, 터미널 어느 위치에서 실행했는 지에 따라 달라짐

# 내 파일 위치 : C:\work\project\main.py
# VS Code로 연 폴더 : C:\work     <- project가 아니라 work를 연 것

# 현재 작업 폴더는 C:\work가 된다
# main.py에서 open("data.txt")를 하면 C:\work\data.txt를 찾는다 (project가 아님에 주의)
# 파일이 project에 있으면 찾지 못함!

# 이러한 점 때문에 '분명 파일이 옆에 있는데 없다'고 착각
# 초반에 개념을 제대로 잡지 않으면 나중에 많은 시간을 쏟게 하는 대표적 원인

print("현재 작업 폴더 : ", os.getcwd())     # C:\Users\swrkd\Documents\GitHub\study\20260813
print("이 파일의 위치 : ", Path(__file__).parent)     # C:\Users\swrkd\Documents\GitHub\study\20260813

# 용어 설명
# os.getcwd() : 현재 작업 폴더를 알려줌
# __file__ : 지금 실행중인 .py 파일의 경로, 파이썬이 자동으로 만들어주는 변수, 앞뒤 밑줄 2개 -> '특별한 변수'
# Path(__file__) : 그 경로를 Path 객체로 만든 것, 문자열보다 다루기 편해짐
# .parent : 그 파일이 들어있는 '폴더', 부모(parent) 폴더라는 뜻

# 해결책 : 항상 '이 파일 기준'으로 경로를 잡는다

# ***암기 필요***
# BASE = Path(__file__).parent <- 해당 .py 파일이 있는 폴더
# DATA = BASE / "data" -> 그 안의 data 폴더
# DATA.mkdir(exist_ok=True) -> 없으면 폴더 만들기

# 이렇게 작성하면어디서 실행하든 항상 같은 위치를 가리킴
# 앞으로 파일을 다루는 모든 코드는 이렇게 시작할 것!
# 나중에 pandas로 CSV를 읽을 때에도 동일하게 작성

BASE = Path(__file__).parent    # 이 파일이 있는 폴더
DATA = BASE / "data"    # 그 안의 data 폴더
DATA.mkdir(exist_ok=True)   # 폴더 만들기
print("기준 폴더 : ", BASE)
print("데이터 폴더 : ", DATA)
print("이제 어디서든 항상 같은 위치를 가리킵니다.")

# mkdir 옵션
# DATA.mkdir() : 폴더 생성 -> 이미 있는 경우 FileExistsError 발생!
# DATA.mkdir(exist_ok=True) -> 사용하면 폴더가 이미 있어도 그냥 넘어가고 에러가 발생하지 않음
# DATA.mkdir(parents=True, exist_ok=True) <- 중간 폴더까지 전부 생성
#                                            ex. a/b/c를 만들 때 a, b 또한 없다면 함께 생성






# --------------------------------------------------------
# 윈도우의 역슬래시(\) 문제
# --------------------------------------------------------

# 윈도우 경로는 역슬래시를 씀
#
#   C:\work\data.txt
#
# 그런데 파이썬에서 역슬래시는 '특수 기호'
#
#   \n  줄바꿈
#   \t  탭
#   \\  역슬래시 자체
#
# 그래서 이렇게 쓰면 문제가 생깁니다.
#
#   "C:\work\new.txt"
#         ↑    ↑
#        \w   \n   ← \n 이 줄바꿈으로 해석됨!
#
#   경로가 "C:\work" + 줄바꿈 + "ew.txt" 가 되므로 주의!
#
#
# [해결 방법 3가지]
#
#   ① pathlib 사용           ← 가장 권장
#      Path("C:/work") / "new.txt"
#
#   ② 슬래시(/)로 쓰기
#      "C:/work/new.txt"
#      윈도우도 슬래시를 알아듣습니다
#
#   ③ 문자열 앞에 r 붙이기 (raw string)
#      r"C:\work\new.txt"
#      r 이 붙으면 역슬래시를 특수 기호로 안 봅니다

print("\n" + "=" * 60)
print("역슬래시 함정 직접 보기")
print("=" * 60)

print("  '경로\\new.txt' 를 출력하면:")
print("   >>>", "경로\new.txt")  # \n 이 줄바꿈으로 해석됨
print()
print("  r'경로\\new.txt' 를 출력하면:")
print("   >>>", r"경로\new.txt")  # r 을 붙이면 그대로 나옴

print("""
   위쪽은 줄이 바뀌어 버렸죠? 경로가 깨진 겁니다.

   결론: pathlib 을 쓰면 이런 고민이 필요 없습니다.
    게다가 윈도우/맥/리눅스에서 알아서 맞춰줍니다.
""")







#  ---------------------------------------------------------
# pathlib 으로 경로 다루기
# ----------------------------------------------------------
#
# Path 객체는 슬래시(/)로 이어 붙일 수 있음
# 나눗셈이 아니라 '경로 연결'로 동작
#
#   DATA / "memo.txt"        ->  .../data/memo.txt
#   BASE / "sub" / "a.txt"   ->  .../sub/a.txt

print("\n" + "=" * 60)
print(" 1-5. 경로 조립하고 정보 꺼내기")
print("=" * 60)

file_path = DATA / "memo.txt"  # / 로 이어 붙이기

print("  전체 경로 :", file_path)
print("  파일 이름 :", file_path.name)  # memo.txt
print("  확장자    :", file_path.suffix)  # .txt
print("  이름만    :", file_path.stem)  # memo
print("  상위 폴더 :", file_path.parent)
print("  존재하나? :", file_path.exists())  # 아직 안 만들었으니 False

# [자주 쓰는 Path 기능 정리]
#
#   ── 경로 만들기 ──
#     Path("폴더") / "파일.txt"    경로 이어 붙이기
#
#   ── 정보 꺼내기 ──
#     .name        파일 이름 (확장자 포함)     report.csv
#     .stem        확장자 뺀 이름              report
#     .suffix      확장자                      .csv
#     .parent      상위 폴더
#
#   ── 확인하기 ──
#     .exists()    있는지 확인
#     .is_file()   파일인지
#     .is_dir()    폴더인지
#
#   ── 조작하기 ──
#     .mkdir()     폴더 만들기
#     .rename()    이름 바꾸기 / 옮기기
#     .unlink()    파일 삭제 (되돌릴 수 없음!)







# ---------------------------------------------------------
# 폴더 안의 파일 목록 보기
# ----------------------------------------------------------
#
# 폴더에 쌓인 파일 100개를 한 번에 처리하려면
# 먼저 목록을 가져와야 합니다.
#
#   .iterdir()      폴더 안의 모든 것
#   .glob("패턴")   패턴에 맞는 것만
#
#
# [glob 패턴 규칙]
#
#   *          아무 글자나 0개 이상
#   ?          아무 글자 하나
#
#   *.csv           모든 csv 파일
#   report*         report 로 시작하는 모든 파일
#   *2026*          이름에 2026 이 들어간 파일
#   report_?월.txt   report_1월.txt, report_2월.txt ... (한 글자만)

print("\n" + "=" * 60)
print("파일 목록 다루기")
print("=" * 60)

# 실습을 위해 파일 몇 개를 만들어 둡니다 (내용은 2부에서 자세히)
for name in ["report_1월.txt", "report_2월.txt", "report_3월.txt", "note.md"]:
    with open(DATA / name, "w", encoding="utf-8") as f:
        f.write(f"{name} 의 내용입니다\n")

print("  [data 폴더 전체]")
for p in sorted(DATA.iterdir()):  # sorted 로 이름순 정렬
    print("     ", p.name)

print("\n  [txt 파일만]  glob('*.txt')")
for p in sorted(DATA.glob("*.txt")):
    print("     ", p.name)

print("\n  [report 로 시작]  glob('report*')")
for p in sorted(DATA.glob("report*")):
    print("     ", p.name)

#   실무 활용
#   월별 보고서 100개가 쌓인 폴더에서
#   glob("report_*.csv") 하나로 전부 가져올 수 있습니다.
#   파일 이름을 손으로 100개 적을 필요가 없습니다.

