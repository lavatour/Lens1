import math

class Source():
    def __init__(self, sourceNum, sourceWidth):
        self.sourceNum = sourceNum  #
        self.sourceWidth = sourceWidth
        self.sourceX = 50   # X position of light source
        self.sourceY = 0    # Y position of light source
        self.source = []    # Source position

    def createSource(self):
        for i in range(self.sourceNum):
            self.source.append([self.sourceX, self.sourceY + i * self.sourceWidth / self.sourceNum])
        #print(f"source = {self.source}")
        return self.source