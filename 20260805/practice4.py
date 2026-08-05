# 1. API 지연시간 SLO 리포트
latencies = [
    120,
    95,
    340,
    110,
    88,
    205,
    130,
    99,
    410,
    150,
    102,
    118,
    260,
    91,
    175,
    133,
    108,
    96,
    220,
    145,
]

n_latencies = sorted(latencies)

m_index = len(n_latencies) // 2  # p50

if len(n_latencies) % 2 == 0:
    m_value = (n_latencies[m_index - 1] + n_latencies[m_index]) / 2
else:
    m_value = n_latencies[m_index]

k = round(len(n_latencies) * 0.95)  # p95


if type(k) != int:
    k = round(k)

print(f"p50: {m_value}")
print(f"p95: {n_latencies[k - 1]}")

if n_latencies[k - 1] > 300:
    print("SLO 위반")
elif n_latencies[k - 1] > 200:
    print("주의")
else:
    print("정상")


# 2. 카나리 배포 자동 롤백 판정
error_rates = [0.4, 0.6, 0.5, 0.3, 0.7, 1.2, 0.9, 1.4, 1.1, 1.0]

# 앞 절반 배포 전 뒤 절반 배포 후
mv = int(len(error_rates) / 2)  # 가운데

before_avg = sum(error_rates[:mv]) / mv  # 배포 전 평
after_avg = sum(error_rates[mv:]) / mv  # 배포 후 평

print(f"배포 전 평균: {before_avg}")
print(f"배포 후 평균: {after_avg:.2f}")

if max(error_rates[mv:]) >= 5.0:  # 배포 후 구간에 5.0 이상이 있으면
    print("ROLLBACK")
else:
    if before_avg == 0:
        if after_avg > 0:
            print("HOLD")
        else:
            print("PROMOTE")
    elif after_avg >= before_avg * 1.5:
        print("ROLLBACK")
    elif after_avg >= before_avg * 1.2:
        print("HOLD")
    else:
        print("PROMOTE")


# 3. 서버 로그 알림 등급 판정
logs = [
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "ERROR",
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "ERROR",
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "INFO",
    "INFO",
]

# 에러율 구하기 - 일단 리스트에서 에러 개수 카운트 -> 전체 개수로 나누기
er_ra = (logs.count("ERROR") / len(logs)) * 100
# warn 개수
wa_co = logs.count("WARN")

print(f"총 로그: {len(logs)}")
print(f"ERROR: {logs.count('ERROR')} / WARN: {logs.count('WARN')}")
print(f"에러율: {er_ra}%")
if logs[0] == "ERROR" and logs[1] == "ERROR" and logs[2] == "ERROR":
    print("CRITICAL - 연속 장애 감지")
else:
    if er_ra >= 20:
        print("CRITICAL")
    elif 10 <= er_ra or wa_co >= len(logs):
        print("WARNING")
    else:
        print("HEALTHY")


# 4. 주문 결제 금액 계산 엔진
items = [12000, 8500, 30000, 4500]
grade = "GOLD"
coupon = 5000

# 상품 합계
price = sum(items)


# 등급 합계
if grade == "GOLD":
    discount = int(price * 0.1)  # 골드 할인 금액
elif grade == "SILVER":
    discount = int(price * 0.05)
else:
    discount = price

# 총 할인액
total_discount = discount + coupon

# 총 할인액은 상품 합계의 30%를 넘을 수 없음 넘으면 30%까지
if total_discount > price * 0.3:
    total_discount = int(price * 0.3)

# 할인 적용 후 금액이 30,000원 이상이면 배송비 무료 미만이면 3,000원
if price - total_discount >= 30000:
    delivery = 0
else:
    delivery = 3000

# 최종 결제 금액
total_price = price - total_discount + delivery

print(f"상품 합계: {price}")
print(f"총 할인: {total_discount}")
print(f"배송비: {delivery}")
print(f"최종 결제 금액: {total_price}")


###### 4번 추가 확인

print("*" * 20)
print("다른 케이스 확인 완료했고 4번 두번째 케이스만 출력해서 제출하겠습니다")

items2 = [9000, 6000]
grade2 = "SILVER"
coupon2 = 0

# 상품 합계
price2 = sum(items2)


# 등급 합계
if grade == "GOLD":
    discount2 = int(price2 * 0.1)  # 골드 할인 금액
elif grade == "SILVER":
    discount2 = int(price2 * 0.05)
else:
    discount2 = price2

# 총 할인액
total_discount2 = discount2 + coupon2

# 총 할인액은 상품 합계의 30%를 넘을 수 없음 넘으면 30%까지
if total_discount2 > price2 * 0.3:
    total_discount2 = int(price2 * 0.3)

# 할인 적용 후 금액이 30,000원 이상이면 배송비 무료 미만이면 3,000원
if price2 - total_discount2 >= 30000:
    delivery2 = 0
else:
    delivery2 = 3000

# 최종 결제 금액
total_price2 = price2 - total_discount2 + delivery2

print(f"상품 합계: {price2}")
print(f"총 할인: {total_discount2}")
print(f"배송비: {delivery2}")
print(f"최종 결제 금액: {total_price2}")
