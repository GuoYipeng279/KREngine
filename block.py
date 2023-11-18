from enum import IntEnum
from region import Region


class Terrain(IntEnum):
    DEFAULT = 0
    UNKNOWN = 1
    WATER = 2
    LAND = 3
    NOPASS = 4

class Block:
    pass

class Block(Region):
    '''
    Blocks are game entity, but not an object, they belong to game system, not game world
    '''
    counter = 0
    graphics = [' ','?','w','.','#']
    adj = [(1,0),(0,1),(-1,0),(0,-1)]
    blocks = dict()

    def __init__(self,x=0,y=0,terrain=Terrain.UNKNOWN,altitude=0):
        # print('Init Block:',(x,y))
        self.x, self.y = x,y
        depth = Region.max_depth
        par:Region = None
        while depth > 0:
            xx,yy = x>>depth, y>>depth
            lr, ud = xx&1, yy&1
            if (xx,yy,depth) not in Region.regions:
                index = (lr<<1)+ud
                Region.regions[(xx,yy,depth)] = Region(par, depth, index)
                if par: par.chi[index] = Region.regions[(xx,yy,depth)]
            par = Region.regions[(xx,yy,depth)]
            depth -= 1
        lr, ud = x&1, y&1
        index = (lr<<1)+ud
        super().__init__(par, 0, index)
        par.chi[index] = self

        # self.sign = hash(x)+hash(y)
        self.lies = None
        self.terrain = terrain
        self.altitude = altitude
        self.adjacent:list[Block] = [None]*4 # 00 for right, 01 for up, 10 for left, 11 for down
        if self.position in Block.blocks: raise NotImplementedError
        Block.blocks[self.position] = self
        Block.counter += 1

        right = Block.getBlock(x+1,y,False)
        self.adjacent[0] = right
        if right: right.adjacent[2] = self

        up = Block.getBlock(x,y+1,False)
        self.adjacent[1] = up
        if up: up.adjacent[3] = self

        left = Block.getBlock(x-1,y,False)
        self.adjacent[2] = left
        if left: left.adjacent[0] = self
        
        down = Block.getBlock(x,y-1,False)
        self.adjacent[3] = down
        if down: down.adjacent[1] = self

    def know(self):
        self.terrain = Terrain.LAND

    def getBlock(x,y,auto=True):
        if (x,y) not in Block.blocks:
            if not auto: return None
            Block.blocks[(x,y)] = Block(x,y)
        ans:Block = Block.blocks[(x,y)]
        return ans

    def printBlock(x,y):
        block = Block.getBlock(x,y,False)
        if block is None: return Block.graphics[Terrain.DEFAULT]
        return str(block)

    @property
    def position(self):
        return self.x, self.y

    def distance2(self, block):
        return (self.x-block.x)**2+(self.y-block.y)**2

    def area(self, cond) -> set:
        # get an area, start from this block, given an condition
        rec = set()
        def dfs(block:Block):
            if block.position in rec or not cond(block): return
            rec.add(block.position)
            for i, bl in enumerate(block.adjacent):
                if bl is None:
                    dx,dy = Block.adj[i]
                    bl = Block.getBlock(block.x+dx, block.y+dy) # ADJACENT
                dfs(bl)
        dfs(self)
        return rec

    def getAdj(self,arg):
        ans = self.adjacent[arg%4]
        return ans

    def __repr__(self) -> str:
        return str((self.x, self.y))

    def __str__(self) -> str:
        if self.lies is None:
            return str(Block.graphics[self.terrain])
        else:
            return str(self.lies)
