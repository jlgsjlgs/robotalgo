class Node:
    def __init__(self, x, y, parent, obs):
        self.x = x
        self.y = y
        self.parent = parent
        
        if parent != None:
            self.gn = parent.gn + 20
        else:
            self.gn = 0
        
        self.hn = abs(obs.goalx-self.x) + abs(obs.goaly-self.y)
        self.fn = self.gn + self.hn


