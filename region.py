from typing import Dict, List
from entity import Entity
import numpy as np

class Region:
    pass

class Region(Entity):
    '''
    Region is a tree like map, blocks are leaf nodes on the tree.
    For unknown regions, they simplify the heat random simulation.
    Building is from bottom to top level

    
    Partition a coarse region into 4 finer regions
    Partition often happen when a coarse region being observed, 
    observe argument for this.
    '''
    max_depth = 10
    regions:List[Dict[tuple, Region]] = [dict() for _ in range(max_depth+1)]
    sparcity = 10

    def __init__(self, observe:Region, x:int, y:int, level:int) -> None:
        if level > Region.max_depth: raise NotImplementedError
        self.partitioned = False
        self.x, self.y = x,y
        Region.regions[level][(x,y)] = self
        # print('REGION:',[len(layer) for layer in Region.regions])
        self.level = level
        self.chi:List[Region] = [] # higher bit for x, lower bit for y

        if level == Region.max_depth: self.randomness:int = (4**level)//Region.sparcity # initial random particles in the top area.
        else: # find parent
            if (x>>1,y>>1) not in Region.regions[level+1]:
                par = Region(self, x>>1, y>>1, level+1)
                Region.regions[level+1][(x>>1,y>>1)] = par
            self.par = Region.regions[level+1][(x>>1,y>>1)]
            if not self.par.partitioned:
                self.par.partition(self)

        if level > 0 and observe:
            self.partition(observe)
        self._neighbours:List[Region] = []

    def partition(self, observe):
        # partition into 4
        if self.partitioned: raise NotImplementedError
        self.partitioned = True
        x,y,level = self.x, self.y, self.level
        for i in range(4):
            xx,yy = (x<<1)+((i>>1)&1),(y<<1)+(i&1)
            if observe and observe.x == xx and observe.y == yy:
                child = observe
            else:
                child = Region(None, xx,yy, level-1) # top to bottom, no child
            # child.randomness = self.randomness // 4
            self.chi.append(child)
        # randomly distribute random from parent
        div1 = np.random.binomial(self.randomness, .5)
        div0 = self.randomness - div1
        div00 = np.random.binomial(div0, .5)
        div10 = np.random.binomial(div1, .5)
        div01 = div0-div00
        div11 = div1-div10
        dist = [div00,div01,div10,div11]
        for c,r in zip(self.chi, dist):
            c.randomness = r
        self.randomness = 0 # handle randomness in subregions when partitioned

    def check_neighbour(self, neighbour:Region, x:int, y:int):
        '''
        Multi level neighbour checking
        '''
        if neighbour is None: return
        if not neighbour.partitioned:
            if self.level != neighbour.level or x > 0 or y > 0:
                self._neighbours.append(neighbour)
            return
        if (x,y) == (1,0):
            self.check_neighbour(neighbour.chi[0])
            self.check_neighbour(neighbour.chi[1])
        elif (x,y) == (-1,0):
            self.check_neighbour(neighbour.chi[2])
            self.check_neighbour(neighbour.chi[3])
        elif (x,y) == (0,1):
            self.check_neighbour(neighbour.chi[0])
            self.check_neighbour(neighbour.chi[2])
        elif (x,y) == (0,-1):
            self.check_neighbour(neighbour.chi[1])
            self.check_neighbour(neighbour.chi[3])

    def neighbours(self):
        '''
        find neighbour smaller or same regions
        '''
        self._neighbours = []
        if self.partitioned: # if partitioned, let subregions do the search
            for subs in self.chi:
                subs.neighbours()
            return
        # same level neighbour, x+1 or y+1 only to avoid repetition
        x,y = self.x, self.y
        if (x+1,y) in Region.regions[self.level]:
            region = Region.regions[self.level][(x+1,y)]
            self.check_neighbour(region,1,0)
        if (x,y+1) in Region.regions[self.level]:
            region = Region.regions[self.level][(x,y+1)]
            self.check_neighbour(region,0,1)
        if (x-1,y) in Region.regions[self.level]:
            region = Region.regions[self.level][(x-1,y)]
            self.check_neighbour(region,-1,0)
        if (x,y-1) in Region.regions[self.level]:
            region = Region.regions[self.level][(x,y-1)]
            self.check_neighbour(region,0,-1)

    def __repr__(self) -> str:
        return str((self.x,self.y,self.level))

    def transfer(self):
        '''
        random particles transfers, according to neighbour regions
        '''
        roots = Region.regions[Region.max_depth]
        for r in roots:
            roots[r].neighbours()
            