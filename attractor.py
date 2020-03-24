from parity_game import ParityGame


def cpre_i(i: int, game: ParityGame, r):
    moves_to_r = game.E & game.bdd.let(game.primed, r)
    states_to_r = game.bdd.exist(game.primed_states, moves_to_r)

    in_odd = states_to_r & game.get_vi(i - 1)
    in_odd = game.E & in_odd
    in_odd = in_odd & game.bdd.let(game.primed, game.V & ~r)
    in_odd = game.bdd.exist(game.primed_states, in_odd)

    return states_to_r & ~in_odd


def attr_i(i: int, game: ParityGame, r):
    previous_attractor = game.bdd.false
    current_attractor = r

    while previous_attractor != current_attractor:
        previous_attractor = current_attractor
        cpre = cpre_i(i, game, current_attractor)
        current_attractor = current_attractor | cpre

    return current_attractor