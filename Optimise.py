'''
Class to minimiseChior find roots of given function
'''
import copy
import math
from Function import Function, ComposeFunction

class Optimise(object):
    def min(self, func, paramsGuess, paramsJump, paramsAccuracy, paramsToFix):
        numParams = len(paramsGuess)
        params = paramsGuess
        for paramIndex in range(numParams):
            if not(paramIndex in paramsToFix):
                params = self.minSingleParam(func, paramIndex, params, paramsJump[paramIndex], paramsAccuracy[paramIndex])

        return params

    def minSingleParam(self, func, freeParamIndex, paramsF, freeParamJump, accuracy):
        params = copy.deepcopy(paramsF)

        numIter = int(math.ceil(-math.log(accuracy/freeParamJump, 2.)))
        if numIter < 1:
            numIter = 1

        val0 = func(params)
        params[freeParamIndex] += freeParamJump
        val1 = func(params)

        if val1 <= val0:
            direction = 1.
        else:
            direction = -1.

        val1 = val0

        for i in range(numIter):
            changeDir = False
            while not(changeDir):
                val0 = val1
                params[freeParamIndex] += direction*freeParamJump
                val1 = func(params)
                if val1 > val0:
                    changeDir = True
            freeParamJump /= 2.
            direction *= -1.

        return params

    #find the minimum of abs(func) so not really a root
    #but it tries its best
    def root(self, func, paramsGuess, paramsJump, paramsAccuracy, paramsToFix):
        composeFuncAbs = ComposeFunction(abs, func)
        params = self.min(composeFuncAbs.evalCompose, paramsGuess, paramsJump, paramsAccuracy, paramsToFix)
        return params
