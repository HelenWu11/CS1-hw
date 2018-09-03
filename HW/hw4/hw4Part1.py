#define a function to get new speed and new altitude
def next_step(g, thrust, altitude, speed):
    acceleration = g - thrust*g
    speed = speed + acceleration
    altitude = altitude - speed
    return (altitude, speed)

#ask input for altitude, g, and fuel
altitude = float(input("Enter starting altitude (meters) => "))
print(altitude)
g = float(input("Enter the gravitational acceleration (m/second^2) => "))
print(g)
fuel = float(input("Enter the total units of fuel => "))
print(fuel)


speed = 0 #speed alayws starts at 0
time = 0
used_fuel = 0
usefuel = 0
speed_list = []
time_list = []
altitude_list = []
used_fuel_list = []

speed_list.append(speed)
time_list.append(time)
altitude_list.append(altitude)
used_fuel_list.append(used_fuel)
print("Time",time,"- Altitude: {:.2f},".format(altitude),"Speed: {:.2f}".format(speed))


#first situation: before the rocket lands and there is still fuel left 
while altitude > 0:
    thrust = float(input("Enter the thrust => "))
    print(thrust)      #If fuel greater than zero  
    if fuel > 0:
        if fuel >= thrust:   
            time += 1
            used_fuel = thrust#fuel used equal to the thrust
            usefuel+=thrust
            fuel -= used_fuel 
            # use max() to make sure altitude won't be negative number  
            (altitude,speed) = (max(next_step(g,thrust,altitude,speed)[0],0),\
                        next_step(g,thrust,altitude,speed)[1])
            #putting spped in the first place, so when sort(),the biggest speed will be 
            print("Time",time,"- Altitude: {:.2f},".format(altitude),\
                      "Speed: {:.2f}".format(speed))            
            #at the last one of the list
            speed_list.append(speed)
            time_list.append(time)
            altitude_list.append(altitude)
            used_fuel_list.append(used_fuel)

        
        elif fuel < thrust:
            print("Out of fuel, able to use thrust of {:.2f}".format(fuel))     
            #when thrust is larger than fuel, set thrust equal to the amout of fuel
            thrust = fuel
            usefuel+=thrust 
            used_fuel = thrust
            fuel -= used_fuel
            time += 1
            (altitude,speed) = (max(next_step(g,thrust,altitude,speed)[0],0),\
                    next_step(g,thrust,altitude,speed)[1])    
            print("Time",time,"- Altitude: {:.2f},".format(altitude),\
              "Speed: {:.2f}".format(speed))
            speed_list.append(speed)
            time_list.append(time)
            altitude_list.append(altitude)
            used_fuel_list.append(used_fuel)
            break
        
if fuel == 0:
    #when the fuel left is zero, set thrust equal to zero too 
    used_fuel = 0
    fuel = 0
    while altitude > 0:
        thrust = 0
        used_fuel += thrust
        fuel -= used_fuel
        usefuel = 0
        time += 1
        (altitude,speed) = (max(next_step(g,thrust,altitude,speed)[0],0),\
        next_step(g,thrust,altitude,speed)[1])              
        print("Time",time,"- Altitude: {:.2f},".format(altitude),\
                      "Speed: {:.2f}".format(speed))        
        speed_list.append(speed)
        time_list.append(time)
        altitude_list.append(altitude)
        used_fuel_list.append(used_fuel)    
 
#different situation of the speed when rocket land    
if speed > 2.2:
    print("Crashed ... ")
    print("Kapow ... ")
    print("... All astronauts are now shorter and you owe us a lander... ")

if speed <= 2.2:
    print("Nice landing!")
    print("The world salutes you!")
    

print()
print("Maximum speed of {:.2f}".format(max(speed_list)),\
      "was reached at time",time_list[speed_list.index(max(speed_list))],\
      "and an altitude of {:.2f}.".format(altitude_list[speed_list.index(max(speed_list))]))
print("After that you used {:.2f}".format(usefuel),"units of fuel.")
print("At the end you had {:.2f}".format(fuel-used_fuel),"units of fuel left.")

    