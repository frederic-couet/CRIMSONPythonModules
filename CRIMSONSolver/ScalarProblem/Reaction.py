from __future__ import print_function

# Notes:
#   -   I am typically not an advocate of getters and setters for the sake of "style", but in this case I assume that 
#       an alternative implementation of these classes may benefit from overriding these getters and setters
#       to change how a scalar's configuration is retrieved. That's also why I use the methods rather than fields for access
#       even between classes in this module.
#
#       For example, perhaps an implementer of these Python modules would want to make the reaction constant vary over time,
#       or spatially. Because of this I have set the precedent of accessing these values via method calls instead of
#       direct field access.
#
#   -   I would actually have preferred to make the ScalarIdentifier class immutable, though I noticed this technique
#       is not typically used elsewhere in the Python modules, I would speculate that this is because of some challenges
#       in managing Python objects from C++; the boundary between the languages is nontrivial in complexity and
#       at this time I suppose I will make an interface that avoids creating unnecessary objects. 
#
#   -   We choose to avoiid using property() as a design decision. I am also concerned it would be confusing because we have our own
#       PropertyStorage class which is completely unrelated to the python property()


class Summand(class):
    def __init__(self, scalarSymbol, order, reactionConstant):
        self._scalarSymbol = scalarSymbol
        self._order = order
        self._reactionConstant = reactionConstant

    def getScalarSymbol(self):
        return self._scalarSymbol

    def setScalarSymbol(self, scalarSymbol):
        self._scalarSymbol = scalarSymbol
    
    def getOrder(self):
        return self._order

    def setOrder(self, order):
        self._order = order
    
    def getReactionConstant(self):
        return self._reactionConstant
    
    def setReactionConstant(self, reactionConstant):
        self._reactionConstant = reactionConstant

    
class Reaction(class):
    def __init__(self):
        self._summands = []

    def renameScalarInReaction(self, oldSymbol, newSymbol):
        for summand in self._summands:
            summandSymbol = summand.getScalarSymbol()

            if(summandSymbol == oldSymbol):
                print("Renaming old scalar symbol in reaction from '", oldSymbol, "' to '", newSymbol, "'",  sep='')
                summand.setScalarSymbol(newSymbol)

    def getSummands(self):
        return self._summands

    def setSummands(self, newSummands):
        self._summands = newSummands

    def RunReaction(self, summands):
        

