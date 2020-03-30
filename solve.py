import sys
from parser.ParityGameParser import ParityGameParser
from zielonka import *
from qpz import *
from spm import *
import argparse

"""
Prints the winning set for a player.

- game, a symbolic parity game
- player, the id of the player
- w, the winning set as bdd
"""
def print_result_from_bdd(game, player, w):
    print("Player " + str(player) + " wins from nodes:")
    models = list(game.bdd.pick_iter(w, care_vars=game.states))
    nodes = []
    for m in models:
        f = game.variable_to_identifier(m)
        nodes.append(f)
    print("\t {" + ", ".join(str(n) for n in sorted(nodes, reverse=True)) + "}")

"""
Prints the winning set and strategy for a player

- player, the id of the player
- w, the winning set as a list of node ids
- strategy, optional, the winning strategy
"""
def print_result_from_graph(player, w, strategy=None):
    print("Player " + str(player) + " wins from nodes:")
    print("\t {" + ", ".join(str(n) for n in sorted(w, reverse=True)) + "}")
    steps = []
    if strategy:
        for s in sorted(strategy.keys()):
            steps.append(str(s) + "->" + str(strategy[s]))
    print("with strategy")
    print("\t [" + ",".join(steps) + "]")


def generate_solution_bdd(game: ParityGame, w0, w1):
    nodes = {}
    models = list(game.bdd.pick_iter(w0, care_vars=game.states))
    for m in models:
        f = game.variable_to_identifier(m)
        nodes[f] = 0
    models = list(game.bdd.pick_iter(w1, care_vars=game.states))
    for m in models:
        f = game.variable_to_identifier(m)
        nodes[f] = 1

    print("paritysol " + str(max(nodes.keys())) + ";")
    for i in sorted(nodes.keys()):
        print(str(i) + " " + str(nodes[i]) + ";")


def generate_solution(w0, w1, strategy0, strategy1):
    nodes = {}
    for n in w0:
        nodes[n] = 0
    for n in w1:
        nodes[n] = 1

    print("paritysol " + str(max(nodes.keys())) + ";")
    for i in sorted(nodes.keys()):
        owner = nodes[i]
        strategy = "";
        if owner == 0 and i in strategy0.keys():
            strategy = " " + str(strategy0[i])
        elif owner == 1 and i in strategy1.keys():
            strategy = " " + str(strategy1[i])
        print(str(i) + " " + str(owner) + strategy + ";")


def main():
    cmd = argparse.ArgumentParser(prog="solve.py", description="Parity game solver for the Reactive Synthesis lecture")
    g = cmd.add_mutually_exclusive_group(required=True)
    g.add_argument('--zielonka', help="use symbolic Zielonka for solving", action='store_true')
    g.add_argument('--qpz', help="use symbolic QPZ for solving", action='store_true')
    g.add_argument('--spm', help="use non-symbolic Small Progress Measures for solving and strategy extraction", action='store_true')
    cmd.add_argument('--readable_solution', help="print a readable solution", action='store_true', required=False)
    cmd.add_argument('--print_game', help="print information about the game", action='store_true', required=False)
    cmd.add_argument('file', metavar='FILE', type=str, help="the game to solve in PGSolver format")

    args = cmd.parse_args()

    parsed_result = ParityGameParser.parse_file(args.file)
    parsed_result.populate()
    if args.print_game:
        print(parsed_result)

    if args.zielonka:
        game = ParityGame()
        game.from_parsed(parsed_result)

        zielonka = ZielonkaSolver(game)
        w0, w1 = zielonka.solve()

        if args.readable_solution:
            print_result_from_bdd(game, 0, w0)
            print_result_from_bdd(game, 1, w1)
        else:
            generate_solution_bdd(game, w0, w1)

    elif args.qpz:
        game = ParityGame()
        game.from_parsed(parsed_result)

        qpz = QPZSolver(game)
        (w0, w1) = qpz.solve()

        if args.readable_solution:
            print_result_from_bdd(game, 0, w0)
            print_result_from_bdd(game, 1, w1)
        else:
            generate_solution_bdd(game, w0, w1)

    elif args.spm:
        spm0 = SmallProgressMeasuresSolver(parsed_result, 0)
        (w0, strategy0) = spm0.solve()

        spm1 = SmallProgressMeasuresSolver(parsed_result.create_subgame(set(w0)), 1)
        (w1, strategy1) = spm1.solve()

        if args.readable_solution:
            print_result_from_graph(0, w0, strategy0)
            print_result_from_graph(1, w1, strategy1)
        else:
            generate_solution(w0, w1, strategy0, strategy1)


if __name__ == '__main__':
    main()
