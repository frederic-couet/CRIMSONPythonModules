# source automatically generated for Python class "SolverIteration"
# using GenerateNewSolverObject.
#
# Generated on 2020-10-23 14:42:43.123000

from CRIMSONCore.PropertyStorage import PropertyStorage

'''
    A class representing one solver iteration as part of a timestep
'''
class SolverIteration(PropertyStorage):

    def __init__(self):
        PropertyStorage.__init__(self)
        self.properties = [
            {
                "Solver": "Fluid"
            },
            {
                "Number of iterations": 1
            }
        ]