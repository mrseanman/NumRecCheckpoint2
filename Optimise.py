'''
Class to minimiseChior find roots of given function
'''
import copy
import math
import numpy as np
from Function import Function, ComposeFunction

class Optimise(object):

    def min(self, func, fParamsGuess, paramsJump, paramsAccuracy, paramsToFix):
        params = copy.deepcopy(fParamsGuess)

        numParams = len(params)

        for i in range(numParams):
            for paramIndex in range(numParams - i):
                if not(paramIndex in paramsToFix):
                    params = self.minSingleParam(func, paramIndex, params, paramsJump[paramIndex], paramsAccuracy[paramIndex])
        return params


    def minSingleParam(self, func, freeParamIndex, fParams, freeParamJump, accuracy):
        params = copy.deepcopy(fParams)

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


    def root(self, func, fParamsGuess, paramsJump, paramsAccuracy, paramsToFix):
        params = copy.deepcopy(fParamsGuess)

        numParams = len(params)

        for paramIndex in range(numParams):
            params = self.rootSingleParam(func, paramIndex, params, paramsJump[paramIndex], paramsAccuracy[paramIndex])
        return params


    def rootSingleParam(self, func, freeParamIndex, fParams, freeParamJump, accuracy):
        params = copy.deepcopy(fParams)

        numIter = int(math.ceil(-math.log(accuracy/freeParamJump, 2.)))
        if numIter < 1:
            numIter = 1

        val0 = func(params)
        params[freeParamIndex] += freeParamJump
        val1 = func(params)

        if ((val1 - val0) * np.sign(val0)) == -1 :
            direction = 1.
        else:
            direction = -1.
        val1 = val0
            
        for i in range(numIter):
            val0 = val1
            while np.sign(val0) == np.sign(val1):
                val0 = val1
                params[freeParamIndex] += direction*freeParamJump
                val1 = func(params)

            freeParamJump /= 2.
            direction *= -1

        return params
