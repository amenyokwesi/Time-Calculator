def add_time(start, duration,days_of_the_week=None):

days_of_the_week_index ={"monday": 0, "tuesday": 1,"wednesday": 2,"thursday": 3,"friday":4,"saturday":5,"sunday":6}

days_of_the_week_array ={"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}

duration_tuple = duration.partition[":"]
print(duration_tuple)
duration_hours=int(duration_tuple[0])
duration_minutes=int(duration_tuple[2])

start_tuple=start.partition(":")
start_minutes_tuple_sart_tuplr[2].partition(" ")
start_hours=int(starttuple[0])
start_minutes=int(start_minutes_tuple[0])
am_or_pm=start_minutes_tuple[2]
am_and_pm_flip={"AM":"PM":"PM":"AM"}

amount_of_days=int(duration_hours/24)

end_minutes=start_minutes+duration_minutes
if(end_minutes >=60):
  start_hours +=1
  end_minutes=end_minutes %60
  amount_of_am_pm_flips=int((start_hours+duration_hours)/12)
end_hours=(start_hours+duration_hours)%12

end_minutes=end_minutes if end_minutes>9 else "0" str(end minutes)
end_hours=end_hours = 12 if end_hours== 0 else end end hours
if(am_or_pm ="PM" and start_hours(duration_hours % 12)>=):
amount_of_days +=1

am_or_pm=am_or_pm_flip[am_or_pm] if an amount of am_pm_flips %2 == 1 else am_or_pm

returnTime = str(end_hours) + ":" +str(end_minutes)+""am_pm
if(day_of_week):
days_of_the_week=day_of_week.lower()
index =int((days_of_the_week_index[days_of_week]) + amount of days)%7
new_day=days_of_the_week_array[index]
returnTime +=","+new_day

if(amount_of_days==1):
   return returnTime + "" +"(next day)"
 elif(amount_of_days > 1):
    return returnTime + "(" + str(amount_of_days)+ "days later)"
    





return start




main.py
from time_calculator import add_time
from 