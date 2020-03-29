import sys
from parser.ParityGameParser import ParityGameParser
from zielonka import *
from qpz import *
from spm import *
import argparse


def print_result_from_bdd(game, player, w):
    print("Player " + str(player) + " wins from nodes:")
    models = list(game.bdd.pick_iter(w, care_vars=(game.states)))
    nodes = []
    for m in models:
        f = game.variable_to_identifier(m)
        nodes.append(f)
    print("\t {" + ", ".join(str(n) for n in sorted(nodes, reverse=True)) + "}")


def print_result_from_graph(player, w, strategy = None):
    print("Player " + str(player) + " wins from nodes:")
    print("\t {" + ", ".join(str(n) for n in sorted(w, reverse=True)) + "}")
    steps = []
    if strategy:
        for s in sorted(strategy.keys()):
            steps.append(str(s) + "->" + str(strategy[s]))
    print("with strategy")
    print("\t [" + ",".join(steps) + "]")


def main():
    cmd = argparse.ArgumentParser(prog="solve.py", description="Parity game solver for the Reactive Synthesis lecture")
    g = cmd.add_mutually_exclusive_group(required=True)
    g.add_argument('--zielonka', action='store_true')
    g.add_argument('--fixpoint', action='store_true')
    g.add_argument('--qpz', action='store_true')
    g.add_argument('--spm', action='store_true')
    cmd.add_argument('file', metavar='FILE', type=str)

    args = cmd.parse_args()

    parsed_result = ParityGameParser.parse_file(args.file)
    parsed_result.populate()
    print(parsed_result)

    if args.zielonka:
        game = ParityGame()
        game.from_parsed(parsed_result)

        w0, w1 = zielonka(game)
        print_result_from_bdd(game, 0, w0)
        print_result_from_bdd(game, 1, w1)
    elif args.fixpoint:
        print("Fixpoint is not yet implemented")
    elif args.qpz:
        game = ParityGame()
        game.from_parsed(parsed_result)

        i = game.d % 2
        wi = qpz(game, game.d, game.parsed_pg.size, game.parsed_pg.size)
        wj = game.V & ~wi

        w0 = wi if i == 0 else wj
        w1 = wj if i == 0 else wi

        print_result_from_bdd(game, 0, w0)
        print_result_from_bdd(game, 1, w1)
    elif args.spm:
        spm = SmallProgressMeasuresSolver(parsed_result)
        (v0, v1, strategy0) = spm.solve()
        print_result_from_graph(0, v0, strategy0)
        print_result_from_graph(1, v1)

if __name__ == '__main__':
    main()
