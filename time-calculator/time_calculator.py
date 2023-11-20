import re

def add_time(start, duration, optional_arg=None):

    # Split times into hours and minutes for calculations
    def split_time(time):
        split = re.split(":| ", time) # split strings by : or space
        hours = int(split[0])
        mins = int(split[1])
        period = split[2] if len(split) > 2 else None  # AM OR PM - handles durations without AM or PM
        if period == "PM": # Convert start time to 24h time
            hours += 12
        return [hours, mins]

    # Define hours and mins for calculations
    start_hours, start_minutes = split_time(start) 
    duration_hours, duration_minutes = split_time(duration) 
 
    # Add start and duration minutes together and divmod to get quotient hours and remainder minutes
    minute_addition_quotient, minute_addition_remainder = divmod(start_minutes + duration_minutes, 60) 

    # Account for single digit minutes to give final minutes in a string
    if minute_addition_remainder < 10:
        final_minutes = "0" + str(minute_addition_remainder)
    else:
        final_minutes = str(minute_addition_remainder)

    # Add duration hours, minute_addition_quotient hours, and start hours to get total hours
    total_hours = start_hours + minute_addition_quotient + duration_hours

    # Divmod total hours to get quotient days and remainder hours
    hour_addition_quotient, hour_addition_remainder = divmod(total_hours, 24) # days = quotient, hours = remainder
    days_later = hour_addition_quotient
    
    # Determine whether final hour lands on 12AM
    if hour_addition_remainder == 0:
        final_hours = 24
    else:
        final_hours = hour_addition_remainder
    
    # Determine whether 
    if 12 <= final_hours < 24:
        final_period = " PM"
        if final_hours != 12:
            final_hours -= 12
    else:
        final_period = " AM"
        if final_hours == 24:
            final_hours = 12
    
    
    # Determine day after addition of times
    days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    if optional_arg == None:
        final_day = "" # If no day is given as a third argument, no final day is returned
    else:
        start_day = optional_arg.lower().capitalize() # If a day is given define here
        try:
            day_index = days_of_week.index(start_day)  # Find the index of the provided day
            final_day = ", " + days_of_week[(day_index + days_later) % 7]
        except ValueError:
            final_day = "Invalid day"
    
    
        
    if days_later == 0:
        string_days_later = ""
    elif days_later == 1:
        string_days_later = " (next day)"
    else:
        string_days_later = " (" + str(days_later) + " days later)"
    
    

    
    return str(final_hours) + ":" + final_minutes + final_period + final_day + string_days_later
    
print(add_time("11:40 AM", "0:25"))
        

    