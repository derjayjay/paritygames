grammar parity_game;

game:           preamble node+;
preamble:       'parity' NUMBER ';';
node:           identifier parity owner successors ('["' NAME '"]')? ';';
successors:     successor (',' successor)*;
owner:          BOOL;
identifier:     BOOL|NUMBER;
parity:         BOOL|NUMBER;
successor:      BOOL|NUMBER;

BOOL:           [0-1];
NUMBER:         [0-9]+;


NAME:           [a-z]+;

WS : [ \t\r\n]+ -> skip ;