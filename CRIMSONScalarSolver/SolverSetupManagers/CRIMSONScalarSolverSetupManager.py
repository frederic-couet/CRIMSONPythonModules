from CRIMSONScalarSolver.BoundaryConditionSets.BoundaryConditionSet import BoundaryConditionSet
from CRIMSONScalarSolver.InitialAndBoundaryConditions import Dirichlet, InitialConditions, Neumann
from CRIMSONScalarSolver.SolverParameters.SolverParameters3D import SolverParameters3D
from CRIMSONScalarSolver.SolverStudies.SolverStudy import SolverStudy


class CRIMSONSolverSolverSetupManager(object):
    humanReadableName = "CRIMSON Scalar Solver"

    def __init__(self):
        self.boundaryConditionSetClasses = {"Boundary condition set": BoundaryConditionSet}
        self.solverParametersClasses = {"Solver parameters 3D": SolverParameters3D}
        self.solverStudyClasses = {"Solver study 3D": SolverStudy}
        self.boundaryConditionClasses = {
                                         "Dirichlet BC": Dirichlet.Dirichlet,
                                         "Neumann BC": Neumann.Neumann,
                                         "Initial Conditions":InitialConditions.InitialConditions
                                         }

    # Boundary condition sets
    def getBoundaryConditionSetNames(self):
        return self.boundaryConditionSetClasses.keys()

    def createBoundaryConditionSet(self, name):
        return self.boundaryConditionSetClasses[name]()

    # Boundary conditions
    def getBoundaryConditionNames(self, ownerBCSet):
        return self.boundaryConditionClasses.keys()

    def createBoundaryCondition(self, name, ownerBCSet):
        return self.boundaryConditionClasses[name]()

    # The scalar solver does not have materials (at the moment)
    def getMaterialNames(self):
        return []

    def createMaterial(self, name):
        pass

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