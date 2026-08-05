# 아이템 리스트
my_bag = ["낡은 검", "빨간 포션", "시민의 옷"]

# 새로운 아이템 획득
item_name = input("아이템 이름 : ")
item_price = int(input("아이템 가격 : "))

my_bag.append(item_name)
print(my_bag)

rank = "초보 모험가"

# 조건
if (item_price >= 10000) or (len(my_bag) >= 4):
    rank = "상급 모험가"


# 최종 출력
print(f"판정된 모험 등급 : {rank}")
print(f"업데이트된 최종 가방 상태 : {my_bag}")
print(f"첫번째 아이템 : {my_bag[0]}, 마지막 아이템 : {my_bag[-1]}")
