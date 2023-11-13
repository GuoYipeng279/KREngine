from character import Character
from player import Player


class Game:

    def __init__(self) -> None:
        self.players:list[Player] = []

    def addPlayer(self,character:Character) -> Player:
        player = Player(character=character)
        self.players.append(player)
        return player

    def simulate(self):
        print('SIMULATING')
        for player in self.players:
            player.command()

