from block import Block, Terrain
from character import Character


class Player(Character):
    directions = {'D':0,'W':1,'A':2,'S':3}
    views = {'L':0,'I':1,'J':2,'K':3}

    def __init__(self, hp: int, weight: int, invincible: bool, position: Block, game) -> None:
        super().__init__(hp, weight, invincible, position, game)
        self.view_x, self.view_y = 0,0
        self.width, self.height = 40,40

    def render(self) -> None:
        for y in range(self.view_y-self.height//2,self.view_y+self.height*2):
            for x in range(self.view_x-self.width//2,self.view_x+self.width*2):
                try:
                    print(self.blocks[(x,y)],end=None)
                except:
                    print(Block.graphics[Terrain.UNKNOWN],end=None)
            print('')

    def command(self):
        cmd = input()
        if cmd: cmd = cmd[0]
        else: return
        if cmd in Player.directions:
            self.move(Player.directions[cmd])
        elif cmd in Player.views:
            if Player.views[cmd] == 0: self.view_x += 1
            if Player.views[cmd] == 1: self.view_y += 1
            if Player.views[cmd] == 2: self.view_x -= 1
            if Player.views[cmd] == 3: self.view_y -= 1
        