def add_time(start, duration, weekday = ""):

  daysOfWeek = ('Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
  
  hourSplit = start.split(':')
  hours = int(hourSplit[0])
  minSplit = hourSplit[1].split(' ')
  minutes = int(minSplit[0])
  ampm = minSplit[1]

  if(ampm == "PM"):
    hours += 12
  
  splitDuration = duration.split(':')
  hours += int(splitDuration[0])
  minutes += int(splitDuration[1])

  hoursMins = divmod(minutes, 60)
  hours += hoursMins[0]
  minutes = hoursMins[1]
  
  daysHours = divmod(hours, 24)
  days = daysHours[0]
  hours = daysHours[1]

  if(hours < 12):
    ampm = "AM"
  else:
    ampm = "PM"

  if(hours % 12 == 0):
    hours = 12
  else:
    hours %= 12

  if(weekday != ""):
    index = daysOfWeek.index(weekday.title())
    newWeekday = daysOfWeek[(index + days) % 7]  
    ampm += ", " + newWeekday
  
  if(days == 1):
    ampm += " (next day)"
  if(days > 1):
    ampm += " (" + str(days) + " days later)"
  
  new_time = str(hours) + ":" + str(minutes).zfill(2) + " " + ampm
  
  return new_time