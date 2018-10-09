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
