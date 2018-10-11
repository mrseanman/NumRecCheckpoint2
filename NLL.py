'''
To return NLL for certain parameters of a certain PDF and dataset
'''

from data import Data
from Function import Function
import math

class NLL(Function):

    def __init__(self, pdf, dataFileName):
        self.pdf = pdf
        self.dataFileName = dataFileName

    def evalNLL(self, params):
        data = Data(self.dataFileName)

        runningNLL = 0.

        for i in range(data.numData):
            L = -math.log(self.pdf(data.data[0][i], params))
            runningNLL +=   L

        return runningNLL
