name = input("Name of robot => ")
print(name)
x_location = int(input("X location => "))
print(x_location)
y_location = int(input("Y location => "))
print(y_location)
ie = 10
ic = ('('+str(x_location)+','+str(y_location)+')')

print("Robot",name,"is at",ic,"with energy:",ie)

while ie<=10:
    command = input("Enter a command (up/left/right/down/attack/end) => ")
    print(command)
    command = command.lower()
    if command == 'up' and y_location != 0 and ie>0:
        y_location -= 10
        ie = min(10,ie+1)
    elif command == 'down' and y_location != 100 and ie>0:
        y_location += 10
        ie = min(10,ie+1)
    elif command == 'right' and x_location != 100 and ie>0:
        x_location += 10
        ie = min(10,ie+1)
    elif command == 'left' and x_location !=0 and ie>0:
        x_location -= 10
        ie = min(10,ie+1)
    elif command == 'attack' and ie>=3:
        ie = min(10,ie-3)
    elif command == 'attack' and ie<3:
        ic = ic
        ie = ie
    elif command == 'up' and y_location == 0 and ie>0:
        ic = ic
        ie = min(10,ie+1)
    elif command == 'down' and y_location == 100 and ie>0:
        ic = ic
        ie = min(10,ie+1)
    elif command == 'left' and x_location == 0 and ie>0:
        ic = ic
        ie = min(10,ie+1)
    elif command == 'right' and x_location == 100 and ie>0:
        ic = ic
        ie = min(10,ie+1)
    
        
    if command == 'up' and y_location != 0 and ie==0:
        ie = min(10,ie+1)
    elif command == 'down' and y_location != 100 and ie==0:
        ie = min(10,ie+1)
    elif command == 'right' and x_location != 100 and ie==0:
        ie = min(10,ie+1)
    elif command == 'left' and ic[0] !=0 and ie==0:
        ie = min(10,ie+1)  
    
    elif command == 'up' and y_location == 0 and ie==0:
        ie = min(10,ie+1)
    elif command == 'down' and y_location == 100 and ie==0:
        ie = min(10,ie+1)
    elif command == 'left' and x_location == 0 and ie==0:
        ie = min(10,ie+1)
    elif command == 'right' and x_location == 100 and ie==0:
        ie = min(10,ie+1)    
        
    elif command == 'end':
        break
    print("Robot",name,"is at",'('+str(x_location)+','+str(y_location)+')',"with energy:",ie)
    