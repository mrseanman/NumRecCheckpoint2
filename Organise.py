from ChiSquare import ChiSquare
from Function import Function, ComposeFunction
from Optimise import Optimise
import numpy as np
import matplotlib.pylab as pl

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

        mWidth = 0.005
        cWidth = 0.05
        paramPlotWidths = [mWidth, cWidth]

        self.plotChiAroundMin(chiLinear.evalChiSquare, params, paramPlotWidths)




    def plotChiAroundMin(self, chiEval, minParams, paramPlotWidths):
        numOfXPoints = 200

        minM = minParams[0]
        minC = minParams[1]

        minChi = chiEval(minParams)

        minPlotM = minM - paramPlotWidths[0]
        maxPlotM = minM + paramPlotWidths[0]
        minPlotC = minC - paramPlotWidths[1]
        maxPlotC = minC + paramPlotWidths[1]

        mRange = np.linspace(minPlotM, maxPlotM, numOfXPoints)
        cRange = np.linspace(minPlotC, maxPlotC, numOfXPoints)

        mVals = []
        cVals = []

        for m in mRange:
            mVals.append(chiEval([m, minC]) - minChi)
        for c in cRange:
            cVals.append(chiEval([minM, c]) - minChi)

        pl.plot(mRange, mVals)
        pl.show()

        pl.plot(cRange, cVals)
        pl.show()
