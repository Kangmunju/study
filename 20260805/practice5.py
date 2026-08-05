# 응용 1. 회문 판별
seq = [1, 2, 3, 2, 1]
if seq == seq[::-1]:  # 리스트 뒤집
    print("True")
else:
    print("False")


# 응용 2. 좌석 예약 시스템
seats = [0, 1, 0, 0, 1]  # 0빈 1예약
n = 2
if n >= len(seats):
    print("없는 좌석입니다")
else:
    if seats[n] == 0:
        print("예약 완료")
        seats[n] = 1
        print(seats)
    else:
        print("이미 예약된 좌석입니다")

print(seats.count(0))


# 응용 3. 삼각형 분류
sides = [3, 4, 5]
n_sides = sorted(sides)  # 가장 긴 변 찾아야 하니까 일단 정렬

if n_sides[2] >= n_sides[0] + n_sides[1]:
    print("삼각형이 아닙니다")
elif n_sides[0] == n_sides[1] and n_sides[1] == n_sides[2]:
    print("정삼각형")
elif n_sides[2] ** 2 == (n_sides[0] ** 2 + n_sides[1] ** 2):
    print("직각삼각형")
elif n_sides[0] == n_sides[1] or n_sides[1] == n_sides[2]:
    print("이등변삼각형")
else:
    print("일반삼각형")
