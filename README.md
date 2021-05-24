# gf-python
Utilities to work with GF trees from Python

# Contents

This repository will contain, in the future, code to do many more things.

## Tree transformation

Modules: `treetransform.py` and `ttutils.py`

These modules can take a set of PGF expressions and transform them into other PGF expressions.

### Unsolved problems

How to get the PGF file?

The full grammar is created on the client side from the L4 file, and sent to the Docassemble server.
We need access to the PGF file in order to create the submodule that is used in treetransform.py.

Right now I just put the PGF in `/tmp` and access it from treetransform.py.
Should we hardcode the path that the PGF file will have on the docassemble? Or give the path as an argument?


## Create PGF trees out of the parsed s(CASP)

Modules: none yet

### Unsolved problems

The code doesn't exist yet.

# The general pipeline

- Generate the files in Haskell, on the client side.
- Create an expert system, and move the generated files to Docassemble server.
- Run the interview, get answers from user, and run a query.
- Query produces answers: a set of s(CASP) models. Parse those answers in Python.
- Initial transformation of the s(CASP) (Python) AST into GF trees.
  We need to match the s(CASP) statements in the answer (is_player(A)) to the GF funs (Player : Arg -> Statement).
  Orthographic restrictions:
  * L4 predicates and GF cats+funs can be anything
  * s(CASP) atoms must be lowercase and variables uppercase
  Maybe this needs to be addressed already when we generate the grammar. Make everything lowercase.
- TODO: Get back to L4toSCASP translation and see if it needs to be revised.
