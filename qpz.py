from attractor import *
from parity_game import ParityGame
from game_solver import GameSolver


class QPZSolver(GameSolver):
    def __init__(self, game: ParityGame):
        super().__init__()
        self.game = game

    def solve(self):
        i = self.game.d % 2
        wi = self.qpz(self.game, self.game.d, self.game.parsed_pg.size, self.game.parsed_pg.size)
        wj = self.game.V & ~wi

        w0 = wi if i == 0 else wj
        w1 = wj if i == 0 else wi
        return (w0, w1)

    def qpz(self, game: ParityGame, d: int, p0: int, p1: int):
        if game.V == game.bdd.false:
            return game.bdd.false

        i = d % 2
        j = 1 - i
        pi = p0 if i == 0 else p1
        pj = p1 if i == 0 else p0

        if pj == 0 or d == 0:
            return game.V

        pip = pi
        pjp = pj // 2

        p0p = pip if i == 0 else pjp
        p1p = pjp if i == 0 else pip

        wj = game.V & ~ self.qpz(game, d, p0p, p1p)
        a = attr_i(j, game, wj)
        game_p = game.subgame(a)
        game_pp = game_p.subgame(attr_i(i, game_p, game_p.get_parity(d)))
        wjpp = self.qpz(game_pp, d - 1, p0, p1)
        ap = attr_i(j, game_p, wjpp)
        game_ppp = game_p.subgame(ap)
        wjppp = (game.V & ~ (a | ap)) & ~ self.qpz(game_ppp, d, p0p, p1p)
        return game.V & ~(a | ap | wjppp)


