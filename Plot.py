import numpy as np
import matplotlib.pylab as pl

'''
Plotting methods
'''
class Plot(object):

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

        #Stores y values for plot
        mVals = []
        cVals = []

        for m in mRange:
            mVals.append(chiEval([m, minC]) - minChi)
        for c in cRange:
            cVals.append(chiEval([minM, c]) - minChi)

        #centers mRange and cRange around minimum
        mRange -= minM
        cRange -= minC

        #delta chiSquare by delta m
        pl.title(r"$\Delta m$ vs. $\Delta \chi ^{2}$ about minimum")
        pl.xlabel(r"$\Delta m$")
        pl.ylabel("$\Delta \chi ^{2}$")
        pl.axvline(x = mErrPos, linestyle=':', color='r')
        pl.axvline(x = -mErrNeg, linestyle=':', color='r')
        pl.axhline(y = 1., linewidth=0.5, linestyle='--', color='dimgray')
        pl.plot(mRange, mVals)
        pl.show()

        #delta chisquare by delta c
        pl.title(r"$\Delta c$ vs. $\Delta \chi ^{2}$ about minimum")
        pl.xlabel(r"$\Delta c$")
        pl.ylabel("$\Delta \chi ^{2}$")
        pl.axvline(x = cErrPos, linestyle=':', color='r')
        pl.axvline(x = -cErrNeg, linestyle=':', color='r')
        pl.axhline(y = 1., linewidth=0.5, linestyle='--', color='dimgray')
        pl.plot(cRange, cVals)
        pl.show()

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

        #stores y values
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
        pl.axhline(y = 0.5, linewidth=0.5, linestyle='--', color='dimgray')
        pl.plot(tauRange, NLLVals)
        pl.show()
