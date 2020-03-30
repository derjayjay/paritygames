# Generated from parity_game.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("@\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\6\t\61\n\t\r\t\16\t\62\3\n")
        buf.write("\6\n\66\n\n\r\n\16\n\67\3\13\6\13;\n\13\r\13\16\13<\3")
        buf.write("\13\3\13\2\2\f\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\3\2\6\3\2\62\63\3\2\62;\4\2C\\c|\5\2\13\f\17\17")
        buf.write("\"\"\2B\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\36\3\2\2\2\7")
        buf.write(" \3\2\2\2\t&\3\2\2\2\13)\3\2\2\2\r+\3\2\2\2\17-\3\2\2")
        buf.write("\2\21\60\3\2\2\2\23\65\3\2\2\2\25:\3\2\2\2\27\30\7r\2")
        buf.write("\2\30\31\7c\2\2\31\32\7t\2\2\32\33\7k\2\2\33\34\7v\2\2")
        buf.write("\34\35\7{\2\2\35\4\3\2\2\2\36\37\7=\2\2\37\6\3\2\2\2 ")
        buf.write("!\7u\2\2!\"\7v\2\2\"#\7c\2\2#$\7t\2\2$%\7v\2\2%\b\3\2")
        buf.write("\2\2&\'\7]\2\2\'(\7$\2\2(\n\3\2\2\2)*\7$\2\2*\f\3\2\2")
        buf.write("\2+,\7.\2\2,\16\3\2\2\2-.\t\2\2\2.\20\3\2\2\2/\61\t\3")
        buf.write("\2\2\60/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62\63\3\2")
        buf.write("\2\2\63\22\3\2\2\2\64\66\t\4\2\2\65\64\3\2\2\2\66\67\3")
        buf.write("\2\2\2\67\65\3\2\2\2\678\3\2\2\28\24\3\2\2\29;\t\5\2\2")
        buf.write(":9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=>\3\2\2\2>?\b")
        buf.write("\13\2\2?\26\3\2\2\2\6\2\62\67<\3\b\2\2")
        return buf.getvalue()


class parity_gameLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    BOOL = 7
    NUMBER = 8
    NAME = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'parity'", "';'", "'start'", "'[\"'", "'\"'", "','" ]

    symbolicNames = [ "<INVALID>",
            "BOOL", "NUMBER", "NAME", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "BOOL", 
                  "NUMBER", "NAME", "WS" ]

    grammarFileName = "parity_game.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


