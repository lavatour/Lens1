import math
import light as Light

class SphericalLens():
    def __init__(self):
        self.x_c = 500
        self.y_c = 0
        self.radius = 300
        self.angle = 0
        self.unitNormalVector = []
        self.refIndex = 1.5

    def equation(self):
        surface = []
        for angle in range(90, 270):
            theta = angle * math.pi / 180
            x = self.x_c + self.radius * math.cos(theta)
            y = -self.y_c + self.radius * math.sin(theta)
            surface.append([x, y])
        return surface

    def raySurfaceIntersection(self, ray):
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

    def dotProduct(self, rayVector):
        """Calculate dot product of ray[-1] and the surface normal vector"""




