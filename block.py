from enum import Enum

class Terrain(Enum):
    DEFAULT = 0
    UNKNOWN = 1
    WATER = 2
    LAND = 3
    NOPASS = 4

class Block:
    graphics = ['*','?','w','.','#']

    def __init__(self,x,y,terrain=Terrain.LAND,altitude=0,game=None):
        self.x, self.y = x,y
        self.sign = hash(x)+hash(y)
        self.terrain = terrain
        self.altitude = altitude
        self.object = None
        self.adjacent = [None]*4 # 00 for right, 01 for up, 10 for left, 11 for down
        if game is not None:
            try:
                right = game.blocks[(x+1,y)]
                self.adjacent[0] = right
                right.adjacent[2] = self
            except: pass
            try:
                up = game.blocks[(x,y+1)]
                self.adjacent[1] = up
                up.adjacent[3] = self
            except: pass
            try:
                left = game.blocks[(x-1,y)]
                self.adjacent[2] = left
                left.adjacent[0] = self
            except: pass
            try:
                down = game.blocks[(x,y-1)]
                self.adjacent[3] = down
                down.adjacent[1] = self
            except: pass

    def position(self):
        return self.x, self.y

    def distance2(self, block):
        return (self.x-block.x)**2+(self.y-block.y)**2

    def area(self, cond) -> set:
        # get an area, start from this block, given an condition
        rec = set()
        def dfs(block):
            if (self.x, self.y) in rec or not cond(block): return
            rec.add(block)
            for bl in block.adjacent:
                dfs(bl)
        dfs(self)
        return rec

    def getAdj(self,arg):
        ans = self.adjacent[arg%4]
        if ans is None: raise NotImplementedError

    def __repr__(self) -> str:
        return str((self.x, self.y))

    def __str__(self) -> str:
        if self.object is None:
            return Block.graphics[self.terrain]
        else:
            return str(self.object)
    