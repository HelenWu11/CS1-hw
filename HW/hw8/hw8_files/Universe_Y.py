class Universe(object):
    def __init__( self,name = '', rewards = [], portal =[] ):
        self.n = name
        self.r = rewards
        self.p = portal
    def __str__(self):
        string = 'Universe:{} ({} rewards and {} portals)'.format(self.n,len(self.r),len(self.p))
        string += '\nRewards:'
        if len(self.r) == 0:
            return string,'\nNone'       
        else:
            for i in range(len(self.r)):
                string += '\nat ({},{}) for {} points: {}'.format(self.r[i][0], self.r[i][1], self.r[i][2],self.r[i][3])
        string += '\nPortals:'
        if len(self.p) == 0:
            return string+ '\nNone'
        else: 
            for i in range(len(self.p)):
                string += '\n{}:({},{}) -> {}:({},{})'.format(self.n,self.p[0],self.p[1],self.p[2],self.p[3],self.p[4])
        return string