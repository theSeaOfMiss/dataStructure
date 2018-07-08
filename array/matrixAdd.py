# 将两个矩阵相加
from array.displayMatrix import display

matrix1 = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]     # 声明二维数组
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

M = 3       # 行数
N = 3       # 列数

matrix3 = [[None] * N for row in range(M)]      # 声明一个空数组

for i in range(M):
    for j in range(N):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

print('矩阵一加矩阵二得：')
display(matrix3)
