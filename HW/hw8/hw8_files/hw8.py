from Person import * 
from Universe import *
import json
from math import sqrt

inputfile = input('Input file => ')

print(inputfile)
data=json.loads(open(inputfile).read())

# a list contains all informations from the file
all_universes = []

# a dictionary that use universes as keys, individuals who are in the universes as values
all_individuals = dict()
for dicts in data:
    all_universes.append(dicts)
    if dicts['universe_name'] not in all_individuals:
        all_individuals[dicts['universe_name']] = dicts['individuals']

# pirnt informations of all universes
print('All universes')
print('-'*40)
for n in range(len(all_universes)):
    all_universes[n] = universes(all_universes[n]['universe_name'],all_universes[n]['rewards'],all_universes[n]['portals'])
    print(universes.__str__(all_universes[n]))
    
    
# print informations of all individuals
print('All individuals')
print('-'*40)
players = []
for universes in all_universes:
    for universe in all_individuals:
        if universe == universes.name:
            for individual in all_individuals[universe]:
                individual = person(universe,universe,individual[0],individual[1],individual[2],individual[3],individual[4],individual[5],[],0)
                players.append(individual)

for individual in players:
    print(person.__str__(individual))
    
print()
print('Start simulation')
print('-'*40)

step = 0 # steps count when there are till people moving
stop = [] # list cotains individuals that have stopped
remove_reward = [] # rewards that given back to the origin position when two people crashed
out_of_100 = True
outofedge = []

print(players)
while step < 100: 
    for n in range(len(players)):
        
        if players[n].name in stop:
            continue
        
        if abs(players[n].dx)< 10 or \
           abs(players[n].dy)< 10 or \
           (players[n].x) >= 1000\
                   or (players[n].x) <= 0 \
                   or (players[n].y) >= 1000 \
                   or (players[n].y) <= 0:
            print(players[n].name+' stopped at simulation step '+str(step)+' at location ({:.1f}'.format(players[n].x)+',{:.1f}'.format(players[n].y)+')')
            print()
            stop.append(players[n].name)
            
    
    crashed = [] # list that contains each step whether there are people crash
    count = 0 # count how many people are still moving
    step +=1
    
    for n in range(len(players)): 
        if players[n].name in stop:
            continue
        
        else:              
            if (players[n].x+players[n].dx) < 1000\
               and (players[n].x+players[n].dx) > 0 \
               and (players[n].y+players[n].dy) < 1000 \
               and (players[n].y+players[n].dy) > 0:
                players[n].x += players[n].dx
                players[n].y += players[n].dy
                count += 1                
              
                for universe in all_universes:
                    # see whether the individual is close enough to get an award
                    for reward in universe.rewards:
                        if sqrt((players[n].x-reward[0])**2+(players[n].y-reward[1])**2)<=players[n].radius and players[n].current == universe.name:
                            players[n].rewards.append(reward)
                            remove_reward.append((universe.name,reward[3]))
                            players[n].points += reward[2]
                            players[n].dx = players[n].dx-(len(players[n].rewards)%2)*(len(players[n].rewards)/6)*players[n].dx
                            players[n].dy = players[n].dy-((len(players[n].rewards)+1)%2)*(len(players[n].rewards)/6)*players[n].dy
                            print (players[n].name+' picked up "'+reward[3]+'" at simulation step '+ str(step))
                            universe.rewards.remove(reward)
                            print(person.__str__(players[n]))
                            print() 
                            
                            #if individual's speed is less than 10 then it will stop and no longer move
                            if abs(players[n].dx) < 10 or abs(players[n].dy) < 10:       
                                print(players[n].name+' stopped at simulation step '+str(step)\
                                      +' at location ({:.1f}'.format(players[n].x)+',{:.1f}'.format(players[n].y)+')')
                                print()
                                stop.append(players[n].name) 
                
    for n in range(len(players)):            
        #if the individual is at the edge of the broad, put it into a list
        if ((players[n].x+players[n].dx) >= 1000\
           or (players[n].x+players[n].dx) <= 0 \
           or (players[n].y+players[n].dy) >= 1000 \
           or (players[n].y+players[n].dy) <= 0 )\
           and players[n].name not in stop:                      
            players[n].x += players[n].dx
            players[n].y += players[n].dy    
            outofedge.append(players[n])
    
    
    #if two individuals hit each other,they will drop their first pick up reward and reward will return to where they picked up
    for i in range((len(players))):
        for n in range((len(players))):
            if sqrt((players[i].x-players[n].x)**2+\
                    (players[i].y-players[n].y)**2)\
               <= players[i].radius+players[n].radius and\
               players[i].current == players[n].current and\
               players[i].name != players[n].name and\
               players[i].name not in stop and\
               players[n].name not in stop:
                if players[i].name not in crashed:
                    print(players[i].name+' and '+players[n].name+' crashed at simulation step '+str(step)+ ' in universe '+ players[i].current)
                    
                    crashed.append(players[i].name)
                    crashed.append(players[n].name)
                    
                    if len(players[i].rewards)>0:                  
                        
                        players[i].points -= players[i].rewards[0][2]
                        
                        for reward in remove_reward:
                            if reward[1] == players[i].rewards[0][3]:
                                for universe in all_universes:
                                    if universe.name == reward[0]:
                                        print(players[i].name+' dropped "'+players[i].rewards[0][3]+\
                                              '", reward returned to '+universe.name+\
                                              ' at ('+str(players[i].rewards[0][0])+','+\
                                              str(players[i].rewards[0][1])+')')                      
                                        universe.rewards.append(players[i].rewards[0])
                                        remove_reward.remove(reward)
                                        
                        players[i].rewards.remove(players[i].rewards[0])
                        
                        players[i].dx = -(players[i].dx + (len(players[i].rewards)%2)\
                                          * (len(players[i].rewards)/6)*players[i].dx)
                        players[i].dy = -(players[i].dy + ((len(players[i].rewards)+1)%2)\
                                          * (len(players[i].rewards)/6)*players[i].dy)                
                    
                    
                    if len(players[n].rewards)>0:
                        players[n].points -= players[n].rewards[0][2]
                        
                        for reward in remove_reward:
                            if reward[1] == players[n].rewards[0][3]:
                                for universe in all_universes:
                                    if universe.name == reward[0]:
                                        print(players[n].name+' dropped "'+players[n].rewards[0][3]+\
                                              '", reward returned to '+universe.name+\
                                              ' at ('+str(players[n].rewards[0][0])+','+\
                                              str(players[n].rewards[0][1])+')')
                                                        
                                        universe.rewards.append(players[n].rewards[0])
                                        remove_reward.remove(reward)                        
                        players[n].rewards.remove(players[n].rewards[0]) 
                        
                        players[n].dx = -(players[n].dx + (len(players[n].rewards)%2)\
                                          * (len(players[n].rewards)/6)*players[n].dx)
                        players[n].dy = -(players[n].dy + ((len(players[n].rewards)+1)%2)\
                                          * (len(players[n].rewards)/6)*players[n].dy)                 
                    
                    print(person.__str__(players[i]))
                    print(person.__str__(players[n]))
                    print()
    

    #If an individual comes near the location of a portal, then she moves to a different universe 
    for n in range(len(players)):  
        for universe in all_universes:
            if universe.name == players[n].current and players[n].name not in stop:
                for portal in universe.portals:
                    if sqrt((players[n].x-portal[0])**2+\
                            (players[n].y-portal[1])**2)<= players[n].radius:
                        print(players[n].name+' passed through a portal at simulation step '+str(step))
                        players[n].current = portal[2]
                        players[n].x = portal[3]
                        players[n].y = portal[4]
                        print(person.__str__(players[n]))
                        print()
    
    # print out people that is going to go out of the edge of the board
    for n in range(len(outofedge)):
        if outofedge[n].name not in stop:
            stop.append(outofedge[n].name)
            print(outofedge[n].name +' stopped at simulation step '+str(step+1)+' at location ({:.1f}'.format(outofedge[n].x)+',{:.1f}'.format(outofedge[n].y)+')')
            print()
        
    
    # if no more people is still moving, then the game ends
    if count == 0:
        print()
        print('-'*40)
        print('Simulation stopped at step',step)
        print(count,'individuals still moving')
        print('Winners:')
        
        max_rewards = 0
        winner = ''
        for n in range(len(players)):
            if len(players[n].rewards)>max_rewards:
                max_rewards = len(players[n].rewards)
                winner = players[n].name
        
        for n in range(len(players)):
            if players[n].name == winner:
                print(person.__str__(players[n]))
                print('Rewards:')
                for item in players[n].rewards:
                    print(' '*4 +item[3])
                print()
        
            elif max_rewards == 0 and winner == '':
                print(person.__str__(players[n]))
                print('Rewards:')
                print()
        out_of_100 = False        
        break

# if the step is bigger or equal to 100, then jump out of loop to end the game 
if out_of_100: 
    #list that include people's name who is still moving
    stillmove = []
    for n in range(len(players)):
        if players[n].name not in stop:
            stillmove.append(players[n].name)
    print()
    print('-'*40)
    print('Simulation stopped at step',step)
    indi_still_move = 'individuals still moving: '
    for n in range(len(stillmove)):
        if n != len(stillmove)-1:
            indi_still_move = indi_still_move + stillmove[n] + ', '
        elif n == len(stillmove)-1:
            indi_still_move = indi_still_move + stillmove[n]
    print(count,indi_still_move)
    print('Winners:')
    max_rewards = 0
    winner = ''
    for n in range(len(players)):
        if len(players[n].rewards)>max_rewards:
            max_rewards = len(players[n].rewards)
            winner = players[n].name
    
    for n in range(len(players)):
        # if a winner is exist 
            if players[n].name == winner:
                print(person.__str__(players[n]))
                print('Rewards:')
                for item in players[n].rewards:
                    print(' '*4 +item[3])
                print()
        #if a winner is not exist
            elif max_rewards == 0 and winner == '':
                print(person.__str__(players[n]))
                print('Rewards:')
                print()