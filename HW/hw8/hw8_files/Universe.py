class universes(object):
    
    def __init__(self,name,rewards,portals):
        self.name = name
        self.rewards = rewards  # lists of rewards that the universe contains
        self.portals = portals # lists of portals that the universe cotains
    
    def __str__(self):
        # return a string with all informations of the universe
        universe = "Universe: "+self.name+\
            " ("+str(len(self.rewards))+\
            " rewards and "+str(len(self.portals))+" portals)"+\
            "\n"+"Rewards:"+"\n"
        # for every reward in the universe
        if len(self.rewards)>0:
            for item in self.rewards:
                universe = universe + "at "+"("+ str(item[0])+","+str(item[1])+')'\
                    ' for '+str(item[2])+' points: '+item[3]+'\n'
        elif len(self.rewards)==0:
            universe = universe + 'None'+'\n'
       
       # for every portal in the universe     
        if len(self.portals)>0:
            universe = universe + 'Portals:'+'\n'
            for item in self.portals:
                universe = universe + self.name + ':('+ \
                    str(item[0])+','+str(item[1])+') -> '+ str(item[2])+\
                    ':('+str(item[3])+','+str(item[4])+')'+'\n'
        else:
            universe = universe + 'Portals:'+'\n'+'None'+'\n'
        return universe
        
        
    