current_hours = 14
current_minutes = 34
current_seconds = 42

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented bt the variables
day = int(60*60*24)
print (day)
current_time_in_sec = int(current_hours)*60*60 + int(current_minutes)*60 + int(current_seconds)
print (current_time_in_sec)
remaining_time = day - current_time_in_sec
print (remaining_time)