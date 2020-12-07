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
                "Scalar simulation parameters":
                [
                    {
                        "Scalar Influx Coefficient": 0.5,
                        "attributes": {"minimum": 0.01, "maximum": 1.0}
                    },

                    # If you want to run the fluid solver only for a few timesteps before running the scalar simulation
                    # (e.g., to let the fluids "settle out"), set this to something other than timestep 1.
                    # Note that timesteps are 1-based. This is NOT an iteration.
                    {
                        "Scalar Start Time": 1,
                        "attributes": {"minimum": 1}
                    },

                    # If you want to stop running the flowsolver after a certain number of timesteps, but continue running
                    # the scalar problem after that, enable this option and set the timestep to stop on
                    {
                        "End Solve Flow": False,
                    },

                    {
                        "End Flow Time": 1,
                        "attributes": {"minimum": 1}
                    },

                    # Type type of scalar discontinuity capturing, 
                    # 1 0 is the one we usually use.
                    {
                        "Scalar Discontinuity Capturing": "1 0"
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