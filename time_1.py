import datetime

# Get the current date
today = datetime.datetime.now()

# Get the number of days since the start of the year
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1

# Print the result
print(day_of_year+10)