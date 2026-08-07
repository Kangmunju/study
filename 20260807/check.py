# 역삼각형
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# 역구구단
for i in range(9, 0, -1):
    for j in range(9, 0, -1):
        print(f"{i} X {j} = {i * j}")


# 다이아몬드
n = 5
for i in range(1, 2 * n):
    if i <= 5:
        print(" " * (n - i) + "*" * (2 * i - 1))
    else:
        j = n * 2 - i
        print(" " * (n - j) + "*" * (2 * j - 1))

        # 6회차 : 공1 *7 -> i = 6인데 얘로 별 7개
        # 7회차 : 공2 *5 -> i = 7인데 얘로 별 5개
        # 8회차 : 공3 *3 -> i = 8인데 얘로 별 3개
        # 9회차 : 공5 *1 -> i = 9인데 얘로 별 1개
