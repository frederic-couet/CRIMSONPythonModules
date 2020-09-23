from CRIMSONCore.PropertyStorage import PropertyStorage
from CRIMSONSolver.ScalarProblem.ScalarBC import ScalarBC


class Scalar(PropertyStorage):
    '''
    A class representing a scalar quantity in a RAD problem
    '''
    def __init__(self):
        PropertyStorage.__init__(self)
        self.properties = [
            {
                "Diffusion coefficient": 0.0
            },
            {
                # Qt is very heavily invested in Unicode, so this will only work if it's initialized with a unicode literal
                "ScalarSymbol":u'My Scalar'
            }
        ]