class Person():
    def __init__(self,job,radius,home_universe,x,y,dx,dy,code):
        self.job=job
        self.radius=radius
        self.home_universe=home_universe
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.code=code
        self.current_universe=home_universe
        self.rewards=list()
        self.point=0
        self.canMove=True
        
    def __str__(self):
        string='{} of {} in universe {}\n    at ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points'.format(self.job,self.home_universe,self.current_universe,self.x,self.y,self.dx,self.dy,len(self.rewards),self.point)
        return string
    
    #if either speed is below 10, stop move
    def checkSpeed(self,step):
        dx=abs(self.dx)
        dy=abs(self.dy)
        if dx<10 or dy<10:
            self.stopMoving(step)
            
    #return True if there is at least one reward in bag
    def hasReward(self):
        if len(self.rewards)==0:
            return False
        else:
            return True
    
    #add reward into the bag and slow down the speed
    #then check the speed
    def pickReward(self,reward,step):
        self.rewards.append(reward)
        n=len(self.rewards)
        dx=self.dx
        dy=self.dy
        self.dx = dx - (n%2)* (n/6)*dx
        self.dy = dy - ((n+1)%2)* (n/6)*dy     
        self.checkSpeed(step)
        self.point+=reward[2]
        print('{} picked up "{}" at simulation step {}'.format(self.job,reward[3],step))
        print(self)
        print()        
    
    #remove the first reward from the bag
    #speed up and reverse direction
    def dropReward(self):
        reward=self.rewards.pop(0)
        n=len(self.rewards)
        dx=self.dx
        dy=self.dy        
        self.dx = -(dx + (n%2)* (n/6)*dx)
        self.dy = -(dy + ((n+1)%2)* (n/6)*dy)
        self.point-=reward[2]
        return reward
    
    def stopMoving(self,step):
        self.canMove=False
        print('{} stopped at simulation step {} at location ({:.1f},{:.1f})'.format(self.job,step,self.x,self.y))
        print()        
        
    def move(self):
        if self.canMove:
            self.x+=self.dx
            self.y+=self.dy