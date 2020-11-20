from CRIMSONCore.PropertyStorage import PropertyStorage

class CouplingType(object):
    enumNames = ["Explicit", "Implicit", "P-Implicit"]
    Explicit, Implicit, PImplicit = range(3)

class SolverType(object):
    enumNames = ["memLS", "acusim"]
    memLS, acusim = range(2)

class SolverParameters3D(PropertyStorage):

    def setIterations(self, iterations):
        self.Iterations = iterations
    
    def getIterations(self):
        return self.Iterations

    def _getStepConstructionSection(self):
        simParametersCategory = self.properties[2]
        simParameters = simParametersCategory['Simulation parameters']
        stepConstructionSection = simParameters[5]

        return stepConstructionSection

    def getFluidIterationCount(self):
        stepConstructionSection = self._getStepConstructionSection()
        numberOfSteps = stepConstructionSection['Step construction']

        #print('DEBUG: [get] Properties is')
        #print(self.properties)
        return numberOfSteps

    def setFluidIterationCount(self, fluidIterationCount):
        stepConstructionSection = self._getStepConstructionSection()
        stepConstructionSection['Step construction'] = fluidIterationCount

        #print('DEBUG: [set] Properties is')
        #print(self.properties)

    def __init__(self):
        PropertyStorage.__init__(self)

        self.Iterations = []

        self.properties = [
            {
                "Time parameters":
                 [
                    {
                        "Number of time steps": 200,
                        "attributes": {"minimum": 1}
                    },
                    {
                        "Time step size": 0.01,
                        "attributes": {"minimum": 0.0, "suffix": " s"}
                    }
                 ]
            },
            {
                "Fluid parameters":
                [
                    {
                        "Viscosity": 0.004,
                        "attributes": {"minimum": 0.0, "suffix": u" g/(mm\u00B7s)"}
                    },
                    {
                        "Density": 0.00106,
                        "attributes": {"minimum": 0.0, "suffix": u" g/mm\u00B3"}
                    }
                ]
            },
            {
                "Simulation parameters":
                [
                    {
                        "Solver type": SolverType.memLS,
                        "attributes": {"enumNames": SolverType.enumNames}
                    },
                    {
                        "Number of time steps between restarts": 5,
                        "attributes": {"minimum": 1}
                    },
                    {
                        "Residual control": True,
                    },
                    {
                        "Residual criteria": 0.001,
                        "attributes": {"minimum": 0.0}
                    },
                    {
                        "Minimum required iterations": 2,
                        "attributes": {"minimum": 1}
                    },
                    {
                        "Step construction": 5,
                        "attributes": {"minimum": 1}
                    },
                    {
                        "Pressure coupling": CouplingType.Implicit,
                        "attributes": {"enumNames": CouplingType.enumNames}
                    },
                    {
                        "Influx coefficient": 0.5,
                        "attributes": {"minimum": 0.01, "maximum": 1.0}
                    },
                    {
                        "Simulate in Purely Zero Dimensions": False,
                    },
                ]
            },
            {
                #TODO: I think this is unused
                "Scalar simulation parameters":
                [
                    {
                        "Residual control": True,
                    },
                    {
                        "Residual criteria": 0.001,
                        "attributes": {"minimum": 0.0}
                    },
                    {
                        "Step construction sequence": "0 1 0 1 0 1",
                    },
                ]
            },
            {
                "Output parameters":
                [
                    {
                        "Output wall shear stress": True
                    },
                    {
                        "Output error indicator": True
                    }
                ]
            },
        ]