from constant import Constant
from event import Event


class Clause(Constant):
    '''
    Set of clauses are fixed from beginning, they are the rules for the game world.
    '''
    def __init__(self, head:Event, *body:Event) -> None:
        self.head = head
        self.body = body