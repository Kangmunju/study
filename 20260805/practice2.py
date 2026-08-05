# 1. 편차 판단
nums1 = [3, 7, 2, 9, 4]
top1 = max(nums1)
bottom1 = min(nums1)
print(f"{top1 - bottom1}")
if top1 - bottom1 >= 5:
    print("차이가 큽니다")
else:
    print("차이가 작습니다")

nums2 = [10, 12, 11]
top2 = max(nums2)
bottom2 = min(nums2)
print(f"{top2 - bottom2}")
if top2 - bottom2 >= 5:
    print("차이가 큽니다")
else:
    print("차이가 작습니다")


# 2. 학점 계산기
scores1 = [88, 92, 79]
s1_avg = sum(scores1) / len(scores1)
print(f"{s1_avg:.2f}")
if s1_avg >= 90:
    print("A")
elif s1_avg >= 80:
    print("B")
elif s1_avg >= 70:
    print("C")
else:
    print("D")

scores2 = scores = [60, 55, 71]
s2_avg = sum(scores2) / len(scores2)
print(f"{s2_avg:.2f}")
if s2_avg >= 90:
    print("A")
elif s2_avg >= 80:
    print("B")
elif s2_avg >= 70:
    print("C")
else:
    print("D")


# 3. 장바구니 중복 체크
cart1 = ["사과", "우유", "빵"]
item1 = "계란"
if item1 in cart1:
    print("이미 담겨 있습니다")
else:
    cart1.append(item1)
    print(cart1)
