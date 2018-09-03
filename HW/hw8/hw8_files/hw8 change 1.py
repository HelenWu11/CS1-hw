from Person1 import *
from Universe1 import * 
import json 


def print_treasure(people,get_treasure):
    print('\n{0} picked up \'{1}\' at simlation step {2}\n{0} of {3} in universe {4}\nat ({5:.1f},{6:.1f}) speed({7:.1f},{8:.1f}) with {9} rewards and {10} points\n'.format(people.name,get_treasure[3],cnt,people.home_universe,people.current_universe,people.x,people.y,people.dx,people.dy,len(people.rewards),get_treasure[2] ))

def print_edge(people,cnt):
    print('{} stopped at simulation {} at location ({:.1f},{:.1f})\n'.format(people.name,cnt,people.x,people.y))
    #print(people.dx,people.dy)

def print_intersection(p1,t1,p2,t2):
    print('{} and {} crashed at simulation step {} in universe {}'.format(p1.name,p2.name,cnt,universe.name))
    if t1  != None:
        print('{} dropped \'{}\', reward returned to {} at ({},{})'.format(p1.name ,t1[3],t1[-1],t1[0],t1[1]))
    if t2 != None:
        print('{} dropped \'{}\', reward returned to {} at ({},{})'.format(p2.name ,t2[3],t2[-1],t2[0],t2[1]))
    print('{} of {} in universe {}\nat ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points'.format(p1.name,p1.home_universe,p1.current_universe,p1.x,p1.y,p1.dx,p1.dy,len(p1.rewards),p1.get_points()))
    print('{} of {} in universe {}\nat ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} point\n'.format(p2.name,p2.home_universe,p2.current_universe,p2.x,p2.y,p2.dx,p2.dy,len(p2.rewards),p2.get_points()))
    

def print_portals(man):
    print('{} passed through a portal at simulation step {}'.format(man.name,cnt))
    print('{} of {} in universe {}'.format(man.name,man.home_universe,man.current_universe))
    print('at ({:.2f},{:.2f}) speed ({:.2f},{:.2f}) with {} rewards and {} points\n'.format(man.x,man.y,man.dx,man.dy,len(man.rewards),man.get_points()))
#input 

if __name__ == "__main__":
    file = 'file3.txt'
    #file = input()
    #print('Input file => file1.txt')
    data = json.loads(open(file).read())
    
    #print(type(data[0])) #every part of the list is a dic 
    #print(data)
    
    uni_dict = dict()
    uni_list = list()
    man_dict = dict()
    man_list = list()
    
    #output_basic_information 
    for universe in data: 
        name = universe['universe_name']
        rewards = universe['rewards']
        portals = universe['portals']
        #print(portals)
        people = universe['individuals']
        word = Universes(name,rewards,portals,people)
        uni_dict[name] = word
        uni_list.append(word)
        
        people = universe['individuals']
        for i in people :
            name_man = i[0]
            radius = i[1]
            x = i[2]
            y = i[3]
            dx = i[4]
            dy = i[5]
            boy = Individuals(name_man,radius,name,x,y,dx,dy,name)
            man_list.append(boy)
            man_dict[boy.name]=boy
            
            
    print('-'*40)
    for i in uni_list:
        print(i)
        print()
    print('\nAll individuals')
    print('-'*40)
    for i in man_list:
        print(i)
        print()   
   
    
    #print('Hello                ',man_dict)
    #print(uni_dict)
            
    #calculation 
    print('\nStart simulation')
    print('-'*40)
    
    
    cnt = 0 
    man_new_list = man_list.copy()
    everyone_stop = False 
    while cnt < 100 and not everyone_stop :
        
        moving = 0 
        everyone_stop = True  
        for people in man_new_list:
            if not people.stop:
                people.move()  #they have moved 
                moving +=1 
                everyone_stop = False
        if not everyone_stop:        
            cnt +=1
        
        man_x_list=list()
        for people in man_new_list: 
            if not people.judge_edge() and not people.judge_stop():
                man_x_list.append(people)
            else:
                print_edge(people,cnt )
                #print(people.dx,people.dy)
        man_new_list = man_x_list.copy()
        
        for people in man_new_list:
            
            #picks up treasure 
            word_treasure = people.current_universe
            list_treasure = uni_dict[word_treasure].rewards 
            get_treasure = people.find(list_treasure)  # return a list of one treasure  
            if get_treasure != None :
                uni_dict[word_treasure].loss(get_treasure) # once get a treasure, the velocity will change 
                
                print_treasure(people,get_treasure)
                if people.judge_stop():
                    print_edge(people,cnt)
                    continue 
            '''
            #check_edge: 
            if people.judge_edge() and people.only  :
                print_edge(people,cnt)
                people.only = False
            '''
            
            #intersection 
            universe = uni_dict[people.current_universe]
            people_list = universe.people
            #print(people_list)
            for people1 in people_list:
                #print(people_list )
                compare  = man_dict[people1[0]]
            
                if compare.name != people.name:
                    if people.judge_hit(compare) and people.crash_only:
                        treasure_lost2 = compare.change_velocity()
                        treasure_lost1 = people.change_velocity()
                        if treasure_lost1 != None:
                            world_from1 = treasure_lost1[-1]
                            uni_dict[world_from1].get(treasure_lost1)
                        if treasure_lost2 != None:
                            world_from2 = treasure_lost2[-1]
                            uni_dict[world_from2].get(treasure_lost2)
                            
                        print_intersection(people,treasure_lost1,compare,treasure_lost2)
                        compare.crash_only = False 
            '''            
            if cnt==5 and  people.name == 'Malware developer':
                print('hello      ',people.current_universe )
            '''            
                    
         
             
            #portal 
            portals_list = universe.portals
            #print(portals_list)
            if people.portals(portals_list):
                #print(people.name)
                new_universe = uni_dict[people.current_universe]
                universe.loseman(people)
                new_universe.addman(people)
                print_portals(people) 


    #final:
    print('-'*40)
    print('Simulation stopped at step',cnt)
    print(moving,'individuals still moving')
    print('Winners:')
    for man in man_list:
        man.get_points()
    print(max(man_list).winner())

