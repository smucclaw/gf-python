import gf_python.treetransform as tt
import gf_python.ttutils as ttutils

#### Test data
## We parse these with the GF grammar

aRock_cScissors = [
   "A wins RPS",
   "RPS is a game",
   "A is a participant in RPS",
   "A is a player",
   "A throws rock",
   "C is a player",
   "C is a participant in RPS",
   "C throws scissors",
   "rock beats scissors",
]

aScissors_cPaper = [
   "A wins RPS",
   "RPS is a game",
   "A is a participant in RPS",
   "A is a player",
   "A throws scissors",
   "C is a player",
   "C is a participant in RPS",
   "C throws paper",
   "scissors beats paper",
]


aPaper_cRock = [
   "A wins RPS",
   "RPS is a game",
   "A is a participant in RPS",
   "A is a player",
   "A throws paper",
   "C is a player",
   "C is a participant in RPS",
   "C throws rock",
   "paper beats rock",
]

def getExpr(sentence):
    try:
        i = tt.eng.parse(sentence)
    except Exception:
        raise Exception("getExpr: sentence not parsed: " + sentence)
    prob,expr = next(i)
    return expr

testCorpus = [aRock_cScissors, aScissors_cPaper, aPaper_cRock]

parsedTestCorpus = [
    [getExpr(s) for s in model]
    for model in testCorpus]

R = tt.gr.embed("AnswerTop")

###### Main

if __name__ == "__main__":
    print(tt.nlgModels(parsedTestCorpus))


################# TESTS #################
## Some rudimentary tests.
## TODO: use a real testing framework?

def samePred(expr1, expr2):
    e1p = ttutils.getPred(expr1)
    e2p = ttutils.getPred(expr2)
    return e1p == e2p
samePredTrue = samePred(getExpr("A is a player"), getExpr("C is a player"))
assert samePredTrue == True

samePredFalse = samePred(getExpr("A is a player"), getExpr("C is a game"))
assert samePredFalse == False

def sameSubj(expr1, expr2):
    e1s = ttutils.getSubj(expr1)
    e2s = ttutils.getSubj(expr2)
    return e1s == e2s

sameSubjSimpleTrue = sameSubj(getExpr("A is a participant in RPS"), getExpr("A is a player"))
assert sameSubjSimpleTrue == True

sameSubjSimpleFalse = sameSubj(getExpr("A is a participant in RPS"), getExpr("B is a player"))
assert sameSubjSimpleFalse == False

sameSubjComplexTrue = sameSubj(getExpr("A and C are participants in RPS"), getExpr("A and C are players"))
assert sameSubjComplexTrue == True

sameSubjComplexFalse = sameSubj(getExpr("A and C are participants in RPS"), getExpr("A and B are players"))
assert sameSubjComplexFalse == False


def nlgSingleModel(model):
    conclusion, evidence = model[0], model[1:]
    firstAggr = tt.aggregateByPredicate(evidence)
    secondAggr = tt.aggregateBySubject(firstAggr)
    finalExpr = R.IfThen(conclusion, (tt.wrapStatement(R.Bullets, secondAggr)))
    return tt.prettyLin(finalExpr)

aRock_cScissors_gold = """A wins RPS if
* A throws rock,
* C throws scissors,
* RPS is a game,
* rock beats scissors and
* A and C are players and participants in RPS"""

aRock_cScissors_system = nlgSingleModel(parsedTestCorpus[0])

assert aRock_cScissors_system == aRock_cScissors_gold
