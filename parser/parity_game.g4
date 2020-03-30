grammar parity_game;

game:           preamble start? node+;
preamble:       'parity' NUMBER ';';
start:          'start' start_node ';';
node:           identifier parity owner successors ('["' NAME '"')? ';';
successors:     successor (',' successor)*;
owner:          BOOL;
identifier:     BOOL|NUMBER;
parity:         BOOL|NUMBER;
successor:      BOOL|NUMBER;
start_node:     BOOL|NUMBER;

BOOL:           [0-1];
NUMBER:         [0-9]+;


NAME:           [a-zA-Z]+;

WS : [ \t\r\n]+ -> skip ;