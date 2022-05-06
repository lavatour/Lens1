import math
import numpy as np

class LinAlg:
    def __init__(self):
        pass

    def dotProd(self, A, B):
        B = np.transpose(B)
        A = np.array(A)
        B = np.array(B)
        dotProd = np.dot(A, B)
        return dotProd

    def crossProd(self, A, B):
        crossProd = np.cross(A, B)
        return crossProd

    def scalarMultiplication(self, scalar, A):
        """Multiply a matrix by a scalar"""
        for i in range(len(A)):
            A[i] = -1 * A[i]
        return A

    def makeUnitVector(self, x1, y1, x2, y2):
        x = x2-x1
        y = y2-y1
        length = math.sqrt(x**2 + y**2)
        ux = x / length
        uy = y / length
        unitVecter = [ux, uy]
        return unitVecter