# Generated from parity_game.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("E\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\5\2\31\n\2\3\2")
        buf.write("\6\2\34\n\2\r\2\16\2\35\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5/\n\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\7\6\66\n\6\f\6\16\69\13\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24")
        buf.write("\2\3\3\2\t\n\2>\2\26\3\2\2\2\4\37\3\2\2\2\6#\3\2\2\2\b")
        buf.write("\'\3\2\2\2\n\62\3\2\2\2\f:\3\2\2\2\16<\3\2\2\2\20>\3\2")
        buf.write("\2\2\22@\3\2\2\2\24B\3\2\2\2\26\30\5\4\3\2\27\31\5\6\4")
        buf.write("\2\30\27\3\2\2\2\30\31\3\2\2\2\31\33\3\2\2\2\32\34\5\b")
        buf.write("\5\2\33\32\3\2\2\2\34\35\3\2\2\2\35\33\3\2\2\2\35\36\3")
        buf.write("\2\2\2\36\3\3\2\2\2\37 \7\3\2\2 !\7\n\2\2!\"\7\4\2\2\"")
        buf.write("\5\3\2\2\2#$\7\5\2\2$%\5\24\13\2%&\7\4\2\2&\7\3\2\2\2")
        buf.write("\'(\5\16\b\2()\5\20\t\2)*\5\f\7\2*.\5\n\6\2+,\7\6\2\2")
        buf.write(",-\7\13\2\2-/\7\7\2\2.+\3\2\2\2./\3\2\2\2/\60\3\2\2\2")
        buf.write("\60\61\7\4\2\2\61\t\3\2\2\2\62\67\5\22\n\2\63\64\7\b\2")
        buf.write("\2\64\66\5\22\n\2\65\63\3\2\2\2\669\3\2\2\2\67\65\3\2")
        buf.write("\2\2\678\3\2\2\28\13\3\2\2\29\67\3\2\2\2:;\7\t\2\2;\r")
        buf.write("\3\2\2\2<=\t\2\2\2=\17\3\2\2\2>?\t\2\2\2?\21\3\2\2\2@")
        buf.write("A\t\2\2\2A\23\3\2\2\2BC\t\2\2\2C\25\3\2\2\2\6\30\35.\67")
        return buf.getvalue()


class parity_gameParser ( Parser ):

    grammarFileName = "parity_game.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'parity'", "';'", "'start'", "'[\"'", 
                     "'\"'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BOOL", "NUMBER", 
                      "NAME", "WS" ]

    RULE_game = 0
    RULE_preamble = 1
    RULE_start = 2
    RULE_node = 3
    RULE_successors = 4
    RULE_owner = 5
    RULE_identifier = 6
    RULE_parity = 7
    RULE_successor = 8
    RULE_start_node = 9

    ruleNames =  [ "game", "preamble", "start", "node", "successors", "owner", 
                   "identifier", "parity", "successor", "start_node" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    BOOL=7
    NUMBER=8
    NAME=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class GameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def preamble(self):
            return self.getTypedRuleContext(parity_gameParser.PreambleContext,0)


        def start(self):
            return self.getTypedRuleContext(parity_gameParser.StartContext,0)


        def node(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parity_gameParser.NodeContext)
            else:
                return self.getTypedRuleContext(parity_gameParser.NodeContext,i)


        def getRuleIndex(self):
            return parity_gameParser.RULE_game

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGame" ):
                listener.enterGame(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGame" ):
                listener.exitGame(self)




    def game(self):

        localctx = parity_gameParser.GameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_game)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.preamble()
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==parity_gameParser.T__2:
                self.state = 21
                self.start()


            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.node()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==parity_gameParser.BOOL or _la==parity_gameParser.NUMBER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreambleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(parity_gameParser.NUMBER, 0)

        def getRuleIndex(self):
            return parity_gameParser.RULE_preamble

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreamble" ):
                listener.enterPreamble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreamble" ):
                listener.exitPreamble(self)




    def preamble(self):

        localctx = parity_gameParser.PreambleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_preamble)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(parity_gameParser.T__0)
            self.state = 30
            self.match(parity_gameParser.NUMBER)
            self.state = 31
            self.match(parity_gameParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def start_node(self):
            return self.getTypedRuleContext(parity_gameParser.Start_nodeContext,0)


        def getRuleIndex(self):
            return parity_gameParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = parity_gameParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(parity_gameParser.T__2)
            self.state = 34
            self.start_node()
            self.state = 35
            self.match(parity_gameParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(parity_gameParser.IdentifierContext,0)


        def parity(self):
            return self.getTypedRuleContext(parity_gameParser.ParityContext,0)


        def owner(self):
            return self.getTypedRuleContext(parity_gameParser.OwnerContext,0)


        def successors(self):
            return self.getTypedRuleContext(parity_gameParser.SuccessorsContext,0)


        def NAME(self):
            return self.getToken(parity_gameParser.NAME, 0)

        def getRuleIndex(self):
            return parity_gameParser.RULE_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode" ):
                listener.enterNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode" ):
                listener.exitNode(self)




    def node(self):

        localctx = parity_gameParser.NodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_node)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.identifier()
            self.state = 38
            self.parity()
            self.state = 39
            self.owner()
            self.state = 40
            self.successors()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==parity_gameParser.T__3:
                self.state = 41
                self.match(parity_gameParser.T__3)
                self.state = 42
                self.match(parity_gameParser.NAME)
                self.state = 43
                self.match(parity_gameParser.T__4)


            self.state = 46
            self.match(parity_gameParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuccessorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def successor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(parity_gameParser.SuccessorContext)
            else:
                return self.getTypedRuleContext(parity_gameParser.SuccessorContext,i)


        def getRuleIndex(self):
            return parity_gameParser.RULE_successors

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuccessors" ):
                listener.enterSuccessors(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuccessors" ):
                listener.exitSuccessors(self)




    def successors(self):

        localctx = parity_gameParser.SuccessorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_successors)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.successor()
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==parity_gameParser.T__5:
                self.state = 49
                self.match(parity_gameParser.T__5)
                self.state = 50
                self.successor()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OwnerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(parity_gameParser.BOOL, 0)

        def getRuleIndex(self):
            return parity_gameParser.RULE_owner

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOwner" ):
                listener.enterOwner(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOwner" ):
                listener.exitOwner(self)




    def owner(self):

        localctx = parity_gameParser.OwnerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_owner)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(parity_gameParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(parity_gameParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(parity_gameParser.NUMBER, 0)

        def getRuleIndex(self):
            return parity_gameParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = parity_gameParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not(_la==parity_gameParser.BOOL or _la==parity_gameParser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParityContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(parity_gameParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(parity_gameParser.NUMBER, 0)

        def getRuleIndex(self):
            return parity_gameParser.RULE_parity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParity" ):
                listener.enterParity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParity" ):
                listener.exitParity(self)




    def parity(self):

        localctx = parity_gameParser.ParityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not(_la==parity_gameParser.BOOL or _la==parity_gameParser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuccessorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(parity_gameParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(parity_gameParser.NUMBER, 0)

        def getRuleIndex(self):
            return parity_gameParser.RULE_successor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuccessor" ):
                listener.enterSuccessor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuccessor" ):
                listener.exitSuccessor(self)




    def successor(self):

        localctx = parity_gameParser.SuccessorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_successor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not(_la==parity_gameParser.BOOL or _la==parity_gameParser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_nodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(parity_gameParser.BOOL, 0)

        def NUMBER(self):
            return self.getToken(parity_gameParser.NUMBER, 0)

        def getRuleIndex(self):
            return parity_gameParser.RULE_start_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_node" ):
                listener.enterStart_node(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_node" ):
                listener.exitStart_node(self)




    def start_node(self):

        localctx = parity_gameParser.Start_nodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_start_node)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            _la = self._input.LA(1)
            if not(_la==parity_gameParser.BOOL or _la==parity_gameParser.NUMBER):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





