from CRIMSONCore.PropertyStorage import PropertyStorage

class CouplingType(object):
    enumNames = ["Explicit", "Implicit", "P-Implicit"]
    Explicit, Implicit, PImplicit = range(3)

class SolverType(object):
    enumNames = ["memLS", "acusim"]
    memLS, acusim = range(2)

class SolverParameters3D(PropertyStorage):
    def __init__(self):
        PropertyStorage.__init__(self)
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
            {
                "Lagrangian particle tracking parameters":
                [
                    {
                        "Particle simulation nametag": u"lagrangian_particles"
                    },
                    {
                        "Number of processors to use": 1,
                        "attributes": {"minimum": 1}
                    },
                    {
                        "Output particle solution every": 1,
                        "attributes": {"minimum": 1, "suffix": " fluid restarts"}
                    },
                    {
                        "Portion of fluid solution to use":
                        [
                            {
                                "Start at fluid problem timestep": 0,
                                "attributes": {"minimum": 0}
                            },
                            {
                                "Finish at fluid problem timestep": 200
                            },
                            {
                                "Repeats": 3,
                                "attributes": {"minimum": 1}
                            }
                        ]
                    },
                    {
                        "Particle Reinjection":
                        [
                            {
                                "Reinject bolus every": 0.5,
                                "attributes": {"minimum": 0.00001, "suffix": " s"}
                            },
                            {
                                "Initial injection time": 0.2,
                                "attributes": {"minimum": 0.0, "suffix": " s"}
                            },
                            {
                                "Maximum reinjections": 9999999,
                                "attributes": {"minimum": 1, "maximum": 9999999}
                            }
                        ]
                    },
                ]
            },
        ]