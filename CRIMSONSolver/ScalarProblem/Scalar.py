from CRIMSONCore.PropertyStorage import PropertyStorage
from CRIMSONSolver.ScalarProblem.ScalarBC import ScalarBC


class Scalar(PropertyStorage):
    '''
    A class representing a scalar quantity in a RAD problem
    '''
    def __init__(self):
        PropertyStorage.__init__(self)
        # Where self.BCs[<faceIdentifier>] = <Instance of ScalarBC>
        self.BCs = {}
        self.properties = [
            {
                "Initial value": 0.0
            },
            {
                "Diffusion coefficient": 0.0
            },
            {
                # Qt is very heavily invested in Unicode, so this will only work if it's initialized with a unicode literal
                "ScalarSymbol":u'My Scalar'
            }
        ]

    def setBC(self, faceIdentifier, scalarBC):  # for use in CPP code
        self.BCs[faceIdentifier] = scalarBC

    def getBC(self, faceIdentifier):  # for use in CPP code
        return self.BCs[faceIdentifier]