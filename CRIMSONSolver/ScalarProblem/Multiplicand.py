"""
    A class representing a  multiplicand in a reaction, e.g., III^2 in k3*III^2*I^4 + k2*II + k1*I^3
    I considered making this a PropertyStorage class but the standard property tree will not be very useful for this, I think,
    since really I want to give you a drop down of possible scalar symbols and constants instead of having you type them in manually.
"""
class Multiplicand(object):
    def __init__(self, scalarSymbol, order):
        self._scalarSymbol = scalarSymbol
        self._order = order

    def getScalarSymbol(self):
        return self._scalarSymbol

    def setScalarSymbol(self, scalarSymbol):
        self._scalarSymbol = scalarSymbol
    
    def getOrder(self):
        return self._order

    def setOrder(self, order):
        self._order = order