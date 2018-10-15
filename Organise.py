from ChiSquare import ChiSquare
from NLL import NLL
from Function import Function, ComposeFunction
from Optimise import Optimise
from Plot import Plot
import numpy as np

'''
Moves around values and calls methods in Optimise class
'''
class Organise(object):

    def findChiParams(self):
        dataFileName = 'testData.txt'
        function = Function()
        chiLinear = ChiSquare(function.evalLinear, dataFileName)
        optimiser = Optimise()

        #m = params[0]
        #c = params[1]
        paramsGuess = [0., 1.]
        paramsAccuracy = [0.000000001, 0.000000001]
        paramsJump = [1., 1.]
        #evals minimum m and c for our ChiSquare
        params = optimiser.min(chiLinear.evalChiSquare, paramsGuess, paramsJump, paramsAccuracy, [])

        minM = params[0]
        minC = params[1]
        minChi = chiLinear.evalChiSquare(params)

        #finding err of values in params by finding where the chiSquare
        #increases by 1 either side of the minimum
        mRootParamGuess = [minM + 1., minC]
        cRootParamGuess = [minM, minC + 1.]
        rootParamsJump = [0.0001, 0.001]
        rootParamsAccuracy = [0.000001, 0.000001]
        mErrPos = abs(optimiser.equalTo((minChi + 1), chiLinear.evalChiSquare, mRootParamGuess, rootParamsJump, rootParamsAccuracy, [1])[0] - minM)
        cErrPos = abs(optimiser.equalTo((minChi + 1), chiLinear.evalChiSquare, cRootParamGuess, rootParamsJump, rootParamsAccuracy, [0])[1] - minC)
        mErrNeg = abs(optimiser.equalTo((minChi + 1), chiLinear.evalChiSquare, [minM - mErrPos, minC], rootParamsJump, rootParamsAccuracy, [1])[0] - minM)
        cErrNeg = abs(optimiser.equalTo((minChi + 1), chiLinear.evalChiSquare, [minM, minC - cErrPos], rootParamsJump, rootParamsAccuracy, [0])[1] - minC)

        mErrMean = (mErrPos + mErrNeg)/2.
        cErrMean = (cErrPos + cErrNeg)/2.

        print("")
        print("[m,c]:\t" + str(params) + "\n")
        print("mErr:\t+" + str(mErrPos) + "\t-" + str(mErrNeg))
        print("mean:\t" + str(mErrMean) + "\n")
        print("cErr:\t+" + str(cErrPos) + "\t-" + str(cErrNeg))
        print("Mean:\t" + str(cErrMean))
        print("")

        #self.plotChiAroundMin(chiLinear.evalChiSquare, params, [mErrPos, cErrPos], [mErrNeg, cErrNeg])
        plotter = Plot()
        plotter.plotChiAroundMin(chiLinear.evalChiSquare, params, [mErrPos, cErrPos], [mErrNeg, cErrNeg])

    def findNLLParams(self, dataFileName):
        function = Function()
        NLLExp = NLL(function.expPDF, dataFileName)
        optimiser = Optimise()

        #finds minimum tau for our NLL
        paramsGuess = [2.]
        paramsJump = [0.01]
        paramsAccuracy = [0.00001]
        params = optimiser.min(NLLExp.evalNLL, paramsGuess, paramsJump, paramsAccuracy, [])

        tauMin = params[0]
        minNll = NLLExp.evalNLL(params)

        #finding err of tau in params by finding where the chiSquare
        #increases by 0.5 either side of the minimum
        tauRootGuess = [tauMin]
        tauRootJump = [0.001]
        tauRootAccuracy = [0.00001]
        tauErrPos = abs(optimiser.equalTo((minNll + 0.5), NLLExp.evalNLL, tauRootGuess, tauRootJump, tauRootAccuracy, [])[0] - tauMin)
        tauErrNeg = abs(optimiser.equalTo((minNll + 0.5), NLLExp.evalNLL, [tauMin-tauErrPos], tauRootJump, tauRootAccuracy, [])[0] - tauMin)
        tauErrMean = (tauErrPos + tauErrNeg)/2.

        print("")
        print("tau:\t" + str(tauMin) + "\n")
        print("tauErr:\t+" + str(tauErrPos) + "\t-" + str(tauErrNeg))
        print("mean:\t" + str(tauErrMean))
        print("")

        #self.plotNLLAroundMin(NLLExp.evalNLL, params, [tauErrPos], [tauErrNeg])
        plotter = Plot()
        plotter.plotNLLAroundMin(NLLExp.evalNLL, params, [tauErrPos], [tauErrNeg])
