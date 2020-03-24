# Generated from parity_game.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\6\b")
        buf.write("*\n\b\r\b\16\b+\3\t\6\t/\n\t\r\t\16\t\60\3\n\6\n\64\n")
        buf.write("\n\r\n\16\n\65\3\n\3\n\2\2\13\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\3\2\6\3\2\62\63\3\2\62;\3\2c|\5\2\13")
        buf.write("\f\17\17\"\"\2;\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5\34\3\2\2\2\7\36\3")
        buf.write("\2\2\2\t!\3\2\2\2\13$\3\2\2\2\r&\3\2\2\2\17)\3\2\2\2\21")
        buf.write(".\3\2\2\2\23\63\3\2\2\2\25\26\7r\2\2\26\27\7c\2\2\27\30")
        buf.write("\7t\2\2\30\31\7k\2\2\31\32\7v\2\2\32\33\7{\2\2\33\4\3")
        buf.write("\2\2\2\34\35\7=\2\2\35\6\3\2\2\2\36\37\7]\2\2\37 \7$\2")
        buf.write("\2 \b\3\2\2\2!\"\7$\2\2\"#\7_\2\2#\n\3\2\2\2$%\7.\2\2")
        buf.write("%\f\3\2\2\2&\'\t\2\2\2\'\16\3\2\2\2(*\t\3\2\2)(\3\2\2")
        buf.write("\2*+\3\2\2\2+)\3\2\2\2+,\3\2\2\2,\20\3\2\2\2-/\t\4\2\2")
        buf.write(".-\3\2\2\2/\60\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\22")
        buf.write("\3\2\2\2\62\64\t\5\2\2\63\62\3\2\2\2\64\65\3\2\2\2\65")
        buf.write("\63\3\2\2\2\65\66\3\2\2\2\66\67\3\2\2\2\678\b\n\2\28\24")
        buf.write("\3\2\2\2\6\2+\60\65\3\b\2\2")
        return buf.getvalue()


class parity_gameLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    BOOL = 6
    NUMBER = 7
    NAME = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'parity'", "';'", "'[\"'", "'\"]'", "','" ]

    symbolicNames = [ "<INVALID>",
            "BOOL", "NUMBER", "NAME", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "BOOL", "NUMBER", 
                  "NAME", "WS" ]

    grammarFileName = "parity_game.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


