# import datetime 한 이후
# timedelta 없이 날짜 계산하는 함수 만들기

import datetime

w = ["월", "화", "수", "목", "금", "토", "일"]
def date_cal(day):
    date = datetime.datetime.now()    # 날짜 계산
    week = datetime.date.today().weekday()
    return date.day + day, w[(week + day) % 7]


