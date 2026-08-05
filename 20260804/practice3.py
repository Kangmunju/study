### 보안 시스템

# 받아야 하는 정보
code = input("요원 코드명 입력 : ")
password = int(input("5자리 보안 코드 입력 : "))
rank = input("마스터키 등급(S/A/N 중 하나만 입력 가능) : ")
temperature = float(input("현재 체온 입력(ex. 36.5) : "))
time = int(input("남은 시간(초) 입력(ex. 200) : "))

# 보안 코드 분해
man = password // 10000
chun = (password // 1000) % 10
baek = (password // 100) % 10
sip = (password // 10) % 10
il = password % 10

# 검문 - 복제 코드 판별
# 1차 - 등급별 논리 판정
co_a = (man + chun) >= (sip + il)
co_b = (password % 2 == 0) or (password % 3 == 0)
co_c = baek % 2 != 0

# 변수 초기화
next_step = False
state = None
level = None
need = None
more = None
remain = None

# 0차 검문 - 복제 코드 확인
if man == il and chun == sip:
    print("복제된 코드 감지! 즉시 폐쇄합니다.")

else:
    # 1차 보안 - 등급별 판정
    if rank == "N":
        next_step = co_a and co_b and co_c
    elif rank == "A":
        next_step = co_a and (co_b or co_c)
    elif rank == "S":
        next_step = co_a
    else:
        print("보안 시스템 작동! 침입자를 체포하라!")

    # 2차 보안 - 생체 인식
    if next_step:
        if 36.0 <= temperature <= 37.5:
            state = "정상"
            level = (man * chun) / (sip + 1)

        elif 35.0 <= temperature <= 38.5:
            state = "주의"
            level = (man * chun) / (sip + 1) * 1.5

        else:
            state = "위독"
            level = None

        if state == "위독":
            print("생체 신호 위독! 의무실로 강제 이송합니다. (위험도: 측정 불가)")

        else:
            # 3차 보안 - 시간 제한
            if level >= 50:
                need = 180
            else:
                need = 60

            if time < need:
                more = need - time
                print(
                    f"시간 초과! 문이 다시 잠겼습니다. "
                    f"(부족한 시간: {more // 60}분 {more % 60:02d}초)"
                )

            else:
                remain = time - need
                print(
                    f"[{code}] 서버실 개방! 상태: {state} / "
                    f"위험도: {level:.2f} / "
                    f"잔여 {remain // 60}분 {remain % 60:02d}초"
                )

    elif rank in ("S", "A", "N"):
        print("보안 시스템 작동! 침입자를 체포하라!")
