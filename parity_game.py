from dd import autoref as _bdd
from parser.ParityGameParser import ParsedNode, ParsedParityGame
from typing import *


class ParityGame:
    variable_size: int = 0

    def __init__(self):
        self.bdd = _bdd.BDD()
        self.variables = []
        self.parsed_pg = ParsedParityGame()

    def from_parsed(self, parsed_pg: ParsedParityGame):
        self.variable_size = parsed_pg.size.bit_length()
        self.parsed_pg = parsed_pg

        self.variables = ["o", "O"]
        for i in range(0, self.variable_size):
            self.variables.append("l%d" % i)
            self.variables.append("L%d" % i)

        self.bdd.declare(self.variables)

    def node_to_variable(self, parsed_node: ParsedNode):
        v = []

        if parsed_node.owner == 0:
            v.append("o")
        else:
            v.append("~o")

        c = 0
        for e in map(int, [i for i in '{:0{size}b}'.format(parsed_node.identifier, size=self.variable_size)]):
            if e == 0:
                v.append("~l%d" % c)
            else:
                v.append("l%d" % c)
            c += 1

        return ' /\ '.join(v)

    def variable_to_node(self, variable):
        return None
