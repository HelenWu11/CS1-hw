radius_sun = input("Enter the radius of the Sun (miles) -> ")
print(radius_sun)
radius_moon = input("Enter the radius of the Moon (miles) -> ")
print(radius_moon)
d1 = input("Enter the maximum distance to the Sun (miles) -> ")
print(d1)
d2 = input("Enter the minimum distance to the Moon (miles) -> ")
print(d2)
rate = input("Enter the rate the Moon is moving away (in/year) -> ")
print(rate)

#Distance_Moon_to_Earth = Distance_Sun_to_Earth*(Radius_of_Moon/Radius_of_Sun)
dm = int(d1) *(int(radius_moon) / int(radius_sun))
d = float(dm) - int(d2)

#5280 feet = 1 mile
#12 inches = 1 foot
year = float(d) /(float(rate) / 12 / 5280)

print("The Moon will have exactly the same apparent size as the Sun when it is", "{0:.2f}".format(dm),"miles away.")

print("The Moon will need to recede another", "{0:.2f}".format(d),"miles")
print("Which will occur in",int(year),"years at the current rate.")
