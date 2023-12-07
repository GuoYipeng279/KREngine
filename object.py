from block import Block
from entity import Entity


class Thing(Entity):
    '''
    Objects among entitys, they have clear coordinates in the game world.
    '''
    counter = 0
    objects = dict()

    def __init__(self,hp:int,weight:int,invincible:bool,movable:bool,position=None) -> None:
        self.hp,self.weight,self.invincible,self.movable,self.position = hp,weight,invincible,movable,position
        self.id = Thing.counter
        if self.position is None: self.position = 0,0
        if type(self.position) == tuple:
            self.position = Block.getBlock(*self.position)
        self.position.lies = self
        Thing.counter += 1
        Thing.objects[self.id] = self

    def moveTo(self, block:Block):
        if block.lies: return
        self.position.lies = None
        block.lies:Thing = self
        self.position = block


    def __str__(self) -> str:
        return 'O'