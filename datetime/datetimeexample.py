import datetime
import calendar #library for calendar
import pytz #library for timezone
#prints today's date
#print(datetime.date.today())

#print(datetime.date.timetuple())

#print(datetime.datetime.now()) # give date and time of now.

# dm = datetime.date.today()

# print(dm.strftime('%d,%m,%Y')) # prints date in format day, month, year

# bdtime = datetime.date(2020,11,21)
# total_data = bdtime - dm
# print(total_data.days)

# print(dm.weekday()) # Monday 0 Sunday 6

# print(dm.isoweekday()) # Monday 1 Sunday 7

# dftm = datetime.timedelta(days=7) # gives the time diffrence

#print(dm-dftm) # gives 7 days before from today

#it prints the all the timezones available
for tz in pytz.all_timezones:
    print(tz)