from entity import Entity

class Region:
    pass

class Region(Entity):
    '''
    Region is a tree like map, blocks are leaf nodes on the tree.
    For unknown regions, they simplify the heat random simulation.
    '''
    regions = dict()
    max_depth = 10

    def __init__(self, par:Region, level:int, at:int) -> None:
        self.par = par
        self.level = level
        self.at = at
        self.chi = [None]*4

