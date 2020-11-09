from CRIMSONCore.PropertyStorage import PropertyStorage

class Scalar(PropertyStorage):
    '''
    A class representing a scalar quantity in a RAD problem
    '''
    def __init__(self):
        PropertyStorage.__init__(self)
        self.properties = [
            {
                "Diffusion coefficient": 0.0,

            }

            # I am deliberately not including ScalarSymbol as a PropertyStorage property, because it needs special treatment and validation before being renamed,
            # if the symbol is already in use by a reaction, it needs to rename the symbol in all the reactions in the scalar problem.
            #
            # I could hook into the property changed event, but it seems easier to just not show it in the property tree.
        ]

        # Qt is very heavily invested in Unicode
        self._scalarSymbol = u"new Scalar"

    def getScalarSymbol(self):
        return self._scalarSymbol
    
    def setScalarSymbol(self, scalarSymbol):
        self._scalarSymbol = scalarSymbol