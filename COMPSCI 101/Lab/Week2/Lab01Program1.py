"""
Jaeyoung Hwang (Jeff)

Compleate the program so that it calculates
the number of days, hours and minutes in 65601 munites.
"""



number_of_minutes = 65601
minutes_per_hour = 60
hours_per_day = 24

number_of_hours = number_of_minutes // minutes_per_hour
number_of_day = number_of_hours // hours_per_day

remaining_hours = number_of_hours % hours_per_day
left_over = number_of_minutes % number_of_hours

print(number_of_minutes,"minutes =", number_of_day,"days,",remaining_hours, "hours and", left_over, "minutes")
