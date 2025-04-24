def print_hours():
    for hour in range(0, 24):
        if hour == 0:
            suffix = "Midnight"
        elif hour == 12:
            suffix = "Noon"
        elif hour < 12:
            suffix = "AM"
        else:
            suffix = "PM"
        
        display_hour = hour if hour in [0, 12] else hour % 12
        print(f"{hour:02d}:00 - {display_hour}:00 {suffix}")


print_hours()
