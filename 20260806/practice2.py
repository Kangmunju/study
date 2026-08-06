# 실습
# 1. 각 사람 평균
#    민수 평균 :
#    철수 평균 :
# 2. 두 사람 평균
#    두 사람의 평균은 ? 입니다
# 3. 누가 더 우수한 사람인지 출력
#    평균 비교 후 민수 or 철수가 더 우수한 학생입니다.
#

student = [
    {"name": "민수", "국어": 95, "영어": 100},
    {"name": "철수", "국어": 75, "영어": 50},
]

minsu_avg = (student[0]["국어"] + student[0]["영어"]) / 2
chulsu_avg = (student[1]["국어"] + student[1]["영어"]) / 2

print(f"민수 평균 : {minsu_avg}")
print(f"철수 평균 : {chulsu_avg}")

mandc_avg = (minsu_avg + chulsu_avg) / 2
print(f"두 사람의 평균은 {mandc_avg}입니다.")

if minsu_avg > chulsu_avg:
    print("민수가 더 우수한 학생입니다.")
elif minsu_avg < chulsu_avg:
    print("철수가 더 우수한 학생입니다.")
else:
    print("두 학생의 평균이 같습니다.")
