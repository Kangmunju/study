## 정보 입력

name = input("이름 : ")
level = int(input("현재 사용자의 레벨 : "))
attack = int(input("현재 사용자의 공격력 : "))

# 방패 소지 여부
shield = input("방패 소지 여부 입력(ex. y/n) : ")
has_shield = shield == "y"

# 입장 자격 심사
if level >= 10 and attack >= 50:
    print("던전 입장 가능!")
else:
    print("입장 자격 미달입니다.")
    print("더 수련하고 오세요")

# 특수 보너스 판별
if has_shield or level >= 30:
    attack *= 1.5
    print("전설의 버프가 발동하여 공격력이 상승!")

# 최종 결과 출력
print(f"{name}님의 최종 레벨은 {level}이고, 최종 전투력은 {attack} 입니다.")
