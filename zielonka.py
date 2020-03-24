from attractor import *
from parity_game import ParityGame


def zielonka(game: ParityGame):
    if game.V == game.bdd.false:
        return game.bdd.false, game.bdd.false

    parity = max(game.parities.keys())
    i = parity % 2
    j = 1 - i

    attr = attr_i(i, game, game.parities[parity])
    if attr == game.V:
        (wi, wj) = (game.V, game.bdd.false)
    else:
        game_p = game.setminus(attr)
        (w0p, w1p) = zielonka(game_p)
        wip = w0p if i == 0 else w1p
        wjp = w1p if i == 0 else w0p
        if wjp == game.bdd.false:
            (wi, wj) = (game.V, game.bdd.false)
        else:
            game_pp = game.setminus(attr_i(j, game, wjp))
            (w0pp, w1pp) = zielonka(game_pp)
            wipp = w0pp if i == 0 else w1pp
            wjpp = w1pp if i == 0 else w0pp
            (wi, wj) = (wipp, game.V & ~wipp)

    w0 = wi if i == 0 else wj
    w1 = wj if i == 0 else wi
    return (w0, w1)
