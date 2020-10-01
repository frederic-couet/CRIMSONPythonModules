from __future__ import print_function

"""
    A class representing a scalar's reaction.
    Note that C++ is responsible for deciding which summands belong to this reaction.
"""
class Reaction(object):
    def __init__(self):

    # this could be static but I am not sure how easy it is to call a static method or function in a file via PythonQt
    """
        Generates a python reaction script for the reaction (for one scalar) on a set of configured summands.
    """
    def generateReactionPythonScript(self, summands):
        # incomplete
        pass