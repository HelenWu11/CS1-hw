from Person import *
class Universe():
    def __init__(self,name,rewards=list(),portals=list()):
        self.name=name
        
        self.rewards=dict()
        for reward in rewards:
            code=reward[-1]
            self.rewards[code]=reward
        
        self.portals=dict()
        for portal in portals:
            code=portal[-1]
            self.portals[code]=portal
        
    def __str__(self):
        string='Universe: {}({} rewards and {} portals)'.format(self.name,len(self.rewards),len(self.portals))
        string+='\nRewards:'
        for reward in self.rewards.values():
            string+='\nat ({},{})for {} points: {}'.format(reward[0],reward[1],reward[2],reward[3])
        string+='\nPortals:'
        if len(self.portals)==0:
            string+='\nNone'
        else:
            for portal in self.portals.values():
                string+='\n{}:({},{}) -> {}:({},{})'.format(self.name,portal[0],portal[1],portal[2],portal[3],portal[4])

        return string
    
    def addReward(self,reward):
        self.rewards[reward[-1]]=reward      
    
    def removeReward(self,reward):
        self.rewards.pop(reward[-1])
    
