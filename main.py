from game import Game
from character import Character


if __name__ == '__main__':
    print('Hello, World!')
    game = Game()
    char1 = Character()
    game.addPlayer(char1)
    while True:
        game.simulate()
        for player in game.players:
            player.render()