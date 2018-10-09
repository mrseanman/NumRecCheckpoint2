'''
Class to minimise a given function
'''

import math
from ChiSquare import ChiSquare

class MinimiseChi(ChiSquare):

    #this uses the fact that chiSquare has a minimum for param[0]
    #along the line of param[1]
    def minimiseChi(self, paramsGuess, paramsJump, paramsAccuracy):
        numParams = len(paramsGuess)
        params = paramsGuess
        for paramIndex in range(numParams):
            params = self.minChiSingleParam(params, paramIndex, paramsJump[paramIndex], paramsAccuracy[paramIndex])

        return params

    def minChiSingleParam(self, params, freeParamIndex, freeParamJump, accuracy):

        numIter = int(math.ceil(-math.log(accuracy, 2.)))
        if numIter < 1:
            numIter = 1

        direction = 1
        chi0 = self.evalChiSquare(params)
        params[freeParamIndex] += direction*freeParamJump
        chi1 = self.evalChiSquare(params)

        if chi1 <= chi0:
            direction = 1.
        else:
            direction = -1.

        for i in range(numIter):
            changeDir = False
            while not(changeDir):
                chi0 = chi1
                params[freeParamIndex] += direction*freeParamJump
                chi1 = self.evalChiSquare(params)
                if chi1 > chi0:
                    changeDir = True
            freeParamJump /= 2.
            direction *= -1.

        return params
