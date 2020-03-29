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

    def setminus(self, a):
        remove = set()
        for i in self.bdd.pick_iter(a, care_vars=self.states):
            remove.add(self.variable_to_identifier(i))

        new_parsed = ParsedParityGame()
        new_parsed.size = self.parsed_pg.size
        for n in self.parsed_pg.nodes.keys():
            if n not in remove:
                nn = deepcopy(self.parsed_pg.nodes[n])
                nn.successors -= remove
                new_parsed.add_node(nn)
        new_parsed.populate()

        new_game = copy(self)
        new_game.parsed_pg = new_parsed
        new_game.populate()
        return new_game

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

    def populate(self):
        ee: Dict[str, str] = {}
        for i in range(0, 2 ** self.variable_size):
            variable = '(' + self.raw_node_to_variable(i, 0) + ')'
            ee[variable] = "FALSE"
            variable = '(' + self.raw_node_to_variable(i, 1) + ')'
            ee[variable] = "FALSE"

        v = []
        for n in self.parsed_pg.nodes.values():
            variable = '(' + self.node_to_variable(n) + ')'
            v.append(variable)
            self.id_to_variable[n.identifier] = variable
            succ = []
            for s in n.successors:
                succ.append('(' + self.node_to_variable(self.parsed_pg.nodes[s], True) + ')')
            ee[variable] = "(" + " \/ ".join(succ) + ")"

        e = []
        for i in ee.keys():
            # print(i + " => " + ee[i])
            e.append('(' + i + '=>' + ee[i] + ')')

        self.V = self.bdd.add_expr(' \/ '.join(v)) if len(v) > 0 else self.bdd.false
        self.V0 = self.V & self.bdd.add_expr('o')
        self.V1 = self.V & self.bdd.add_expr('~o')
        self.E = self.bdd.add_expr(' /\ '.join(e))

        for p in range(0, self.d + 1):
            self.parities[p] = self.bdd.false

        for p in self.parsed_pg.parities.keys():
            v = []
            for n in self.parsed_pg.parities[p]:
                v.append(self.id_to_variable[n])
            self.parities[p] = self.bdd.add_expr(' \/ '.join(v))

    def get_vi(self, i: int):
        if i == 0:
            return self.V0
        else:
            return self.V1

    def node_to_variable(self, node: ParsedNode, primed=False):
        return self.raw_node_to_variable(node.identifier, node.owner, primed)

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
