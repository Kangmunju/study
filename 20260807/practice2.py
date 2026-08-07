# 11. 글자 세기
text = input("문자열 : ")
t = {}
for i in text:
    if i in t:
        t[i] += 1
    else:
        t[i] = 1
print("11번")
print(t)


# 12. 딕셔너리 뒤집기
# if문으로있으면이름값넣ㄱ
# 없으면점수가키고이름값으로넣
scores = {"철수": 90, "영희": 85, "민수": 90}
s = {}
for i in scores:
    if scores[i] in s:
        s[scores[i]].append(i)
    else:
        s[scores[i]] = [i]
print("12번")
print(s)


# 13. 투표 집계
#   기대 출력: A 4표 (50.0%) 당선 뭔가 딕셔너리로 만들어야될듯
votes = ["A", "B", "A", "C", "B", "A", "C", "A"]
result = {}
for i in votes:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
a = ""
v = 0
for i in result:
    if result[i] > v:
        v = result[i]
        a = i
p = v / len(votes) * 100
print("13번")
print(f"{a} {v}표 ({p:.1f}%) 당선")

# 14. 약수 구하기
print("14번")
n = int(input("숫자: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")


# 15. 소수 판별
print("15번")
n = int(input("숫자: "))
if n < 2:
    print(f"{n}은(는) 소수가 아닙니다.")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} 입력 -> 소수가 아닙니다.")
            break
    else:
        print(f"{n} 입력 -> 소수입니다.")

# 16. 자릿수 합
print("16번")
number = input("숫자: ")
t = 0
d = []
nn = int(number)
for i in range(len(number)):
    d.append(nn % 10)
    nn //= 10
for i in d:
    t += i
print(f"{number} 입력 -> {t}")


# 17. 최대공약수-약수니까작은수로검사하면될듯..????
print("17번")
a = int(input("첫 번째 수: "))
b = int(input("두 번째 수: "))
c = min(a, b)
x = 1
for i in range(1, c + 1):
    if a % i == 0 and b % i == 0:
        x = i
print(f"{a}과 {b} 입력 -> {x}")


# 18. 피보나치 수열
print("18번")
n = int(input("개수: "))
a = 1
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

# 19. 완전수 찾기(1~100)
# 완전수 = 자기 자신을 뺀 약수의 합이 자기 자신과 같은 수?아먼개소리야ㅠㅠ
print("19번")
for i in range(1, 101):
    total = 0
    for j in range(1, i):
        if i % j == 0:
            total += j
    if total == i:
        print(i, end=" ")

# 20. 모음 세기
print("20번")
text = input("문장: ")
count = 0
for i in text.lower():
    if i in "aeiou":
        count += 1
print(f"{text} 입력 -> 모음 {count}개")
