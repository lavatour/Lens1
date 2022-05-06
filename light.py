import math

class Light():
    def __init__(self, rayCount):
        self.rayNumber = rayCount
        self.sourceX = 50   # X position of light source
        self.sourceY = 0    # Y position of light source
        self.sourceWidth = 10
        self.ray = []
        self.angle = 0

    def source(self):
        self.ray.append([self.sourceX, self.sourceY + self.rayNumber * self.sourceWidth])
        return self.ray

