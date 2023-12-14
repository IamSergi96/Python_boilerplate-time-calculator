# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


def add_time(start_time, duration, starting_day=None):
  #convert start_time to minutes from 00:00
  start_parts = start_time.split()
  start_hours, start_minutes = map(int, start_parts[0].split(":"))
  start_period = start_parts[1]
  start_minutes += start_hours * 60  #convert start_time to minutes from 00:00
  if start_period == "PM":
    start_minutes += 12 * 60
  #convert duration to minutes
  duration_hours, duration_minutes = map(
      int, duration.split(":"))  #split time in 00:00
  duration_minutes += duration_hours * 60  #convert duration to minutes
  #sum start_time and duration
  end_minutes = start_minutes + duration_minutes

  #new time in AM/PM format
  end_hours = end_minutes // 60 % 12
  if end_hours == 0:
    end_hours = 12
  end_minutes = end_minutes % 60
  end_period = "AM" if (end_minutes + start_minutes) // 720 % 2 == 0 else "PM"

  #days_later
  days_later = end_minutes // 1440  #minutes per day, so how many days later?
  #in which day are we?
  if starting_day:
    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"
    ]
    starting_day_index = days.index(
        starting_day.lower().capitalize())  #case insensitive
    end_day_index = (starting_day_index + days_later) % 7
    end_day = days[end_day_index]
    if days_later == 1:
      end_day = f"{end_day} (next day)"
    elif days_later > 1:
      end_day = f"{end_day} ({days_later} days later)"
  else:
    end_day = ""
  #return end_time
  result = f"{end_hours}:{end_minutes:02} {end_period}"  #2 digits minutes
  if end_day:
    result += f", {end_day}"
  return result


print(add_time("11:06 PM", "2:02"))

# Run unit tests automatically
main(module='test_module', exit=False)
