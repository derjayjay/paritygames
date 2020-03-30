from parity_game import ParityGame


def cpre_i(i: int, game: ParityGame, r):
    """
    compute CPre_i for i in set r for game g
    """
    moves_to_r = game.E & game.bdd.let(game.primed, r)              # get all transitions that end in r
    states_to_r = game.bdd.exist(game.primed_states, moves_to_r)    # get all states with transitions to r

    in_odd = states_to_r & game.get_vi(i - 1)                       # get the subset of states that belong to opponent
    in_odd = game.E & in_odd                                        # get all transitions from these states
    in_odd = in_odd & game.bdd.let(game.primed, game.V & ~r)        # get those transitions, that do not end in r
    in_odd = game.bdd.exist(game.primed_states, in_odd)             # get all opponent states not exclusively going to r

    return states_to_r & ~in_odd                                    # CPre_i(R)


def attr_i(i: int, game: ParityGame, r):
    """
    compute the attractor for i of set r in the game game
    """
    previous_attractor = game.bdd.false
    current_attractor = r

    while previous_attractor != current_attractor:
        previous_attractor = current_attractor
        cpre = cpre_i(i, game, current_attractor)
        current_attractor = current_attractor | cpre

    return current_attractor
