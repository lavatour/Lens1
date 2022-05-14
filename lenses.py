import math
import light as Light

class Lens():
    def __init__(self, radius, x_c, y_c, refIndex):
        self.radius = radius
        self.x_c = x_c
        self.y_c = y_c
        self.unitNormalVector = []
        self.refIndex = refIndex
        #self.lens1FocalPt = [0, 0]

    def equation(self):
        surface = []
        for angle in range(90, 270):
            theta = angle * math.pi / 180
            x = self.x_c + self.radius * math.cos(theta)    # X coords of lens
            y = -self.y_c + self.radius * math.sin(theta)   # Y coords of lens
            surface.append([x, y])
        return surface


    def rayLensIntersection(self, ray):
        #intersection = []
        #print(f"ray = {ray[-1]}")
        y = ray[-1][1]
        theta = math.pi + math.asin((y + self.y_c) / self.radius)
        x = self.x_c + self.radius * math.cos(theta)
        ray.append([x, y])
        #print(f"inside ray = {ray}")
        return ray


    def normalVect(self, ray):
        """Calculate normal vector. Confirm by calculating normal angle."""
        x, y = (ray[-1][0] - self.x_c), ray[-1][1]
        radius = math.sqrt(x*x + y*y)
        #print(f"radius = {math.sqrt(x*x + y*y)}")
        normalVector = [x, y]
        self.unitNormalVector = [x / radius, y /  radius]
        return self.unitNormalVector

        """Calculate dot product of ray[-1] and the surface normal vector"""


class SecondLens():
    def __init__(self):
        self.xc = 965
        self.yc = 0
        self.radius = 30
        self.unitNormalVector = []


    def equation2(self):
        surface = []
        for angle in range(90, 270):
            theta = angle * math.pi / 180
            x = self.xc + self.radius * math.cos(theta)
            y = self.yc + self.radius * math.sin(theta)
            surface.append([x,y])
        #print(surface)
        return surface

    def rayLens2Intersection(self, ray, angle):
        x = ray[-1][0]
        y = ray[-1][1]
        #print(f"x, y = {x, y}")
        h, k = self.xc, self.yc

        while abs(((x - h) ** 2 + (y - k) ** 2)- self.radius ** 2) > 0.000001:
            #print(f"h, k = {h, k}")
            #print(f"x, y = {x, y}")
            dist = math.sqrt((x - self.xc)**2 + (y - self.yc)**2 ) - self.radius
            #print(f"dist, dist * math.cos(angle[-1]) = {dist, dist * math.cos(angle[-1]) - self.radius}")
            #print(f"((x - h)**2 + (y - k)**2) - self.radius**2, {((x - h)**2 + (y - k)**2) - self.radius**2}")
            x = x + dist * math.cos(angle[-1])
            y = y + dist * math.sin(angle[-1])

        ray.append([x, y])

    def normalVect(self, ray):
        """Calculate normal vector. Confirm by calculating normal angle."""
        x, y = (ray[-1][0] - self.xc), ray[-1][1]
        normalTheta = math.atan2(y, x)
        # print(normalTheta * 180 / (math.pi))
        radius = math.sqrt(x * x + y * y)
        #print(f"radius = {math.sqrt(x*x + y*y), radius}")
        normalVector = [x, y]
        self.unitNormalVector = [x / radius, y / radius]
        return self.unitNormalVector


