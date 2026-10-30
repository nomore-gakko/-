class Matrix:
    def __init__(self,data):
        if not data or not all(isinstance(row,list) for row in data):
            raise ValueError("输入的不是二维列表")
        row_len=len(data[0])
        if not all(len(row)==row_len for row in data):
            raise ValueError("每一行要一样长")
        self.data=[list(row) for row in data]
        self.rows=len(self.data)
        self.cols=row_len
    def __add__(self,other):
        if self.rows!=other.rows or self.cols!=other.cols:
            raise ValueError("矩阵大小不一样啊喂！")
        result=[]
        for i in range(self.rows):
            row=[]
            for j in range(self.cols):
                row.append(self.data[i][j]+other.data[i][j])
            result.append(row)
        return Matrix(result)
    def __mul__(self,other):
       if isinstance(other,(int,float)):
           result=[]
           for i in range(self.rows):
               row=[]
               for j in range(self.cols):
                   row.append(self.data[i][j]*other)
               result.append(row)
           return Matrix(result)
       elif isinstance(other,Matrix):
           if self.cols!=other.rows:
               raise ValueError("乘不了！")
           result=[[0 for _ in range(other.cols)] for _ in range(self.rows)]
           for i in range(self.rows):
              for j in range(other.cols):
                  for k in range(self.cols):
                     result[i][j]+=self.data[i][k]*other.data[k][j]
           return Matrix(result)
    def transpose(self):
        transpose_data=[list(row) for row in zip(*self.data)]
        return Matrix(transpose_data)
    def __str__(self):
        res=""
        for row in self.data:
            res+=" ".join(str(x) for x in row)+"\n"
        return res