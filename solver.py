import sys
from parser.ParityGameParser import ParityGameParser
from attractor import *
from zielonka import *
from dd import autoref as _bdd


def main(argv):
    #txt = ("parity 9; 0 6 1 3,4; 1 5 0 3,8; 2 4 1 4,8; 3 3 0 1,6; 4 2 1 2,4; 5 2 1 5,7; 6 1 0 3,6; 7 1 1 1,5; 8 0 1 0,8;")
    #txt = ("parity 7; 0 5 1 1; 1 6 0 3,5; 2 4 0 1; 3 1 1 0,4; 4 2 1 1,6; 5 3 1 2,4; 6 2 0 3,5;")
    #txt = ("parity 2; 0 2 0 2;  1 3 1 1,2; 2 2 0 0;")
    txt = ("parity 8;"
            "0 0 0 1,2;"
            "1 1 1 2,3;"
            "2 0 0 3,4;"
            "3 1 1 4,5;"
            "4 0 0 5,6;"
            "5 1 1 6,7;"
            "6 0 0 7,0;"
            "7 1 1 0,1;")
    parsed_result = ParityGameParser.parse_string(txt)
    parsed_result.populate()
    print(parsed_result)
    game = ParityGame()
    game.from_parsed(parsed_result)

    w0, w1 = zielonka(game)

    print("w0")
    models = list(game.bdd.pick_iter(w0, care_vars=(game.states)))
    for m in models:
        f = game.variable_to_identifier(m)
        print('\t' + str(f))

    print("w1")
    models = list(game.bdd.pick_iter(w1, care_vars=(game.states)))
    for m in models:
        f = game.variable_to_identifier(m)
        print('\t' + str(f))




if __name__ == '__main__':
    main(sys.argv)
