from ChiSquare import ChiSquare
from Function import Function, ComposeFunction
from Optimise import Optimise

class Organise(object):

    def findParams(self):
        dataFileName = 'testData.txt'

        function = Function()
        chiLinear = ChiSquare(function.evalLinear, dataFileName)
        optimiser = Optimise()

        #m = params[0]
        #c = params[1]
        paramsGuess = [-1., 1.]
        paramsAccuracy = [0.001, 0.001]
        paramsJump = [1., 1.]
        #evals minimum m and c for our ChiSquare
        params = optimiser.min(chiLinear.evalChiSquare, paramsGuess, paramsJump, paramsAccuracy, [])

        chiMinusOne = ComposeFunction(function.minusOne, chiLinear.evalChiSquare)

        rootPramsGuess = [1., 4.]
        rootParamsJump = [0.1, 0.1]
        rootParamsAccuracy = [0.0001, 0.0001]
        mErr = optimiser.root(chiMinusOne.evalCompose, rootPramsGuess, rootParamsJump, rootParamsAccuracy, [1])[0] - params[0]
        rootPramsGuess = [1, 4.]
        cErr = optimiser.root(chiMinusOne.evalCompose, rootPramsGuess, rootParamsJump, rootParamsAccuracy, [0])[1] - params[1]

        print("[m,c] = " + str(params))
        print("m err = " + str(mErr))
        print("c err = " + str(cErr))
