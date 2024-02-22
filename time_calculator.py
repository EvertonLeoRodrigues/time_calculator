def add_time(start, duration, start_day=False):

  """Add a duration of time to a given start time and return the result

  Parameters:
  - start_time (str): The starting time in 12-hour clock format (ending in AM or PM).
  - duration (str): The duration time to be added, indicating the number of hours and minutes.
  - start_day (str, optional): The starting day of the week (case-insensitive). Defaults to None

  Returns:
  new_time (str): A string representing the result time after adding the duration

  The function handles the following scenarios:
  - If the result is on the next day, it appends "(next day)" after the time.
  - If the result is more than one day later, it appends "(n days later)" after the time,
    where "n" is the number of days later.
  - If the optional starting day parameter is provided, the output displays the day of the week of the result.
    The day of the week appears after the time and before the number of days later

  Examples:
  add_time("3:00 PM", "3:10")
  # Returns: "6:10 PM

  add_time("11:30 AM", "2:32", "Monday")
  # Returns: "2:02 PM, Monday

  add_time("11:43 AM", "00:20")
  # Returns: "12:03 PM

  add_time("10:10 PM", "3:30")
  # Returns: "1:40 AM (next day)

  add_time("11:43 PM", "24:20", "tueSday")
  # Returns: "12:03 AM, Thursday (2 days later)

  add_time("6:30 PM", "205:12")
  # Returns: "7:42 AM (9 days later)"
  """ 
  
  start_time, period = start.split()
  
  start_hour, start_minute = map(int, start_time.split(':'))
  duration_hour, duration_minute = map(int, duration.split(':'))
  
  total_hour =  start_hour + duration_hour
  total_minute = start_minute + duration_minute

  if total_minute >=60:
    total_hour += 1
  
  new_minute = total_minute%60
  
  
  days_later = total_hour//24
  new_hour = total_hour%24
  
  new_period = None
  if period == 'AM' and new_hour >= 12:
    new_period = 'PM'
    new_hour %= 12
  elif period == 'PM' and new_hour >= 12:
    new_period = 'AM'
    new_hour %= 12
    days_later += 1
  else:
    new_period = period
  
  if new_hour == 0:
    new_hour = 12
  
  new_time = f'{new_hour}:{new_minute:02d} {new_period}'
  
  if start_day:
    formating_day = start_day.lower().capitalize()
    days_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_index = days_week.index(formating_day)
    new_index = (day_index+days_later)%7
    new_day = days_week[new_index]
    
    new_time+=f', {new_day}'
    
  if days_later == 1:
    new_time += f' (next day)'
  elif days_later > 1:
    new_time += f' ({days_later} days later)'
    
  
  return new_time


