

class LinearAlgebra:
    def __init__(self):
        pass

    def dotProd(self, A, B):
        [rowsA, colsA] = MatrixMath.size(self, A)
        [rowsB, colsB] = MatrixMath.size(self, B)
        # print(f"rowsA, rowsB = {colsA, colsB}")
        if colsA != colsB:
            print("Error, Dot product impossible, matrices different sizes")
            return
        A = np.array(A)
        B = np.array(B)
        dotProd = np.dot(A, B)
        return dotProd
