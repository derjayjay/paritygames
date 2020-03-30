from antlr4 import *
from parser.parity_gameLexer import parity_gameLexer
from parser.parity_gameParser import parity_gameParser
from parser.parity_gameListener import parity_gameListener
from pathlib import Path
from typing import List, Set, Dict
from copy import deepcopy


class ParsedNode:
    def __init__(self):
        self.identifier = 0
        self.parity = 0
        self.owner = 0
        self.successors: Set[int] = set()

    def __str__(self):
        s = "Node %d (parity %d, owner %d) - " % (self.identifier, self.parity, self.owner)
        s += "successors are " + str(self.successors)
        return s

    def add_successor(self, identifier):
        self.successors.add(identifier)


class ParsedParityGame:
    def __init__(self):
        self.size: int = 0
        self.nodes: Dict[int, ParsedNode] = {}

        self.even: Set[int] = set()
        self.odd: Set[int] = set()

        self.parities: Dict[int, Set[int]] = {}

    def __str__(self):
        s = "Parity game of size %d\n" % self.size
        for node in self.nodes.values():
            s += "\t" + str(node) + "\n"
        return s

    def add_node(self, node):
        self.nodes[node.identifier] = node

    """
    populate the data structures of the parity game
    """
    def populate(self):
        for node in self.nodes.values():
            if node.owner == 0:
                self.even.add(node.identifier)
            else:
                self.odd.add(node.identifier)

            if node.parity not in self.parities.keys():
                self.parities[node.parity] = {node.identifier}
            else:
                self.parities[node.parity].add(node.identifier)

    """
    create a subgame from the current parity game
    
    - remove, the set of nodes to remove
    """
    def create_subgame(self, remove: Set[int]):
        new = ParsedParityGame()
        new.size = self.size
        for n in self.nodes.keys():
            if n not in remove:
                nn = deepcopy(self.nodes[n])
                nn.successors -= remove
                new.add_node(nn)
        new.populate()
        return new


class ParityGamePrintListener(parity_gameListener):
    game = None
    current_node = None

    def enterNode(self, ctx: parity_gameParser.NodeContext):
        self.current_node = ParsedNode()

    def exitNode(self, ctx: parity_gameParser.NodeContext):
        self.game.add_node(self.current_node)

    def enterIdentifier(self, ctx: parity_gameParser.IdentifierContext):
        self.current_node.identifier = int(ctx.getText())

    def enterParity(self, ctx: parity_gameParser.ParityContext):
        self.current_node.parity = int(ctx.getText())

    def enterOwner(self, ctx: parity_gameParser.OwnerContext):
        self.current_node.owner = int(ctx.getText())

    def enterSuccessor(self, ctx: parity_gameParser.SuccessorContext):
        self.current_node.add_successor(int(ctx.getText()))

    def enterGame(self, ctx: parity_gameParser.GameContext):
        self.game = ParsedParityGame()

    def enterPreamble(self, ctx: parity_gameParser.PreambleContext):
        self.game.size = int("%s" % ctx.NUMBER())


class ParityGameParser:
    @staticmethod
    def parse_file(path):
        txt = Path(path).read_text()
        return ParityGameParser.parse_string(txt)

    @staticmethod
    def parse_string(string):
        return ParityGameParser.parse(InputStream(string))

    @staticmethod
    def parse(input_stream):
        lexer = parity_gameLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = parity_gameParser(stream)
        tree = parser.game()
        printer = ParityGamePrintListener()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        return printer.game
