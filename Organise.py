from ChiSquare import ChiSquare
from NLL import NLL
from Function import Function, ComposeFunction
from Optimise import Optimise
import numpy as np
import matplotlib.pylab as pl

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

        self.plotChiAroundMin(chiLinear.evalChiSquare, params, [mErrPos, cErrPos], [mErrNeg, cErrNeg])


    def plotChiAroundMin(self, chiEval, minParams, errPosParams, errNegParams):
        numOfXPoints = 200

        minM = minParams[0]
        minC = minParams[1]
        mErrPos = errPosParams[0]
        cErrPos = errPosParams[1]
        mErrNeg = errNegParams[0]
        cErrNeg = errNegParams[1]

        minChi = chiEval(minParams)

        mWidth = 2 * mErrPos
        cWidth = 2 * cErrPos
        paramPlotWidths = [mWidth, cWidth]

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

        #centers mRange and cRange around minimum
        mRange -= minM
        cRange -= minC

        pl.title(r"$\Delta m$ vs. $\Delta \chi ^{2}$ about minimum")
        pl.xlabel(r"$\Delta m$")
        pl.ylabel("$\Delta \chi ^{2}$")
        pl.axvline(x = mErrPos, linestyle=':', color='r')
        pl.axvline(x = -mErrNeg, linestyle=':', color='r')
        pl.plot(mRange, mVals)
        pl.show()

        pl.title(r"$\Delta c$ vs. $\Delta \chi ^{2}$ about minimum")
        pl.xlabel(r"$\Delta c$")
        pl.ylabel("$\Delta \chi ^{2}$")
        pl.axvline(x = cErrPos, linestyle=':', color='r')
        pl.axvline(x = -cErrNeg, linestyle=':', color='r')
        pl.plot(cRange, cVals)
        pl.show()

    def findNLLParams(self, dataFileName):
        function = Function()
        NLLExp = NLL(function.expPDF, dataFileName)
        optimiser = Optimise()

        paramsGuess = [2.]
        paramsJump = [0.01]
        paramsAccuracy = [0.00001]
        params = optimiser.min(NLLExp.evalNLL, paramsGuess, paramsJump, paramsAccuracy, [])

        tauMin = params[0]
        minNll = NLLExp.evalNLL(params)

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

        self.plotNLLAroundMin(NLLExp.evalNLL, params, [tauErrPos], [tauErrNeg])

    def plotNLLAroundMin(self, NLLEval, minParams, errPosParams, errNegParams):
        numOfXPoints = 200

        minTau = minParams[0]
        tauErrPos = errPosParams[0]
        tauErrNeg = errNegParams[0]

        minNLL = NLLEval([minTau])

        tauWidth = 2 * tauErrPos
        minPlotTau = minTau - tauWidth
        maxPlotTau = minTau + tauWidth

        tauRange = np.linspace(minPlotTau, maxPlotTau, numOfXPoints)

        NLLVals = []

        for tau in tauRange:
            NLLVals.append(NLLEval([tau]) - minNLL)

        #centers tauRange around tauMin
        tauRange -= minTau

        pl.title(r"$\Delta \tau$ vs. $\Delta NLL$ about minimum")
        pl.xlabel(r"$\Delta \tau$")
        pl.ylabel("$\Delta NLL$")
        pl.axvline(x = tauErrPos, linestyle=':', color='r')
        pl.axvline(x = -tauErrNeg, linestyle=':', color='r')
        pl.plot(tauRange, NLLVals)
        pl.show()
