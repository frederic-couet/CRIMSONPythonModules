import InitialAndBoundaryConditions
import BoundaryConditionSets
import SolverParameters
import SolverStudies
import SolverSetupManagers

__all__ = ['InitialAndBoundaryConditions', 'BoundaryConditionSets', 'SolverParameters', 'SolverStudies',
           'SolverSetupManagers']

import inspect


def getHumanReadableName(objClass):
    return objClass.humanReadableName if hasattr(objClass, 'humanReadableName') else objClass.__name__

def getSolverSetupManager():
    solverSetupManagerClass = SolverSetupManagers.CRIMSONScalarSolverSetupManager.CRIMSONSolverSolverSetupManager
    return (getHumanReadableName(solverSetupManagerClass), solverSetupManagerClass)

def reloadAll():
    for module_name in __all__:
        # [AJM] this line makes this module only work on Python 2, because in Python 2 exec no longer effects the global scope.
        exec ('{0} = reload({0})'.format(module_name))
