from datetime import datetime,date

today_time=datetime.now().time()
# month=datetime.now().month
# dayd=datetime.now().day
# print(month, " ", dayd)
today_date=datetime.now().date()

print(today_date,"::::", today_time)

dob=date(1998,3,27)
age=(today_date-dob).days
print(age)
years=age//365
# print(years)
# print(24*365,age%365)
months=(age % 365) // 30

print(years,"years and", months, "months")
