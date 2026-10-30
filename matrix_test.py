"""from matrix_class import Matrix
A = Matrix([[1, 2], 
            [3, 4]])

# 2. 打印看看效果（会自动调用你写的 __str__ 方法）
print("矩阵 A:")
print(A)

# 3. 测试数乘
print("A 乘以 2:")
print(A * 2)

# 4. 测试矩阵加法
B = Matrix([[5, 6], 
            [7, 8]])
print("A + B:")
print(A + B)

# 5. 测试转置
print("A 的转置:")
print(A.transpose())"""
from matrix_class import Matrix
from square_matrix import SquareMatrix

print("=== 测试方阵的独有功能 ===")

# 1. 创建一个正确的方阵
sm = SquareMatrix([[1, 2, 3],
                   [2, 4, 5],
                   [3, 5, 6]])
print("打印方阵 sm:")
print(sm)

# 2. 测试计算迹 (trace)
# 1 + 4 + 6 = 11
print(f"sm 的迹: {sm.trace()}") 

# 3. 测试是否对称 (is_symmetric)
# 这是一个对称矩阵，应该返回 True
print(f"sm 是对称矩阵吗: {sm.is_symmetric()}")

# 4. 创建一个不对称的方阵
sm2 = SquareMatrix([[1, 0, 0],
                    [2, 4, 0],
                    [3, 5, 6]])
print(f"\nsm2 是对称矩阵吗: {sm2.is_symmetric()}") # 应该返回 False

print("\n=== 测试继承和拦截功能 ===")

# 5. 测试继承：子类能不能直接用父类的加法？
sm3 = SquareMatrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print("两个方阵相加 (调用父类 __add__):")
print(sm + sm3)  # 完美运行，因为继承了父类

# 6. 测试拦截：如果输入的不是方阵会怎样？
print("\n尝试创建一个 2x3 的非方阵（应该报错）：")
try:
    error_matrix = SquareMatrix([[1, 2, 3], 
                                 [4, 5, 6]])
except ValueError as e:
    print(f"成功捕获报错: {e}")