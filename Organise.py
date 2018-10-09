from MinimiseChi import MinimiseChi
from Function import Function

class Organise(object):

    def findParams(self):
        dataFileName = "testData.txt"
        paramsGuess = [-1., 1.]
        paramsAccuracy = [0.001, 0.001]
        paramsJump = [1., 1.]


        function = Function()
        minimiseLinear = MinimiseChi(function.evalLinear, "testData.txt")

        params = minimiseLinear.minimiseChi(paramsGuess, paramsJump, paramsAccuracy)

        print(params)
