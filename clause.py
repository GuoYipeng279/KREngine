from typing import List
from constant import Constant
from event import Event, Predicates
import clingo


class Clause:
    pass

class Clause(Constant):
    '''
    Set of clauses are fixed from beginning, they are the rules for the game world.
    '''

    rules:List[Clause] = []

    def default_values(default:str, value:int, typ:str='char'):
        ans = (
            '{0}(X,{1}) :- not -{0}(X,{1}), {2}(X).'.format(default,value,typ),
            '-{0}(X,{1}) :- {0}(X,T1), T1 != {1}, {2}(X).'.format(default,value,typ),
            ':- {0}(X,T1),{0}(X,T2),T1!=T2.'.format(default),
        )
        return ans

    # mechanisms
    land = [
        'block(here).',
        'land(here).',
        *default_values('arable',0,'land'),
        'va_arable(X,1) :- attacked(Y,X), char(Y).',
        'va_seed(X,1) :- seeded(X), land(X)',
    ]
    # S for self
    instincts = [
        'self(me).', # who is self
        'char(me).', # me is a character
        'attack(X) :- not -attack(X), revenge(X).', # revenge by attack if no exceptions
        'attack(X) :- not -attack(X), jealous(X).', # same for jealous
        '-attack(X) :- afraid(X).', # cant attack when afraid
        'afraid(X) :- strength(X,V1), strength(S,V2), self(S), V1>2*V2.', # afraid who 2x stronger
        'protect(me) :- not -protect(me).', # self protection
        '-attack(X) :- protect(X).', # dont attack protecting ones
        'revenge(X) :- attacked(X,Y),protect(Y).', # when protecting ones attacked, revenge
        'jealous(X) :- not -jealous(X), wealth(X,V1), wealth(S,V2), self(S), V1>10*V2.', # jealous those 10x wealther
        'unprotect(X) :- protect(X), attacked(X,S), self(S).', # stop protecting ones who attack me.
        *default_values('wealth',0),
        *default_values('strength',0),
    ]

    solver_out = []

    def __init__(self) -> None:
        self.model = []

    def on_model(m):
        Clause.solver_out = str(m).split()

    def solver(self, program, facts=[]):
        ctl = clingo.Control()
        ctl.add("base", [], '\n'.join(program))
        ctl.add("base", [], '\n'.join(facts))
        ctl.ground([("base", [])])
        ctl.solve(on_model=self.on_model)
        return Clause.solver_out

if __name__ == '__main__':
    print('\n'.join(Clause.instincts))
    c = Clause()
    ans = c.solver(Clause.instincts,['attacked(him,me).'])
    print(ans)