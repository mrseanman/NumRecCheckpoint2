'''
Class to return ChiSquare relating to a dataset in data
for given parameters
'''

from Data import Data
from Function import Function

class ChiSquare(Function):

    def __init__(self, func, dataFileName):
        self.func = func
        self.dataFileName = dataFileName

    def evalChiSquare(self, params):
        data = Data(self.dataFileName)

        runningChi = 0.
        for i in range(data.numData):
            d = (data.data[1][i] - self.func(data.data[0][i], params)) / data.errData[i]
            runningChi += d**2.

        return runningChi
