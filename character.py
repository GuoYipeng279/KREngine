from block import Block
from event import Event
from object import Thing
from enum import Enum

class BodyState(Enum):
    HEALTHY = 0
    INJURED = 1
    WASTED = 2
    LOST = 3

class Body:
    def __init__(self, owner) -> None:
        self.owner = owner
        self.state = BodyState.HEALTHY

    def injure(self):
        self.state += 1
    
    def recover(self):
        if self.state == BodyState.INJURED:
            self.state -= 1

class Hand(Body):
    def __init__(self, owner) -> None:
        super().__init__(owner)
        self.inhand = None

    def take(self, equip):
        if self.state != BodyState.HEALTHY: return
        self.inhand = equip
        
    def use(self):
        if self.state != BodyState.HEALTHY: return

class Character(Thing):
    def __init__(self, hp: int, weight: int, invincible: bool, position: Block, game) -> None:
        super().__init__(hp, weight, invincible, True, position, game)
        self.memory = []
        self.knowledge = []
        self.facing = 0 # 0 right, 1 up, 2 left, 3 down
        self.alive = True
        self.sight = 10
        self._sighting = set()

    def move(self, facing:int):
        if facing == self.facing:
            self.position = self.position.getAdj(facing)
        else:
            self.facing = facing

    def insight(self,block:Block) -> bool:
        return self.position.distance2(block) <= self.sight**2

    @property
    def sighting(self) -> set:
        if not self._sighting:
            self._sighting = self.position.area(self.insight)
        return self._sighting

    def see(self, block:Block):
        pass

    def use(self, card):
        pass

    def tell(self, event:Event):
        pass

    def talk(self, sth):
        pass
    
    def observe(self, event:Event):
        pass

    def __str__(self) -> str:
        return 'P'