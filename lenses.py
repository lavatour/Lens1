import math
import light as Light

class Lens():
    def __init__(self, radius, x_c, y_c, n1, n2):
        self.radius = radius
        self.x_c = x_c
        self.y_c = y_c
        self.unitNormalVector = []
        self.n1 = n1
        self.n2 = n2

        #self.lens1FocalPt = [0, 0]

    def equation(self):
        surface = []
        for angle in range(90, 270):
            theta = angle * math.pi / 180
            x = self.x_c + self.radius * math.cos(theta)
            y = -self.y_c + self.radius * math.sin(theta)
            surface.append([x, y])
        return surface




    def normalVect(self, ray):
        """Calculate normal vector. Confirm by calculating normal angle."""
        x, y = (ray[-1][0] - self.x_c), ray[-1][1]
        radius = math.sqrt(x*x + y*y)
        #print(f"radius = {math.sqrt(x*x + y*y)}")
        normalVector = [x, y]
        self.unitNormalVector = [x / radius, y /  radius]
        return self.unitNormalVector


class SecondLens():
    def __init__(self):
        self.x_c = 965
        self.y_c = 0
        self.radius = 30
        self.unitNormalVector = []


    def equation2(self):
        surface = []
        for angle in range(90, 270):
            theta = angle * math.pi / 180
            x = self.x_c + self.radius * math.cos(theta)
            y = self.y_c + self.radius * math.sin(theta)
            surface.append([x,y])
        #print(surface)
        return surface


    def normalVect(self, ray):
        """Calculate normal vector. Confirm by calculating normal angle."""
        x, y = (ray[-1][0] - self.x_c), ray[-1][1]
        normalTheta = math.atan2(y, x)
        # print(normalTheta * 180 / (math.pi))
        radius = math.sqrt(x * x + y * y)
        #print(f"radius = {math.sqrt(x*x + y*y), radius}")
        normalVector = [x, y]
        self.unitNormalVector = [x / radius, y / radius]
        return self.unitNormalVector
