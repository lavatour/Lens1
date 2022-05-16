import math
from lenses import Lens
from lenses import SecondLens
from linearAlg import LinAlg

class Light():
    """Light class for Light objects"""
    def __init__(self, rayNumber):   #Number of rays to be generated
        self.rayNumber = rayNumber
        self.sourceX = 50   # X position of light source
        self.sourceY = 0    # Y position of light source
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
        #print(f"x, y = {x, y}")
        h, k = lens.x_c, lens.y_c

        while abs(((x - h) ** 2 + (y - k) ** 2)- lens.radius ** 2) > 0.000001:
            #print(f"h, k = {h, k}")
            #print(f"x, y = {x, y}")
            dist = math.sqrt((x - lens.x_c)**2 + (y - lens.y_c)**2 ) - lens.radius
            #print(f"dist, dist * math.cos(angle[-1]) = {dist, dist * math.cos(angle[-1]) - self.radius}")
            #print(f"((x - h)**2 + (y - k)**2) - self.radius**2, {((x - h)**2 + (y - k)**2) - self.radius**2}")
            x = x + dist * math.cos(self.angle[-1])
            y = y + dist * math.sin(self.angle[-1])

        self.ray.append([x, y])


    """
    def rayLensIntersection(self, lens):
        #intersection = []
        #print(f"ray = {ray[-1]}")
        y = self.ray[-1][1]
        #print(f"radius, y, self.y_c = {self.radius, y, self.y_c}")
        #print(f"asin(inside) = {(y + self.y_c) / self.radius}")
        #if (y + self.y_c) / self.radius > 1:
            #theta = math.pi / 4
        #else:
        print(f"y = {y}, self.y_c = {lens.y_c}")
        print(f"asin = {(y + lens.y_c) / lens.radius}")
        theta = math.pi - math.asin((y + lens.y_c) / lens.radius)
        print(f"theta = {theta * 180 / math.pi} radius = {lens.radius}")

        x = lens.x_c + lens.radius * math.cos(theta)
        y = lens.y_c + lens.radius * math.sin(theta)
        print(f"x, y = {x, y}")
        self.ray.append([x, y])
        #print(f"inside ray = {ray}")
        return self.ray
    """



    def refraction(self, lens, n1, n2):
        """Ray - Lens1 Interaction and refraction"""
        lens.rayLensIntersection(self.ray, self.angle)
        # Compute Normal Vector
        unitNormalVector = lens.normalVect(self.ray)
        #if n1 == 1.5:
        #    print(f"unitNormalVector = {unitNormalVector}")
        # Compute ray Unit Normal Vector
        print(f"33 ray = {self.ray}, angle = {self.angle}")
        rayUnitVector = [math.cos(self.angle[-1]), math.sin(self.angle[-1])]
        #if self.ray[0][1] == 40:
        #print(f"rayUnitVector = {rayUnitVector}")

        #Compute dot produce. If angle is obtuse unitNormalVector will be multiplied by -1
        dotProd = LinAlg.dotProd(self, unitNormalVector, rayUnitVector)
        if dotProd < 0:
            unitNormalVector = LinAlg.scalarMultiplication(self, -1, unitNormalVector)
        #if n1 == 1.5:
        print(f"unitNormalVector = {unitNormalVector}")

        # Use cross product to find sin(theta)
        crossProd = LinAlg.crossProd(self, unitNormalVector, rayUnitVector)
        if n1 == 1.5:
            print(f"crossProd = {crossProd}")
        angleOfIncidence = math.asin(crossProd)
        if n1 == 1.5:
            print(f"AngleofIncidence = {angleOfIncidence * 180 / math.pi}")

        # Compute Angle of refraction
        angleOfRefraction = lens.n1 * math.asin(math.sin(angleOfIncidence) / lens.n2)
        if n1 == 1.5:
            print(f"angleOfRefraction = {angleOfRefraction * 180 / math.pi}")

        normalAngle = math.asin(unitNormalVector[1])
        print(f"normalAngle = {normalAngle}")
        lightAngle = normalAngle + angleOfRefraction
        if n1 == 1.5:
            print(f"lightAngle*180/math.pi = {lightAngle*180/math.pi}")
        self.angle.append(lightAngle)


    def rayExtension(self):
        dx = 700 * math.cos(self.angle[-1])
        dy = 700 * math.sin(self.angle[-1])
        #print(f"rayAngle = {self.angle[-1] * 180/math.pi}")
        self.ray.append([self.ray[-1][0] + dx, self.ray[-1][1] + dy])


        """ ********************************************************"""


    #def refraction2(self):
        """Ray """
        #print(f"raym = {self.ray}")
        #self.lens2.rayLens2Intersection(self.ray, self.angle)
        #print(f"raym = {self.ray}")
