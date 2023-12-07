from enum import IntEnum
from constant import Constant

# CONSTANTS ARE THINGS

class Predicates(IntEnum):
    ALIVE=0, # a character is alive, ALIVE(sb)
    KNOW=1, # sb know about sth, KNOW(sb, sth)
    KILLED=2, # A killed B, KILLED(A,B)
    SEE=3, # sb is seeing somewhere, SEE(A,Place)
    SEEN=4, # sb know terrain of sw, SEEN(A,Place)
    FARMER=5, # sb is a farmer, FARMER(A)
    GOTO=6, # sb is going smw, GOTO(A,Place)
    ARABLE=7, # smw is arable, ARABLE(Place)
    FIELD=8, # An area is a field, FIELD(AREA)
    GOTOWORK=9, # sb is going workplace, GOTOWORK(A,Place)
    WORKING=10, # sb is working
    AT=11, # sb at sw, AT(A,Place)
    OWN=12, # sb own sth, OWN(A,sth)


class Event(Constant):
    '''
    Events are facts in the game world, generating while game simulating
    Initialize as P(args), these are absolutely true.
    e.g. KNOW(A,sth wrong), means A have some false knowledge, but this fact is true, A does know sth
    '''
    def __init__(self, predicate:Predicates, *args:Constant) -> None:
        self.predicate = predicate
        self.args = args

    def __str__(self):
        return str(self.predicate)+"("+','.join(self.args)+")"

if __name__ == '__main__':
    print(Event(Predicates.ALIVE, Constant.X))