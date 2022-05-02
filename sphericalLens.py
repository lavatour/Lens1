import math
import light as Light

class SphericalLens():
    def __init__(self):
        self.x_c = 500
        self.y_c = 0
        self.radius = 300

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
        print(f"inside ray = {ray}")
        return ray


