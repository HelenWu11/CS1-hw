class person(object):
    def __init__(self,home_universe,current_universe,name,radius,x,y,dx,dy,rewards = [], points = 0):
        self.universe = home_universe  #the home universe for the person
        self.current = current_universe #the current universe where the person on 
        self.name = name  
        self.radius = radius  #people are present in a circle
        self.x = x  # x location of the person
        self.y = y # y location of the person
        self.dx = dx # velocity
        self.dy = dy # velocity
        self.rewards = rewards #rewards the person got 
        self.points = points # points the person got
    
    def __str__(self):
        # return a string with all informations for the person
        individual = self.name+' of '+ self.universe +\
            ' in universe '+ self.current +\
            '\n'+' '*4 +'at ({:.1f}'.format(self.x)+\
            ',{:.1f}'.format(self.y)+\
            ') speed ({:.1f}'.format(self.dx)+\
            ',{:.1f}'.format(self.dy)+') with '+\
                str(len(self.rewards)) +\
                ' rewards and '+\
                str(self.points) + ' points'

        return individual