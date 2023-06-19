def add_time(start, duration):
  start_hour, start_minute, am_pm = start[:-6], start[-5:-3], start[-2:]

  duration_hour, duration_minute = duration.split(':')

  if am_pm == 'PM':
    start_hour = str(int(start_hour) + 12) 

  total_minutes = int(start_hour) * 60 + int(start_minute) + int(duration_hour) * 60 + int(duration_minute)

  days_gone = total_minutes // (24 * 60)
  minute_new = total_minutes % (24* 60)
  hour_new = minute_new // (60)
  minute_extra = minute_new % (60)

  if hour_new < 12:
    am_pm = "AM"
    if hour_new == 0:
      hour_new = 12
  else:
    am_pm = "PM"
    if hour_new > 12:
      hour_new -= 12


  time_new = f"{hour_new}:{minute_extra:02d} {am_pm}"
  if days_gone == 1:
    days_later = "(next day)"
  elif days_gone > 1:
    days_later = f"{days_gone} (days later)"
  else:
    days_later = ""

  time_end = time_new + days_later

  return time_end

print(add_time("10:50 AM", "4:12")) 


  
  
  



