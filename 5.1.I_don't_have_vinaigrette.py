# Yiska Levi
import datetime
import random

user_input = input('Enter Two dates\n')
dates = user_input.split(' ')
date_format = "%Y-%m-%d"
try:
    date_obj1 = datetime.datetime.strptime(dates[0], date_format)
    date_obj2 = datetime.datetime.strptime(dates[1], date_format)
    # Define the start and end dates
    start_date = None
    end_date = None
    if date_obj1 < date_obj2:
        start_date = date_obj1
        end_date = date_obj2
    else:
        start_date = date_obj2
        end_date = date_obj2

    # Generate a random number of days between the two dates
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)

    # Add the random number of days to the start date to get the random date
    random_date = start_date + datetime.timedelta(days=random_days)
    # Print the resulting date
    print(random_date.date())
    # Get the abbreviated day of the week from the datetime object
    abbrev_day_of_week = random_date.strftime("%a")
    if abbrev_day_of_week == "Mon":
        print('אין לי ויניגרט!')


except ValueError:
    print("Invalid date")
