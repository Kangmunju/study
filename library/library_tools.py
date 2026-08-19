LOAN_DAYS = 14        #기본 대출 기간
FEE_PER_DAY = 100     #연체료 (하루당)
MAX_BOOKS = 5         #1인당 최대 대출 권수

import datetime

def get_due_date(days=LOAN_DAYS):
    """오늘+days 날짜를 리턴"""
    return (datetime.date.today()) + (datetime.timedelta(days=days))

def get_late_fee(late_days, per_day=100):
    return late_days * per_day

if __name__ == "__main__":
    print("library_tools 자체 테스트")