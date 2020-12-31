SECS_CONST = 60
KM_CONST = 1.61


# Exercise 1.2.1
# How many seconds are there in 42 minutes 42 seconds?
def minutes_to_seconds(minutes, seconds):
    result = minutes * SECS_CONST + seconds
    print(f"There are {result} seconds in {minutes} minutes and {seconds} seconds.")


minutes_to_seconds(42, 42)


# Exercise 1.2.2
# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile
def kilometers_to_miles(kilometers):
    miles = kilometers / KM_CONST
    print(f"There are {round(miles, 2)} miles in {kilometers} kilometers.")


kilometers_to_miles(10)


# Exercise 1.2.3
# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
# mile in minutes and seconds)? What is your average speed in miles per hour?
def average_pace_and_speed(kilometers, minutes, seconds):
    final_minutes = seconds / SECS_CONST + minutes
    km_to_miles = kilometers / KM_CONST
    result = final_minutes / km_to_miles
    average_speed = SECS_CONST / result
    print(f"If you run {kilometers} kilometers in {minutes} minutes and {seconds} seconds"
          f", your average pace is {round(result, 2)} minutes per mile. Your average speed"
          f" is {round(average_speed, 2)} miles per hour.")


average_pace_and_speed(10, 42, 42)
