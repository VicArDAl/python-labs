'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

miles = 10
kilometers = miles*1.6

minutes = 30
min_to_hour = minutes*(1/60)
seconds = 30
sec_to_hour = seconds*(1/60)*(1/60)
time = (min_to_hour+sec_to_hour)
speed = kilometers/time
print("his average speed is", speed, "km/h")