# Engineering Notebook

#### Sat, Mar 22

Which part of the program did you work on? 

* recap on the material provided in the lecture
* some preliminary research
* familiarize myself with the dd python package

What was the goal?

* getting started

What was the result?

* found a paper on working with BDDs for parity game solving [1]
* set up the project repo

#### Sun, Mar 23

Which part of the program did you work on? 

* parser for pgSolver parity game format
* BDD-based parity game encoding

What was the goal?

* tweak the provided antlr4 grammar for easier parsing
* learn how to encode the different sets and relations of a parity game in BDDs

What ws the result?

* got the parse running and implemented data structures to represent the parsed information
* a basic data structure for storing parity games in BDDs
    * enconding of states as conjunction of boolean variables
    * transition relation as implications on the encoded variables
    * set as disjunctions of the encoded variables
    
#### Mon, Mar 24

Which part of the program did you work on? 

* attractor computation
* Zielonka's algorithm

What was the goal?

* solving a given parity game with Zielonka at the end of the day

What ws the result?

* implemented the algorithms as described on the lecture slides
* impleneted a way to extract the required stated information from a given BDD

#### Tue, Mar 25

Which part of the program did you work on? 

* command line arguments
* printing of results according to specification

What was the goal?

* having the program usable from the command line to automatically test implementation against test set 
and compare with pgsolver

What ws the result?

* the Zielonka algorithm implementation seems to be working 




#### Resources 
[1] [A comparison of BDD-based parity game solvers](https://arxiv.org/pdf/1809.03097.pdf)