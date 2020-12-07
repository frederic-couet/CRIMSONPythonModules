from CRIMSONCore.PropertyStorage import PropertyStorage

class Scalar(PropertyStorage):
    '''
    A class representing a scalar quantity in a RAD problem
    '''
    def __init__(self):
        PropertyStorage.__init__(self)
        self.properties = [
                {
                    "Diffusion coefficient": 1.1
                },
                {
                    # Set this to true to have residuals be factored in by the flowsolver
                    # (as of Dec. 2020 this is not implemented in the flowsolver and this flag will have no effect)
                    "Residual control": False,
                },
                {
                    "Residual criteria": 0.001,
                    "attributes": {"minimum": 0.0}
                },

            # I am deliberately not including ScalarSymbol as a PropertyStorage property, because it needs special treatment and validation before being renamed,
            # the UI renames the node and checks for duplicates.
            #
            # I could hook into the property changed event, but it seems easier to just not show it in the property tree.
        ]

        # Qt is very heavily invested in Unicode
        self._scalarSymbol = u"new Scalar"
        self._reactionString = u""

    def getScalarSymbol(self):
        return self._scalarSymbol
    
    def setScalarSymbol(self, scalarSymbol):
        self._scalarSymbol = scalarSymbol

    # I made a function for this because I want to show a nicer UI in a separate window
    def getReactionString(self):
        return self._reactionString
    
    def setReactionString(self, reactionString):
        self._reactionString = reactionString