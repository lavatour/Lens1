import math
import light as Light

class FirstLens():
    def __init__(self):
        self.x_c = 500
        self.y_c = 0
        self.radius = 300
        self.unitNormalVector = []
        self.refIndex = 1.5
        #self.lens1FocalPt = [0, 0]

    def equation(self):
        surface = []
        for angle in range(90, 270):
            theta = angle * math.pi / 180
            x = self.x_c + self.radius * math.cos(theta)
            y = -self.y_c + self.radius * math.sin(theta)
            surface.append([x, y])
        return surface


    def rayLens1Intersection(self, ray):
        #intersection = []
        #print(f"ray = {ray[-1]}")
        y = ray[-1][1]
        theta = math.pi + math.asin((y + self.y_c) / self.radius) #
        x = self.x_c + self.radius * math.cos(theta)
        ray.append([x, y])
        #print(f"inside ray = {ray}")
        return ray


    def normalVect(self, ray):
        """Calculate normal vector. Confirm by calculating normal angle."""
        x, y = (ray[-1][0] - 500), ray[-1][1]
        normalTheta = math.atan2(y, x)
        #print(normalTheta * 180 / (math.pi))
        radius = math.sqrt(x*x + y*y)
        #print(f"radius = {math.sqrt(x*x + y*y)}")
        normalVector = [x, y]
        self.unitNormalVector = [x / radius, y /  radius]
        return self.unitNormalVector


    #def dotProduct(self, rayVector):
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
        z = 1
        while abs(((x - h) ** 2 + (y - k) ** 2)- self.radius ** 2) > 0.000001:
            print(f"h, k = {h, k}")
            print(f"x, y = {x, y}")
            dist = math.sqrt((x - self.xc)**2 + (y - self.yc)**2 ) - self.radius
            #print(f"dist, dist * math.cos(angle[-1]) = {dist, dist * math.cos(angle[-1]) - self.radius}")
            print(f"((x - h)**2 + (y - k)**2) - self.radius**2, {((x - h)**2 + (y - k)**2) - self.radius**2}")
            x = x + dist * math.cos(angle[-1])
            y = y + dist * math.sin(angle[-1])
            print(f"x, y = {x, y}")
            print(f"((x - h)**2 + (y - k)**2) - self.radius**2  = {((x - h)**2 + (y - k)**2) - self.radius**2}")
            print(f"(abs((x - h)**2 + (y - k)**2) - self.radius**2) = {abs(((x - h) ** 2 + (y - k) ** 2)- self.radius ** 2)}")
            if abs((x - h)**2 + (y - k)**2) - self.radius**2 > 1:
                print("keep going")
            print()
            z += 1
            if z > 10:
                print()
                break



"""
    def rayLens2Intersection(self, ray):
        h , k = self.xc, self.yc
        r = self.radius
        x1, y1 = ray[-2][0], ray[-2][1]
        x2, y2 = ray[-1][0], ray[-1][1]
        m = (y2 - y1) / (x2- x1)
        b = -1*m*x1 + y1
        A = m**2 + 1
        B = 2*m*b
        C = b**2  - r**2
        if ray[0][1] == 40:
            print(f"h, k = {h}, {k}")
            print(f"ray = {ray}")
            print(f"x1, y1, x2, y2 = {round(x1, 3)}, {round(y1, 3)}, {round(x2, 3)}, {round(y2, 3)}")
            print(f"m = {m}")
            print(f"b = {b}")
            print(f"A, B, C = {A}, {B}, {C}")
            print(f"B**2-4*A*C = {B**2-4*A*C}")
"""