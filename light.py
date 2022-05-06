import math
from sphericalLens import SphericalLens
from linearAlg import LinAlg

class Light():
    """Light class for Light objects"""
    def __init__(self, rayCount):   #Number of rays to be generated
        self.rayNumber = rayCount
        self.sourceX = 50   # X position of light source
        self.sourceY = 0    # Y position of light source
        self.sourceWidth = 10   # Vertical distance between rays
        self.ray = []           # ray position
        self.angle = 0          # ray angle
        self.lens = SphericalLens()  # Initiate Lens Class This will depend on the type of lens being used

    def source(self):
        self.ray.append([self.sourceX, self.sourceY + self.rayNumber * self.sourceWidth])
        return self.ray

    def refraction(self):
        # Returns point where light intersects lens surface.
        self.lens.raySurfaceIntersection(self.ray)
        # Compute Normal Vector
        unitNormalVector = self.lens.normalVect(self.ray)
        #print(f"unitNormalVector = {unitNormalVector}")
        # Compute ray Unit Normal Vector
        rayUnitVector = LinAlg.makeUnitVector(self, self.ray[-2][0], self.ray[-2][1], self.ray[-1][0], self.ray[-1][1])
        dotProd = LinAlg.dotProd(self, unitNormalVector, rayUnitVector)
        if dotProd < 0:
            unitNormalVector = LinAlg.scalarMultiplication(self, -1, unitNormalVector)
        print(f"unitNormalVector = {unitNormalVector}")
        crossProd = crossProd = LinAlg.crossProd(self, rayUnitVector, unitNormalVector)
        angleOfIncidence = math.asin(crossProd)
        print(f"AngleofIncidence = {angleOfIncidence * 180 / math.pi}")




        # Compute dot product of ray and


