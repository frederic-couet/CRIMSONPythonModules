from CRIMSONSolver.BoundaryConditionSets.BoundaryConditionSet import BoundaryConditionSet
from CRIMSONSolver.BoundaryConditions import InitialPressure, NoSlip, PrescribedVelocities, RCR, ZeroPressure, \
    DeformableWall, Netlist, PCMRI

from CRIMSONSolver.ScalarProblem import Scalar, ScalarProblem
from CRIMSONSolver.ScalarProblem import ScalarDirichlet, ScalarNeumann, InitialConcentration
from CRIMSONSolver.ScalarProblem import ReactionCoefficient, SolverIteration

from CRIMSONSolver.SolverParameters.SolverParameters3D import SolverParameters3D
from CRIMSONSolver.SolverStudies.SolverStudy import SolverStudy
from CRIMSONSolver.Materials import DeformableWallMaterial, AnisoDeformableWallMaterial


class CRIMSONSolverSolverSetupManager(object):
    humanReadableName = "CRIMSON Solver"

    def __init__(self):
        self.boundaryConditionSetClasses = {"Boundary condition set": BoundaryConditionSet}
        self.solverParametersClasses = {"Solver parameters 3D": SolverParameters3D}
        self.solverStudyClasses = {"Solver study 3D": SolverStudy}
        self.boundaryConditionClasses = {"Initial pressure": InitialPressure.InitialPressure,
                                         "No slip": NoSlip.NoSlip,
                                         "Prescribed velocities (analytic)": PrescribedVelocities.PrescribedVelocities,
                                         "RCR": RCR.RCR,
                                         "Zero pressure": ZeroPressure.ZeroPressure,
                                         "Deformable wall": DeformableWall.DeformableWall,
                                         "Netlist": Netlist.Netlist,
                                         "Prescribed velocities (PC-MRI)": PCMRI.PCMRI
                                         }
        self.materialClasses = {"Deformable wall material": DeformableWallMaterial.DeformableWallMaterial,
                                "Deformable wall material (anisotropic)": AnisoDeformableWallMaterial.AnisoDeformableWallMaterial}
        self.scalarProblemClasses = {"Scalar problem set": ScalarProblem.ScalarProblem}
        self.scalarClasses = {"Scalar": Scalar.Scalar}
        self.scalarBCClasses = {"Scalar Dirichlet": ScalarDirichlet.ScalarDirichlet,
                                "Scalar Neumann":   ScalarNeumann.ScalarNeumann,
                                "Initial Concentration": InitialConcentration.InitialConcentration}

        self.reactionCoefficientClasses = {"Reaction Coefficient": ReactionCoefficient.ReactionCoefficient}
        self.solverIterationClasses = {"Solver Iteration": SolverIteration.SolverIteration}

    # Boundary condition sets
    def getBoundaryConditionSetNames(self):
        return self.boundaryConditionSetClasses.keys()

    def createBoundaryConditionSet(self, name):
        return self.boundaryConditionSetClasses[name]()

    # Boundary conditions
    # [AJM] Why is it necessary to pass in the ownerBCSet here? It's not used for anything and it makes the C++ code a lot more complicated...
    def getBoundaryConditionNames(self, ownerBCSet):
        return self.boundaryConditionClasses.keys()

    def createBoundaryCondition(self, name, ownerBCSet):
        return self.boundaryConditionClasses[name]()

    # Materials
    def getMaterialNames(self):
        return self.materialClasses.keys()

    def createMaterial(self, name):
        return self.materialClasses[name]()

    # Solver parameters
    def getSolverParametersNames(self):
        return self.solverParametersClasses.keys()

    def createSolverParameters(self, name):
        return self.solverParametersClasses[name]()

    # Solver studies
    def getSolverStudyNames(self):
        return self.solverStudyClasses.keys()

    def createSolverStudy(self, name):
        return self.solverStudyClasses[name]()

    # Scalar problems
    def getScalarProblemNames(self):
        return self.scalarProblemClasses.keys()

    def createScalarProblem(self, name):
        return self.scalarProblemClasses[name]()

    # Scalars
    def getScalarNames(self, ownerScalarProblem):
        return self.scalarClasses.keys()

    def createScalar(self, name, ownerScalarProblem):
        return self.scalarClasses[name]()

    # Scalar boundary and initial conditions
    def getScalarBCNames(self, ownerScalar):
        return self.scalarBCClasses.keys()

    def createScalarBC(self, name, ownerScalar):
        return self.scalarBCClasses[name]()

    def getReactionCoefficientNames(self):
        return self.reactionCoefficientClasses.keys()
    
    def createReactionCoefficient(self, name):
        return self.reactionCoefficientClasses[name]
    
    def getSolverIterationNames(self):
        return self.solverIterationClasses.keys()
    
    def createSolverIteration(self, name):
        return self.solverIterationClasses[name]