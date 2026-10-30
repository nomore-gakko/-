from matrix_class import Matrix
class SquareMatrix(Matrix):
    def __init__(self,data):
        super().__init__(data)
        if self.rows!=self.cols:
            raise ValueError("不是方阵哦")
    def trace(self):
        return sum(self.data[i][i] for i in range(self.rows))
    def is_symmetric(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j]!=self.data[j][i]:
                    return False
        return True