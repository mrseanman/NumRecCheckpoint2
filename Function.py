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

    def minusOne(self, x):
        return x - 1.

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
