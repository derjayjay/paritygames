from attractor import *
from parity_game import ParityGame
from game_solver import GameSolver


class ZielonkaSolver(GameSolver):
    def __init__(self, game: ParityGame):
        super().__init__()
        self.game = game

    def solve(self):
        return self.zielonka(self.game)

    def zielonka(self, game: ParityGame):
        if game.V == game.bdd.false:
            return game.bdd.false, game.bdd.false

        parity = max(game.parities.keys())
        i = parity % 2
        j = 1 - i

        attr = attr_i(i, game, game.get_parity(parity))
        if attr == game.V:
            (wi, wj) = (game.V, game.bdd.false)
        else:
            game_p = game.subgame(attr)
            (w0p, w1p) = self.zielonka(game_p)
            wip = w0p if i == 0 else w1p
            wjp = w1p if i == 0 else w0p
            if wjp == game.bdd.false:
                (wi, wj) = (game.V, game.bdd.false)
            else:
                game_pp = game.subgame(attr_i(j, game, wjp))
                (w0pp, w1pp) = self.zielonka(game_pp)
                wipp = w0pp if i == 0 else w1pp
                wjpp = w1pp if i == 0 else w0pp
                (wi, wj) = (wipp, game.V & ~wipp)

        w0 = wi if i == 0 else wj
        w1 = wj if i == 0 else wi
        return (w0, w1)