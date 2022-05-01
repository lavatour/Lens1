import math

class SphericalLens():
    def __init__(self, light):
        self.x_c = 500
        self.y_c = 0
        self.radius = 300
        self.light = light

    def equation(self):
        surface = []
        for angle in range(90, 270):
            theta = angle * math.pi / 180
            x = Xc + self.radius * math.cos(theta)
            y = Yc + self.radius * math.sin(theta)
            surface.append([x, y])
        return surface

    def raySurfaceIntersection(self):
        intersection = []
        for source in self.light:
            x, y_0 = source[0], source[1]
            theta = math.asin((y - y_o)/self.radius)
            x = x_0 + self.radius * math.cos(theta)
            y = source[1]
            intersection.append([x, y])
        print(f"intersection = {intersection}")
        return intersection


