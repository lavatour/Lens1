import math
from lenses import Lens
from lenses import SecondLens
from linearAlg import LinAlg

class Light():
    """Light class for Light objects"""
    def __init__(self, rayNumber):   #Number of rays to be generated
        self.rayNumber = rayNumber
        self.sourceX = 50   # X position of light source
        self.sourceY = -190    # Y position of light source
        self.sourceWidth = 10   # Vertical distance between rays
        self.ray = []           # ray position
        self.angle = []          # ray angle
        #self.lens = lens  # Initiate Lens Class This will depend on the type of lens being used
        self.lens2 = SecondLens()
        self.xfp = 0   # The points where the ray crosses the focal line

    def lightSource(self):
        """ SOURCE POINTS """
        self.ray.append([self.sourceX, self.sourceY + self.rayNumber * self.sourceWidth])
        self.angle.append(0)
        return self.ray


    def rayLensIntersection(self, lens):
        x = self.ray[-1][0]
        y = self.ray[-1][1]
        h, k = lens.x_c, lens.y_c

        while abs(((x - h) ** 2 + (y - k) ** 2)- lens.radius ** 2) > 0.000001:
            dist = math.sqrt((x - lens.x_c)**2 + (y - lens.y_c)**2 ) - lens.radius
            x = x + dist * math.cos(self.angle[-1])
            y = y + dist * math.sin(self.angle[-1])

        self.ray.append([x, y])



    def refraction(self, lens, n1, n2):
        """Ray - Lens1 Interaction and refraction"""
        # Compute Normal Vector
        unitNormalVector = lens.normalVect(self.ray)
        rayUnitVector = [math.cos(self.angle[-1]), math.sin(self.angle[-1])]

        #Compute dot produce. If angle is obtuse unitNormalVector will be multiplied by -1
        dotProd = LinAlg.dotProd(self, unitNormalVector, rayUnitVector)
        if dotProd < 0:
            unitNormalVector = LinAlg.scalarMultiplication(self, -1, unitNormalVector)

        # Use cross product to find sin(theta)
        crossProd = LinAlg.crossProd(self, unitNormalVector, rayUnitVector)

        angleOfIncidence = math.asin(crossProd)

        # Compute Angle of refraction
        angleOfRefraction = lens.n1 * math.asin(math.sin(angleOfIncidence) / lens.n2)

        normalAngle = math.asin(unitNormalVector[1])
        lightAngle = normalAngle + angleOfRefraction
        self.angle.append(lightAngle)


    def rayExtension(self):
        dx = 700 * math.cos(self.angle[-1])
        dy = 700 * math.sin(self.angle[-1])
        self.ray.append([self.ray[-1][0] + dx, self.ray[-1][1] + dy])

