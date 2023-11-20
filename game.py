from typing import List
from character import Character
from player import Player


class Game:

    def __init__(self) -> None:
        self.players:List[Player] = []
        self.boundary_of_randomness = [] # on BOUND OF KNOWLEDGE, introduce randomness
        self.events = [] # set of facts in current frame.

    def addPlayer(self,character:Character) -> Player:
        player = Player(character=character)
        self.players.append(player)
        return player

    def deduce(self):
        '''
        The frame for the base logic engine to deduce the facts and update the world.
        i.e. the actions from players take effects.
        '''

    def generate(self):
        '''
        The frame for the boundary of randomness to generate RANDOMNESS
        '''

    def simulate(self):
        '''
        The frame for players to play, and take effects.
        '''
        print('SIMULATING')
        for player in self.players:
            player.command()

