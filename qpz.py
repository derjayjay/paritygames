from attractor import *
from parity_game import ParityGame


def qpz(game: ParityGame, d: int, p0: int, p1: int):
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

    wj = game.V & ~ qpz(game, d, p0p, p1p)
    a = attr_i(j, game, wj)
    game_p = game.setminus(a)
    game_pp = game_p.setminus(attr_i(i, game_p, game_p.parities[d]))
    wjpp = qpz(game_pp, d - 1, p0, p1)
    ap = attr_i(j, game_p, wjpp)
    game_ppp = game_p.setminus(ap)
    wjppp = (game.V & ~ (a | ap)) & ~ qpz(game_ppp, d, p0p, p1p)
    return game.V & ~(a | ap | wjppp)
