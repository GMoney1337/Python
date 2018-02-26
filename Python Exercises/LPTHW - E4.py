"""
EXAMPLE ERROR:
Traceback (most recent call last):
  File "ex4.py", line 8, in <module>
    average_passengers_per_car = car_pool_capacity / passenger
NameError: name 'car_pool_capacity' is not defined

The error occurred because an extra underscore was added between 'car' and
'pool' that was not originally there
"""
#Sets variable 'cars' equal to 100
cars = 100
#Sets space_in_a_car equal to 4.0
space_in_a_car = 4.0
#Sets drivers equal to 30
drivers = 30
#Sets passengers equal to 90
passengers = 90
#Sets cars_not_driven equal to cars minus drivers
cars_not_driven = cars - drivers
#Sets cars_driven equal to drivers
cars_driven = drivers
#Sets carpool_capacity equal to cars_driven * space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#Sets average_passengers_per_car to passengers divided by cars_driven
average_passengers_per_car = passengers / cars_driven

#Prints "There are 100 cars available"
print("There are", cars, "cars available.")
#Prints "There are only 30 drivers available"
print("There are only", drivers, "drivers available.")
#Prints "There will be 70 empty cars today."
print("There will be", cars_not_driven, "empty cars today.")
#Prints "We can transport 120 people today"
print("We can transport", carpool_capacity, "people today.")
#Prints "We have 90 to carpool today"
print("We have", passengers, "to carpool today.")
#Prints "We need to put about 3 in each car"
print("We need to put about", average_passengers_per_car, "in each car")
