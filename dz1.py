from datetime import datetime

def get_days_from_today(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    current_date = datetime.today()
    delta = current_date - date
    return delta.days

date_str = '2022-02-24'
days_difference = get_days_from_today(date_str)
print(days_difference)
