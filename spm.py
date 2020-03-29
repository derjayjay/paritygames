from parser.ParityGameParser import ParsedParityGame, ParsedNode
from game_solver import GameSolver
from typing import *
from itertools import cycle, zip_longest


class SmallProgressMeasuresSolver(GameSolver):
    def __init__(self, game: ParsedParityGame):
        super().__init__()
        self.game: ParsedParityGame = game
        self.V: List[int] = self.game.nodes.keys()
        self.cycle = cycle(self.V)
        self.pi: Dict[int, List[int]] = {}
        self.max_parity = max(self.game.parities.keys())
        self.failed = 0
        self.max_pi = [0 for i in range(0, self.max_parity + 1)]
        for p in self.game.parities.keys():
            self.max_pi[p] = len(self.game.parities[p])

    def solve(self):
        for n in self.V:
            pr = []
            for i in range(0, self.max_parity + 1):
                pr.append(0)
            self.pi[n] = pr

        self.small_progress_measures()

        v0 = []
        v1 = []
        strategy0 = {}

        for n in self.V:
            if self.pi[n]:
                v0.append(n)
                if self.game.nodes[n].owner == 0:
                    strategy0[n] = self.find_strategy(n)
            else:
                v1.append(n)

        print(strategy0)
        return (v0, v1, strategy0)

    def small_progress_measures(self):
        v = self.next_vertex()

        while v != -1:
            new = self.lift(v)
            if not self.are_equal(self.pi[v], new):
                self.pi[v] = new
                self.failed = 0
            v = self.next_vertex()

        pass

    def are_equal(self, left: List[int], right: List[int]):
        if len(left) != len(right):
            return False

        for (l, r) in zip_longest(left, right):
            if l != r:
                return False

        return True

    def find_strategy(self, v: int):
        n = self.game.nodes[v]
        neighbours = {}
        for w in n.successors:
            neighbours[w] = self.pi[w]

        minimum = self.min(list(neighbours.values()))
        return [key for key, value in neighbours.items() if self.are_equal(value, minimum)][0]

    def next_vertex(self):
        if self.failed >= len(self.V):
            return -1
        else:
            self.failed += 1
            return next(self.cycle)

    def lift(self, v):
        n = self.game.nodes[v]
        measures = []
        for w in n.successors:
            measures.append(self.prog(v, w))

        if n.owner == 0:
            return self.min(measures)
        else:
            return self.max(measures)

    def prog(self, v, w):
        p = self.game.nodes[v].parity
        m = [0 for i in range(self.max_parity + 1)]
        mw = self.pi[w]
        if not mw:
            return []

        if p % 2 == 1:
            m[p] = mw[p] + 1
            if m[p] > self.max_pi[p]:
                return []
        else:
            m[p] = mw[p]

        for i in range(p + 1, self.max_parity + 1):
            if i % 2 == 0:
                continue
            m[i] = mw[i]

        return m

    def max(self, measures: List[List[int]]):
        current_max = measures[0]
        if not current_max:
            return current_max

        for i in range(1, len(measures)):
            m = measures[i]
            if not m:
                return m

            for p in range(self.max_parity, 0, -1):
                if m[p] < current_max[p]:
                    break
                elif m[p] > current_max[p]:
                    current_max = m
                    break
                else:
                    continue

        return current_max

    def min(self, measures: List[List[int]]):
        current_min = measures[0]

        for i in range(1, len(measures)):
            m = measures[i]
            if not m:
                continue
            if not current_min:
                current_min = m
                continue

            for p in range(self.max_parity, 0, -1):
                if m[p] < current_min[p]:
                    current_min = m
                    break
                elif m[p] > current_min[p]:
                    break
                else:
                    continue
        return current_min
