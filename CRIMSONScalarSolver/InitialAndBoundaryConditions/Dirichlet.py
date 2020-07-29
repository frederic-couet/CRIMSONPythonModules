from CRIMSONCore.FaceData import FaceData
from PythonQt.CRIMSON import FaceType


class Dirichlet(FaceData):
    # TODO: Investigate this field
    unique = True
    humanReadableName = "Dirichlet BC"

    # TODO: Investigate this field
    applicableFaceTypes = []

    def __init__(self):
        FaceData.__init__(self)
        self.properties = [
            {
                # TODO: Is there a better name for this than "value"?
                "value": 0.0,
                # TODO: What units? Should put the units in the "suffix" field
                "attributes": {"minimum": 0.0, "suffix": u""}
            },
        ]
