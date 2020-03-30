from dd import autoref as _bdd
from parser.ParityGameParser import ParsedNode, ParsedParityGame
from typing import *
from copy import copy, deepcopy


class ParityGame:
    def __init__(self):
        self.bdd: _bdd.BDD = None
        self.variable_size: int = 0
        self.d: int = 0
        self.variables = []
        self.states: List[str] = ['o']
        self.primed_states: List[str] = ['O']
        self.primed: Dict[str, str] = {}
        self.unprimed: Dict[str, str] = {}
        self.parsed_pg: ParsedParityGame = None
        self.V = None
        self.V0 = None
        self.V1 = None
        self.E = None
        self.parities = {}
        self.id_to_variable = {}

    def __copy__(self):
        new = type(self)()
        new.bdd = self.bdd
        new.variable_size = self.variable_size
        new.variables = self.variables
        new.states = self.states
        new.primed_states = self.primed_states
        new.primed = self.primed
        new.unprimed = self.unprimed
        new.d = self.d

        return new

    """
    Create a subgame from this game
    
    - a, the set of nodes to remove, as bdd
    """
    def subgame(self, a):
        remove = set()
        for i in self.bdd.pick_iter(a, care_vars=self.states):
            remove.add(self.variable_to_identifier(i))

        new_parsed = self.parsed_pg.create_subgame(remove)

        new_game = copy(self)
        new_game.parsed_pg = new_parsed
        new_game.populate()
        return new_game

    """
    create a symbolic parity game from a parsed parity game
    
    - parsed_pg, the parsed parity game
    """
    def from_parsed(self, parsed_pg: ParsedParityGame):
        self.bdd = _bdd.BDD()
        self.variable_size = parsed_pg.size.bit_length()
        self.parsed_pg = parsed_pg
        self.d = max(self.parsed_pg.parities.keys())

        self.variables = ["o", "O"]
        for i in range(0, self.variable_size):
            self.states.append("l%d" % i)
            self.primed_states.append("L%d" % i)

        self.variables += self.states
        self.variables += self.primed_states

        for s in self.states:
            self.primed[s] = s.upper()

        for s in self.primed_states:
            self.unprimed[s] = s.lower()

        self.bdd.declare(*self.variables)
        self.populate()

    """
    populate the data structures of the parity game
    """
    def populate(self):
        # initialise the transition relation with transitions to false for every possible state
        ee: Dict[str, str] = {}
        for i in range(0, 2 ** self.variable_size):
            variable = '(' + self.raw_node_to_variable(i, 0) + ')'
            ee[variable] = "FALSE"
            variable = '(' + self.raw_node_to_variable(i, 1) + ')'
            ee[variable] = "FALSE"

        # create the transitions from the successor set of every vertex
        v = []
        for n in self.parsed_pg.nodes.values():
            variable = '(' + self.node_to_variable(n) + ')'
            v.append(variable)
            self.id_to_variable[n.identifier] = variable
            succ = []
            for s in n.successors:
                succ.append('(' + self.node_to_variable(self.parsed_pg.nodes[s], True) + ')')
            ee[variable] = "(" + " \/ ".join(succ) + ")"

        # set up the relation
        e = []
        for i in ee.keys():
            # print(i + " => " + ee[i])
            e.append('(' + i + '=>' + ee[i] + ')')

        # finally, fill the sets V, V_0, V_1 and E
        self.V = self.bdd.add_expr(' \/ '.join(v)) if len(v) > 0 else self.bdd.false
        self.V0 = self.V & self.bdd.add_expr('o')
        self.V1 = self.V & self.bdd.add_expr('~o')
        self.E = self.bdd.add_expr(' /\ '.join(e))

        # create a set of nodes for each parity
        for p in self.parsed_pg.parities.keys():
            v = []
            for n in self.parsed_pg.parities[p]:
                v.append(self.id_to_variable[n])
            self.parities[p] = self.bdd.add_expr(' \/ '.join(v))

    """
    get the set V_i for a player i
    
    - i, the player id
    """
    def get_vi(self, i: int):
        if i == 0:
            return self.V0
        else:
            return self.V1

    """
    get the set of vertices with parity p
    
    - p, the parity
    """
    def get_parity(self, p: int):
        if p not in self.parities.keys():
            return self.bdd.false
        return self.parities[p]


    """
    get a boolean expression representing the given vertex
    
    - node, the node from the parsed parity game
    - primed, optional, when the boolean expression should use primed variables
    """
    def node_to_variable(self, node: ParsedNode, primed=False):
        return self.raw_node_to_variable(node.identifier, node.owner, primed)

    """
    get a boolean expression representing the given id

    - identifier, the id of the node
    - owner, the player owning the node
    - primed, optional, when the boolean expression should use primed variables
    """
    def raw_node_to_variable(self, identifier: int, owner: int, primed=False):
        v = []
        if primed:
            p = 'L'
            o = 'O'
        else:
            p = 'l'
            o = 'o'

        if owner == 0:
            v.append(o)
        else:
            v.append("~" + o)

        c = 0
        for e in map(int, [i for i in '{:0{size}b}'.format(identifier, size=self.variable_size)]):
            if e == 0:
                v.append("~" + p + "%d" % c)
            else:
                v.append(p + "%d" % c)
            c += 1

        return ' /\ '.join(v)

    """
    converts a conjunction of boolean variables to a vertex id
    
    - variable, the conjunction
    - primed, whether primed variables should be used
    """
    def variable_to_identifier(self, variable: Dict[str, bool], primed=False):
        s = ''
        if primed:
            p = 'L'
        else:
            p = 'l'

        for i in range(0, self.variable_size):
            if variable[p + '%d' % i]:
                s += '1'
            else:
                s += '0'

        return int(s, 2)
