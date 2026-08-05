# 4. 중앙값 찾기
a = 7
b = 2
c = 5
if a >= b and a <= c:
    print(a)
elif b >= a and b <= c:
    print(b)
else:
    print(c)


# 5. 안전한 삭제
todo = ["운동", "공부", "청소"]
x = "독서"
if x in todo:
    todo.remove(x)
    print("삭제 완료")
else:
    print("목록에 없습니다")
    print(todo)


# 6. 전반기 vs 후반기
sales = [10, 20, 30, 40, 50, 60]
middle = len(sales) // 2
before = sum(sales[:middle])
after = sum(sales[middle:])
print(before, after)
if after > before:
    print("후반 우세")
elif after < before:
    print("전반 우세")
else:
    print("동일")


# 2. 카나리 배포 자동 롤백 판정
error_rates = [0.4, 0.6, 0.5, 0.3, 0.7, 1.2, 0.9, 1.4, 1.1, 1.0]

# 앞 절반은 배포 전, 뒤 절반은 배포 후
mv = int(len(error_rates) / 2)  # 가운데

before_avg = sum(error_rates[:mv]) / mv  # 배포 전 평균
after_avg = sum(error_rates[mv:]) / mv  # 배포 후 평균

print(f"배포 전 평균: {before_avg}")
print(f"배포 후 평균: {after_avg}")

if "5.0" in error_rates[mv:]:  # 배포 후 구간에 5.0 있으면
    print("ROLLBAEK")
else:
    if before_avg == 0:
        if after_avg >= 0:
            print("HOLD")  # 배포 전 평균이 0이면서 배포 후 평균이 0 초과
        else:
            print("PROMOTE")  # 배포 전 평균이 0이면서 배포 후 평균이 0보다 작
    elif after_avg >= before_avg * 1.5:
        print("ROLLBAEK")
    elif after_avg >= before_avg * 1.2:
        print("HOLD")
    else:
        print("PROMOTE")
