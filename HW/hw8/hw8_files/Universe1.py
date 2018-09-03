class Universes(object):
    
    def __init__(self,name='',rewards = list(), portals = list(),people = list()):
        self.name = name 
        self.rewards = rewards.copy()
        self.portals = portals.copy()
        self.people = people.copy()
        '''
        list of rewarsd. each rewards : x,y ,points(how much you get ),name(the reward's name)
        
        list of portals. each portals: from_x,from_y [the location in local place], to_name[transport universe], to_x,to_y [places you get]
        '''
    
    def __str__(self):
        
        prt='Universe: {} ({} rewards and {} portals)\n'.format(self.name, len(self.rewards), len(self.portals))
        
        prt +='Rewards:\n'
        for i in self.rewards : 
            prt +='at ({},{}) with for {} points : {}\n'.format(i[0],i[1],i[2],i[3])
            
        prt +='Portals:\n'
        if len(self.portals) == 0:
            prt+='None\n'
        else: 
            for i in self.portals: 
                prt+='{}: ({},{}) -> {}: ({},{})\n'.format(self.name,i[0],i[1],i[2],i[3],i[4])
        return prt
    
    def loss(self,treasure_list):
        self.rewards.remove(treasure_list)

    def get(self,treasure):
        self.rewards.append(treasure[0:4])
    
    def loseman(self,man):
        x = list().copy()
        for i in self.people.copy():
            if i[0] != man.name :
                x.append(i)
        self.people = x
    
    def addman(self,man):
        self.people.append([man.name,man.radius,man.x,man.y,man.dx,man.dy])
        
