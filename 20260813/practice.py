from pathlib import Path      
BASE = Path(__file__).parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)
top100 = DATA / "top100.txt"    #탑백이라는텍스트파일을만들

def write_lines(path, lines):     #줄리스트파일로저장함수
    try:
        with open(path, "w", encoding="utf-8") as f:
            for line in lines:
                f.write(line + "\n")
            return path
    except FileNotFoundError:
        print("저장할 폴더 X")
        return None

def read_lines(path):     #파일읽고리스트반환없으면빈리스트
    try:
        with open(path, "r", encoding="utf-8") as f:
            result = []
            for line in f:
                result.append(line.strip())
            return result
    except FileNotFoundError:
        print("파일 없음")
        return []

melon = []

while True:
    song = input("노래 제목(end 입력하면 종료!) : ")
    if song == "end":
        break
    if song == "":
        print("노래 제목을 입력하지 않음")
        continue
    name = input("가수 이름 : ")
    if name == "":
        print("가수 이름 입력하지 않음")
        continue
    melon.append(f"{song} - {name}")

write_lines(top100, melon)

