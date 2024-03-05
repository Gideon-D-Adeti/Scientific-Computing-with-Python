from datetime import datetime, timedelta

def add_time(start, duration, day=""):
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    start_time, am_pm = start.split()
    
    # start_hours, start_minutes = map(int, start_time.split(":"))
    duration_hours, duration_minutes = map(int, duration.split(":"))

    start_dt = datetime.strptime(start_time + am_pm, "%I:%M%p")
    duration_dt = timedelta(hours=duration_hours, minutes=duration_minutes)

    end_dt = start_dt + duration_dt

    new_hours = (end_dt.hour % 12) or 12
    new_minutes = end_dt.minute
    am_pm = "AM" if end_dt.hour < 12 else "PM"

    new_time = ""

    if day:
        day = day.lower()
        start_day_index = days.index(day)
        end_day_index = (start_day_index + (end_dt.day - start_dt.day)) % 7
        new_day = days[end_day_index].capitalize()
        if end_dt.day - start_dt.day == 1:
            new_day_str = "(next day)"
        elif end_dt.day - start_dt.day > 1:
            new_day_str = f"({end_dt.day - start_dt.day} days later)"
        else:
            new_day_str = ""
        
        new_time = f"{new_hours}:{str(new_minutes).zfill(2)} {am_pm}, {new_day} {new_day_str}"
        return new_time.rstrip()
    else:
        if end_dt.day - start_dt.day == 1:
            new_day_str = "(next day)"
        elif end_dt.day - start_dt.day > 1:
            new_day_str = f"({end_dt.day - start_dt.day} days later)"
        else:
            new_day_str = ""
        
        new_time = f"{new_hours}:{str(new_minutes).zfill(2)} {am_pm} {new_day_str}"
        return new_time.rstrip()
    

# Testing
print(add_time('3:00 PM', '3:10'))
# Returns: 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))
# Returns: 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))
# Returns: 12:03 PM

print(add_time('10:10 PM', '3:30'))
# Returns: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
# Returns: 7:42 AM (9 days later)
