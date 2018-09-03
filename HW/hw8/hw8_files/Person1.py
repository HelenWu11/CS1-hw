from math import *
class Individuals(object):
    def __init__(self,name='', radius=0, home_universe='', x=0, y=0, dx=0, dy=0, current_universe='', rewards=list()):
        self.name = name
        self.radius = radius       # they are presented as a circle 
        self.home_universe = home_universe  #where does he come from 
        self.x = x        #location x
        self.y = y        #location y
        self.dx = dx      #velocity 
        self.dy = dy      #velocity 
        self.stop = False
        self.only = True 
        self.crash = False
        self.crash_only = True  
        self.edge =False 
        self.points = 0
        self.current_universe = home_universe  
        self.rewards = rewards.copy()  #list [x,y,point,name,from which universe]
                                    # huge problem !!!! that we initialize a list in our argument, when we do in the argument?? different classes would share the same \
                                    # but not copy a new list. 
    
    def __str__(self):
        prt = '{0} of {1} in universe {2}\n    at ({3},{4}) speed ({5},{6}) with {7} rewards and {8} points'.format(self.name,self.home_universe,self.current_universe,self.x,self.y,self.dx,self.dy,0,0)
        #rewards's dictionary does not exist 
        return prt
    
    def move(self): #move 
        self.x += self.dx 
        self.y += self.dy
    
    def judge_stop(self):  # to make sure its velocity and its location in the universe 
        if abs(self.dx) < 10 or abs(self.dy) < 10:
            self.stop = True 
        '''    
        if self.x >= 1000 or self.y >= 1000 or self.x <= 0 or self.y <= 0:
            self.stop = True 
        '''    
        return self.stop
    
    def judge_edge(self):
        if self.x >= 1000 or self.y >= 1000 or self.x <= 0 or self.y <= 0:
            self.edge  = True 
        return self.edge 
    
    #find the treasure they can get 
    def find(self,treasure_list):
        for t in treasure_list:
            copy_t = t.copy()
            x_t = t[0]
            y_t = t[1]
            points_t = t[2]
            name_t = t[3]
            if  sqrt((self.x-x_t)**2+(self.y-y_t)**2)<=self.radius :
                copy_t.append(self.current_universe)
                self.rewards.append(copy_t)
                
                n = len(self.rewards)
                #velocity 
                self.dx = self.dx - (n % 2)* (n/6)*self.dx
                self.dy = self.dy - ((n+1)%2)* (n/6)*self.dy 
                return t
    
    def judge_hit(self,other ):  #to make sure they will hit or not   
        if sqrt((self.x-other.x)**2+(self.y-other.y)**2) <= (self.radius+other.radius):
            return True 
        else:
            return False 
    
    def change_velocity(self):
        n = len(self.rewards)
        if n > 0: 
            treasure_loss = self.rewards.pop(0)
            n = len(self.rewards)
            self.dx = -(self.dx + (n%2)*(n/6)* self.dx)
            self.dy = -(self.dy + ((n+1)%2)*(n/6)*self.dy)        
            return treasure_loss 
        else:
            return None 
        
    #find portals 
    def portals(self, portals):
        for portal in portals:
            #print(portal )
            x_from = portal[0]
            y_from = portal[1]
            name_to = portal[2]
            x_to = portal[3]
            y_to = portal[4]
            if sqrt((self.x-x_from)**2+(self.y-y_from)**2) <= self.radius:
                
                self.current_universe = name_to
                self.x = x_to
                self.y = y_to
                
                return True 
        return False 
    
    
    
    
    #final 
    def get_points(self):  # to calculate the points of their rewards
        self.points = 0 
        for reward in self.rewards: 
            self.points += reward[2]
        return self.points 
    
    def __lt__(self,other):  #make sure the max 
        if self.points < other.points:
            return True  
        else:
            return False           

    def winner(self):  #the winner print 
        x= '{} in universe {}\n'.format(self.name,self.current_universe)
        x+= 'at ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points\nRewards:\n'.format(self.x,self.y,self.dx,self.dy,len(self.rewards),self.points)
        for n in self.rewards : 
            x+= n[3]+'\n'
        return x 
    
    
   