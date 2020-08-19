import datetime

dt = datetime.date.today()

jd = datetime.date(2020,8,30)

dftm = jd - dt
print (f"Your job is going to expire in {dftm.days} days")