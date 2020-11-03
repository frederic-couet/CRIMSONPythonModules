from CRIMSONSolver.BoundaryConditionSets.BoundaryConditionSet import BoundaryConditionSet
from CRIMSONSolver.BoundaryConditions import InitialPressure, NoSlip, PrescribedVelocities, RCR, ZeroPressure, \
    DeformableWall, Netlist, PCMRI

from CRIMSONSolver.ScalarProblem import Scalar, ScalarProblem
from CRIMSONSolver.ScalarProblem import ScalarDirichlet, ScalarNeumann, InitialConcentration

from CRIMSONSolver.SolverParameters.SolverParameters3D import SolverParameters3D
from CRIMSONSolver.SolverStudies.SolverStudy import SolverStudy
from CRIMSONSolver.Materials import DeformableWallMaterial, AnisoDeformableWallMaterial

from CRIMSONSolver.Generic.GenericTypeIDObject import GenericTypeIDObject

# Keep in sync with crimson\Plugins\uk.ac.kcl.HierarchyManager\src\HierarchyManager.h
class RelationType:
    OneToOne = 0
    OneToMany = 1
    Unknown = 2

# Keep in sync with crimson\Plugins\uk.ac.kcl.HierarchyManager\src\HierarchyManager.h
class NodeTypeFlags:
    fNone = 0
    fRecursiveDeletion = 1
    fUndoableDeletion = 2
    fPickable = 4

TypeID_Invalid = -1

class CRIMSONSolverSolverSetupManager(object):
    humanReadableName = "CRIMSON Solver"

    # TODO: Python's syntax allows you to call a static method from a class instance,
    #       so this might be OK, though I don't know if PythonQt supports it.

    """
        Type names must be unique
    """
    def getTypeNames():
        return [
            "SolverRoot",
            "SolverParameters",
            BoundaryConditionSet.__name__,
            "BoundaryCondition",
            "Material",
            SolverStudy.__name__,
            "Solution",
            "AdaptationData",
            "PCMRIData",
            "MRAPoint",
            "PCMRIPoint",
            ScalarProblem.__name__,
            Scalar.__name__,
            "ScalarBoundaryCondition",
            "ReactionCoefficient"
        ]

    def getTypeIDToTypeNameDictionary():
        typeIDToNameDict = dict()
        typeNames = getTypeNames()

        for typeID in range(len(typeNames)):
            typeName = typeNames[typeID]

            typeIDToNameDict[typeID] = typeName

        return typeIDToNameDict

    def getTypeNameToTypeIDDictionary():
        typeNameToIDDict = dict()
        typeNames = getTypeNames()

        for typeID in range(len(typeNames)):
            typeName = typeNames[typeID]

            if(typeName in typeNameToIDDict):
                atIndex = typeNameToIDDict[typeName]
                print("Unexpected error: Duplicate type name in typenames array. Name '", typeName, "' at index ", typeID, " already defined previously at index ", atIndex, sep = '' )
                continue

            typeNameToIDDict[typeName] = typeID

        return typeIDToNameDict

    getTypeNames                    = staticmethod(getTypeNames)
    getTypeIDToTypeNameDictionary   = staticmethod(getTypeIDToTypeNameDictionary)
    getTypeNameToTypeIDDictionary   = staticmethod(getTypeNameToTypeIDDictionary)

    # Quick access static fields
    NameToTypeID =  getTypeNameToTypeIDDictionary()
    TypeIDToName =  getTypeIDToTypeNameDictionary()

    def getTypeIDsToClassesDictionary():
        return {
            NameToTypeID["BoundaryConditionSet"]: {
                BoundaryConditionSet.BoundaryConditionSet.humanReadableName: BoundaryConditionSet
            },
            NameToTypeID["SolverParameters"]: {
                SolverParameters3D.SolverParameters3D.humanReadableName: SolverParameters3D
            },
            NameToTypeID["SolverStudy"]: {
                SolverStudy.SolverStudy.humanReadableName, SolverStudy
            },
            NameToTypeID["BoundaryCondition"]: {
                InitialPressure.InitialPressure.humanReadableName: InitialPressure,
                NoSlip.NoSlip.humanReadableName: NoSlip,
                PrescribedVelocities.PrescribedVelocities.humanReadableName: PrescribedVelocities.PrescribedVelocities,
                RCR.RCR.humanReadableName: RCR.RCR,
                ZeroPressure.ZeroPressure.humanReadableName: ZeroPressure,
                DeformableWall.DeformableWall.humanReadableName: DeformableWall,
                Netlist.Netlist.humanReadableName: Netlist,
                PCMRI.PCMRI.humanReadableName: PCMRI
            },
            NameToTypeID["Material"]: {
                DeformableWallMaterial.DeformableWallMaterial.humanReadableName: DeformableWall.DeformableWall,
                AnisoDeformableWallMaterial.AnisoDeformableWallMaterial.humanReadableName: AnisoDeformableWallMaterial.AnisoDeformableWallMaterial
            },
            NameToTypeID["ScalarProblem"]: {
                ScalarProblem.ScalarProblem.humanReadableName: ScalarProblem.ScalarProblem
            },
            NameToTypeID["Scalar"]: {
                Scalar.Scalar.humanReadableName: Scalar.Scalar
            },
            NameToTypeID["ScalarBoundaryCondition": {
                ScalarDirichlet.ScalarDirichlet.humanReadableName: ScalarDirichlet.ScalarDirichlet,
                ScalarNeumann.ScalarNeumann.humanReadableName: ScalarNeumann.ScalarNeumann,
                InitialConcentration.InitialConcentration.humanReadableName: InitialConcentration.InitialConcentration
            }
        }

    getTypeIDsToClassesDictionary = staticmethod(getTypeIDsToClassesDictionary)

    TypeIDsToClasses = getTypeIDsToClassesDictionary()

    def __init__(self):
        pass

    # Convenience method for implementing backwards compatible type specific methods
    def _getPyClassNamesToClasses(self, typeName):
        typeID = NameToTypeID[typeName]
        return TypeIDsToClasses[typeID]

    def getGenericTypeNames(self, typeId):
        return TypeIDsToClasses[typeID]

    def createGenericType(self, typeID, humanReadableName):
        return TypeIDsToClasses[typeID][humanReadableName]()

    # Boundary condition sets
    def getBoundaryConditionSetNames(self):
        return self._getPyClassNamesToClasses("BoundaryConditionSet").keys()

    def createBoundaryConditionSet(self, name):
        return self._getPyClassNamesToClasses("BoundaryConditionSet")[name]()

    # Boundary conditions
    def getBoundaryConditionNames(self, ownerBCSet):
        return self._getPyClassNamesToClasses("BoundaryCondition").keys()

    def createBoundaryCondition(self, name, ownerBCSet):
        return self._getPyClassNamesToClasses("BoundaryCondition")[name]()

    # Materials
    def getMaterialNames(self):
        return self._getPyClassNamesToClasses("Material").keys()

    def createMaterial(self, name):
        return self._getPyClassNamesToClasses("Material")[name]()

    # Solver parameters
    def getSolverParametersNames(self):
        return self._getPyClassNamesToClasses("SolverParameters").keys()

    def createSolverParameters(self, name):
        return self._getPyClassNamesToClasses("SolverParameters")[name]()

    # Solver studies
    def getSolverStudyNames(self):
        return self._getPyClassNamesToClasses("SolverStudy").keys()

    def createSolverStudy(self, name):
        return self._getPyClassNamesToClasses("SolverStudy")[name]

    # Scalar problems
    def getScalarProblemNames(self):
        return self._getPyClassNamesToClasses("ScalarProblem").keys()

    def createScalarProblem(self, name):
        return self._getPyClassNamesToClasses("ScalarProblem")[name]

    # Scalars
    def getScalarNames(self, ownerScalarProblem):
        return self._getPyClassNamesToClasses("Scalar").keys()

    def createScalar(self, name, ownerScalarProblem):
        return self._getPyClassNamesToClasses("Scalar")[name]

    # Scalar boundary and initial conditions
    def getScalarBCNames(self, ownerScalar):
        return self._getPyClassNamesToClasses("ScalarBoundaryCondition").keys()

    def createScalarBC(self, name, ownerScalar):
        return self._getPyClassNamesToClasses("ScalarBoundaryCondition")[name]


    def getRelations():
        return {
            NameToTypeID["SolverRoot"]: {
                NameToTypeID["SolverParameters"]: RelationType.OneToMany,
                NameToTypeID["BoundaryConditionSet"]: RelationType.OneToMany,
                NameToTypeID["Material"]: RelationType.OneToMany,
                NameToTypeID["SolverStudy"]: RelationType.OneToMany,
                NameToTypeID["ScalarProblem"]: RelationType.OneToMany
            },

            NameToTypeID["BoundaryConditionSet"]: {
                NameToTypeID["BoundaryCondition"]: RelationType.OneToMany
            },

            NameToTypeID["SolverStudy"]: {
                NameToTypeID["Solution"]: RelationType.OneToMany,
                NameToTypeID["AdaptationData"]: RelationType.OneToMany,
            },

            NameToTypeID["VesselTree"]: {
                NameToTypeID["SolverRoot"]: RelationType.OneToMany
            },

            NameToTypeID["Solid"]: {
                NameToTypeID["SolverRoot"]: RelationType.OneToMany
            },

            NameToTypeID["Image"]: {
                NameToTypeID["Contour"]: RelationType.OneToMany,
                NameToTypeID["ContourReferenceImage"]: RelationType.OneToMany,
                NameToTypeID["ContourSegmentationImage"]: RelationType.OneToMany

                NameToTypeID["PCMRIPoint"]: RelationType.OneToOne
            },

            NameToTypeID["BoundaryCondition"]: {
                NameToTypeID["PCMRIData"]: RelationType.OneToOne,
                NameToTypeID["MRAPoint"]: RelationType.OneToOne
            },

            NameToTypeID["ScalarProblem"]: {
                NameToTypeID["Scalar"], RelationType.OneToMany
            },

            NameToTypeID["Scalar"]: {
                NameToTypeID["ScalarBoundaryCondition"]: RelationType.OneToMany
            }

        }

    getRelations = staticmethod(getRelations)

    """
        NOTE:
        This is not a redundant copy of getRelations, nor can this be derived from getRelations.
        getRelations handles more than just the tree hierarchy, there are some loops in that structure, which would ruin this function.

        Note that this matches what's in crimson\Plugins\uk.ac.kcl.SolverSetupView\src\internal\SolverObjectTraits.hSolverObjectTraits.h.

        Not all the node types were present in SolverObjectTraits, I am not sure why this is. Maybe this functionality can be cleaned up later.

    """
    def getOwnerDictionary():
        return {
            # Solver Root has no owner

            NameToTypeID["BoundaryConditionSet"]: NameToTypeID["SolverRoot"],

            NameToTypeID["SolverStudy"]: NameToTypeID["SolverRoot"]

            # Vessel Tree has no owner in SolverObjectTraits
            # Solid has no owner in SolverObjectTraits
            # Image has no owner in SolverObjectTraits

            NameToTypeID["BoundaryCondition"]: NameToTypeID["BoundaryConditionSet"]

            NameToTypeID["ScalarProblem"]: NameToTypeID["SolverRoot"],

            NameToTypeID["Scalar"]:NameToTypeID["ScalarProblem"]
        }

    getOwnerDictionary = staticmethod(getOwnerDictionary)

    def getOwnerNodeType(typeIDToGetOwnerOf):
        ownerDictionary = getOwnerDictionary()

        if(typeIDToGetOwnerOf in ownerDictionary):
            return ownerDictionary[typeIDToGetOwnerOf]
        
        else:
            return TypeID_Invalid

    getOwnerNodeType = staticmethod(getOwnerNodeType)