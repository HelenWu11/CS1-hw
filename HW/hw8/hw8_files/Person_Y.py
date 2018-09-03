class Person(object):
    def __init__( self,name,radius,home_universe,x,y,dx,dy,current_universe,rewards = [],points = 0):
        self.name = name
        self.radius = radius
        self.home_universe = home_universe
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.current_universe = current_universe
        self.rewards = rewards
        self.points = points
    def __str__ (self):
        string = '{} of EasyCS1 in universe EasyCS1'.format(self.name, self.home_universe, self.current_universe)
        string += '\n    at ({},{}) speed ({},{}) with {} rewards and {} points'.format(self.x, self.y, self.dx, self.dy,len(self.rewards), self.points)
        return string