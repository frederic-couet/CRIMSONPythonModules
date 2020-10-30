# source automatically generated for Python class "GenericTypeIDObject"
# using GenerateNewSolverObject.
#
# Generated on 2020-10-29 11:34:14.785000

from CRIMSONCore.PropertyStorage import PropertyStorage

# Does this cause an infinite dependency loop? Do I need to move this to a different file?
# I'd rather not, because then I'd have to show C++ where this other file is to call the static methods on it
from CRIMSONSolver.SolverSetupManagers.CRIMSONSolverSolverSetupManager import CRIMSONSolverSolverSetupManager

"""
    An abstract class for Python classes, where the hierarchy is specified in Python
"""
class GenericTypeIDObject(PropertyStorage):

    def __init__(self):
        PropertyStorage.__init__(self)
        self.properties = [
            {

            }
        ]

    def getHumanReadableName(self):
        # e.g., "Boundary Condition" instead of BoundaryCondition
        raise NotImplementedError("Derived types must specify a human readable name for this node.")

    def getMyNodeIcon(self):
        raise NotImplementedError("Derived types must specify an icon for this object's node.")

    def getMyTypeID(self):
        # you can do something like YourType.__name__ if it's appropriate, but don't do this if you have several python objects that relate 
        # back to the same type, e.g., you might have many "BoundaryCondition" classes
        raise NotImplementedError("Derived types must implement this method and specify a TypeID.")

    def getMyTypeName(self):
        typeID = self.getMyTypeID()
        CRIMSONSolverSolverSetupManager.TypeIDToName[typeID]

    # This might need to be stored in a mitk::DataNode property somewhere so that you can sort based on the python type of this node.
    def getOwnerNodeType(self):
        return CRIMSONSolverSolverSetupManager.getOwnerNodeType(self.getMyTypeID())





