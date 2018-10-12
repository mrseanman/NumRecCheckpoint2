'''
Returns the value of a function for a given set
of independent variables
'''
import numpy as np

class Function(object):

    #m = params[0]
    #c = params[1]
    def evalLinear(self, x, params):
        return params[0]*x + params[1]

    #tau = params[0]
    def expPDF(self, x , params):
        tau = params[0]
        return 1./tau * np.exp(-x / tau)

    #x = params[0]
    def polyNomial(self, params):
        x = params[0]
        return x**2. - 2.


'''
Creates an instance of a class that is useful for evaluating a compsition
of 2 functions in Function (or in python libraries)
'''
class ComposeFunction(object):
    def __init__(self, funcToCompose, funcInitial):
        self.funcInitial = funcInitial
        self.funcToCompose = funcToCompose

    def evalCompose(self, params):
        return self.funcToCompose(self.funcInitial(params))

class AddFunction(object):
    def __init__(self, addX):
        self.addX = addX

    def evalAdd(self, a):
        return a + self.addX
