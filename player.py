from block import Block
from character import Character


class Player:
    '''
    Players of the game, a player controled character is 
    controled by WASD, rather than C+ planning
    '''
    directions = {'D':0,'S':1,'A':2,'W':3}
    views = {'L':0,'K':1,'J':2,'I':3}
    players = []

    def __init__(self, character:Character) -> None:
        self.character = character
        self.view_x, self.view_y = 0,0
        self.width, self.height = 40,40
        Player.players.append(self)

    def render(self) -> None:
        for y in range(self.view_y-self.height//2,self.view_y+self.height//2):
            for x in range(self.view_x-self.width//2,self.view_x+self.width//2):
                # print(self.character.game.blocks)
                print(Block.printBlock(x,y),end='')
            print('')

    def command(self):
        try:
            cmd = input('Player{}:'.format(self.character.id))
        except:
            cmd = 'W'
        if cmd == 'Q': quit()
        # print(cmd)
        if cmd: cmd = cmd[0]
        else: return
        if cmd in Player.directions:
            self.character.move(Player.directions[cmd])
        elif cmd in Player.views:
            if Player.views[cmd] == 0: self.view_x += 1
            if Player.views[cmd] == 1: self.view_y += 1
            if Player.views[cmd] == 2: self.view_x -= 1
            if Player.views[cmd] == 3: self.view_y -= 1
        