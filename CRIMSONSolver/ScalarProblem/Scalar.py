from CRIMSONCore.PropertyStorage import PropertyStorage
from CRIMSONSolver.ScalarProblem.ScalarBC import ScalarBC


class Scalar(PropertyStorage):
    '''
    Base class for all face-attached data classes (e.g. boundary conditions and materials).

    In addition to having the functionality of a :mod:`PropertyStorage <CRIMSONCore.PropertyStorage>`, the face data
    also stores a list of :mod:`face identifiers <CRIMSONCore.FaceIdentifier>` stored in ``FaceData.faceIdentifiers``
    which are filled by the C++ code through user interaction.

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