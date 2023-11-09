from block import Block


class Thing:
    def __init__(self,hp:int,weight:int,invincible:bool,movable:bool,position:Block,game) -> None:
        self.hp,self.weight,self.invincible,self.movable,self.position = hp,weight,invincible,movable,position
        self.game = game

    def __str__(self) -> str:
        return 'O'