# Exercise 2.2.1
# The volume of a sphere with radius r is 4/3*πr**3. What is the volume of a sphere with radius 5?
import math


def volume_calculation(radius):
    volume = 4 / 3 * math.pi * radius ** 3
    print(f"The volume of a sphere with radius {radius} is {volume}.")


volume_calculation(5)

# Exercise 2.2.2
# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy
# and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

price = 24.95
discount = 0.6
shipping_first = 3
shipping_additional = 0.75


def total_cost(copies):
    cost = (copies * price * discount) + shipping_first + shipping_additional * (copies - 1)
    print(f"The total wholesale cost for {copies} copies is {round(cost, 2)}$.")


total_cost(60)

# Exercise 2.2.3
# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile)
# and 1 mile at easy pace again, what time do I get home for breakfast?
from datetime import timedelta

time_left = timedelta(hours=6, minutes=52)
one_mile = timedelta(minutes=8, seconds=15)
three_miles = 3 * timedelta(minutes=7, seconds=12)
total_time = time_left + 2 * one_mile + three_miles
print(f"You will get home at {total_time} for breakfast.")
