# 21. 회문 판별
print("21번")
word = input("단어: ")
check = True
for i in range(len(word)):
    if word[i] != word[len(word) - 1 - i]:
        check = False
        break
if check:
    print(f"{word}입력 -> 회문입니다")
else:
    print(f"{word} -> 회문이 아닙니다")


# 22. 단어 길이별 분류 - 몰라이거..나중
print("22번")
sentence = "I am a student"
w = sentence.split()
r = {}
for i in w:
    if len(i) in r:
        r[len(i)].append(i)
    else:
        r[len(i)] = [i]

print(r)


# 23. 암호화
# ord()문자를아스키
# chr()아스키를문자
print("23번")
text = "abc"
t = list(text)
r = ""
#   기대 출력: bcd
for i in range(len(t)):
    if list[i] == "a":
        r += "z"
    else:
        r += chr(ord(t[i]) + 1)
print(r)


# 24. 직각삼각형
print("24번")
n = int(input("n: "))
for i in range(1, n + 1):
    print("*" * i)


# 25. 역삼각형
print("25번")
n = int(input("n: "))
for i in range(n, 0, -1):
    print("*" * i)

# 26. 오른쪽 정렬 삼각형
print("26번")
n = int(input("n: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

# 27. 숫자피라미드
print("27번")
n = int(input("n: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")  # 줄안바꾸고계속쳐야됨
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()


# 28. 속 빈 사각형
print("28번")
n = int(input("n:"))
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
    print()


# 29. 성적 처리 프로그램
# 각 학생의 총점, 평균, 등급 출력
# 평균 1등
students = {"철수": [90, 85, 77], "영희": [95, 92, 88], "민수": [60, 72, 68]}
max_a = 0
first = ""
for i in students:
    a = sum(students[i]) / len(students[i])
    print(f"{i} 총점 {sum(students[i])} 평균 {a:.1f}", end=" ")
    if a >= 90:
        print("A")
    elif a >= 80:
        print("B")
    elif a >= 70:
        print("C")
    else:
        print("D")
    if a > max_a:
        max_a = a
        first = i
print(f"1등: {first} ({max_a:.1f}점)")

# 30. 장바구니 갱신
menu = {"아메리카노": 4500, "라떼": 5000, "케이크": 6500}
order = ["아메리카노", "케이크", "라떼", "아메리카노"]
# 주문내역을수량과함께정리
# 각항목소개와총액출력
# 총액이만원이상십퍼할인
# 최종금액천단위
c = {}
# c = {'k':'v'}
# c['새로운키'] = '새로운키의 밸류
# 개수
for i in order:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
# 소계총액
total = 0
for i in c:
    price = menu[i] * c[i]
    total += price
    print(f"{i} {c[i]}개 = {price:,}원")
# 합계
print(f"합계: {total:,}원")
# 10%할인
if total >= 20000:
    print("10% 할인 적용")
    total = total * 0.9
# 최종
print(f"최종: {total:,.0f}원")
