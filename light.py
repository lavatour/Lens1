import math
from sphericalLens import FirstLens
from sphericalLens import SecondLens
from linearAlg import LinAlg

class Light():
    """Light class for Light objects"""
    def __init__(self, rayCount):   #Number of rays to be generated
        self.rayNumber = rayCount
        self.sourceX = 50   # X position of light source
        self.sourceY = 0    # Y position of light source
        self.sourceWidth = 10   # Vertical distance between rays
        self.ray = []           # ray position
        self.angle = []          # ray angle
        self.lens = FirstLens()  # Initiate Lens Class This will depend on the type of lens being used
        self.xfp = 0   # The points where the ray crosses the focal line

    def source(self):
        self.ray.append([self.sourceX, self.sourceY + self.rayNumber * self.sourceWidth])
        self.angle.append(0)
        return self.ray

    def refraction1(self):
        """Ray """
        self.lens.raySurfaceIntersection(self.ray)
        # Compute Normal Vector
        unitNormalVector = self.lens.normalVect(self.ray)
        #print(f"unitNormalVector = {unitNormalVector}")
        # Compute ray Unit Normal Vector
        rayUnitVector = LinAlg.makeUnitVector(self, self.ray[-2][0], self.ray[-2][1], self.ray[-1][0], self.ray[-1][1])

        #Compute dot produce. If angle is obtuse unitNormalVector will be multiplied by -1
        dotProd = LinAlg.dotProd(self, unitNormalVector, rayUnitVector)
        if dotProd < 0:
            unitNormalVector = LinAlg.scalarMultiplication(self, -1, unitNormalVector)
        #print(f"unitNormalVector = {unitNormalVector}")

        # Use cross product to find sin(theta)
        crossProd = crossProd = LinAlg.crossProd(self, rayUnitVector, unitNormalVector)
        angleOfIncidence = math.asin(crossProd)
        #print(f"AngleofIncidence = {angleOfIncidence * 180 / math.pi}")

        # Compute Angle of refraction
        angleOfRefraction = math.asin(1 * math.sin(angleOfIncidence) / self.lens.refIndex)

        self.angle.append(self.angle[-1] + angleOfRefraction)
        #print(f"angleOfRefraction = {angleOfRefraction * 180 / math.pi}")

        # Next Ray Segment
        x = self.ray[-1][0] + 500 * math.cos(self.angle[-1])
        y = self.ray[-1][1] + 500 * math.sin(self.angle[-1])
        self.ray.append([x, y])

        # Calculate point at which each ray reaches lens axis, x = 0.

        m = math.tan(self.angle[-1])
        #print(f"angle = {round(self.angle[-1] * 180 / math.pi, 2)}")
        if m != 0:
            self.xfp = y / m + x

    def refraction2(self):
        SecondLens.equation(self)




