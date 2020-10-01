from __future__ import print_function

from Multiplicand import Multiplicand

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

"""
    A class representing a summand in a reaction, e.g., k3*III^2 in k3*III^2 + k2*II + k1*I^3
    I considered making this a PropertyStorage class but the standard property tree will not be very useful for this, I think,
    since really I want to give you a drop down of possible scalar symbols and constants instead of having you type them in manually.

    Remember that C++ manages which Multiplicands belong to this Summand, via the HierarchyManager.
"""
class Summand(object):
    def __init__(self, reactionConstant):
        self._reactionConstant = reactionConstant
    
    def getReactionConstant(self):
        return self._reactionConstant
    
    def setReactionConstant(self, reactionConstant):
        self._reactionConstant = reactionConstant