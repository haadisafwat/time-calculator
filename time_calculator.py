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

print(add_time("11:55 AM", "3:12"))  # Output: 3:07 PM
print(add_time("9:15 PM", "5:30"))  # Output: 2:45 AM (next day)
print(add_time("11:40 PM", "0:25"))  # Output: 12:05 AM (next day)
print(add_time("2:59 AM", "24:00"))  # Output: 2:59 AM (next day)
print(add_time("11:59 PM", "24:05"))  # Output: 12:04 AM (2 days later)
print(add_time("8:16 PM", "466:02"))

  
  
  



