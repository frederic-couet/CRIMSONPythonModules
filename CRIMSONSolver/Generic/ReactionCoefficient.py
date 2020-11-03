from GenericTypeIDObject import GenericTypeIDObject

"""
    A class representing a coefficient in a chemical reaction
"""
class ReactionCoefficient(GenericTypeIDObject):

    def __init__(self):
        PropertyStorage.__init__(self)
        self.properties = [
            {
                "Coefficient value": 1.234,
                "Name": "k1"
            }
        ]

    def getHumanReadableName(self):
        return "Reaction Coefficient"

    def getMyNodeIcon(self):
        return "TBD"

    def getMyTypeID(self):
        return CRIMSONSolverSolverSetupManager.NameToTypeID["ReactionCoefficient"]

    def getMyTypeName(self):
        typeID = self.getMyTypeID()
        return CRIMSONSolverSolverSetupManager.TypeIDToName[typeID]

    # This might need to be stored in a mitk::DataNode property somewhere so that you can sort based on the python type of this node.
    def getOwnerNodeType(self):
        return CRIMSONSolverSolverSetupManager.getOwnerNodeType(self.getMyTypeID())
