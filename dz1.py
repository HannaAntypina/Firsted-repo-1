from datetime import datetime

date = datetime(year=2022, month=2, day=24)
current_date = datetime.now()
delta = current_date - date
print (delta)