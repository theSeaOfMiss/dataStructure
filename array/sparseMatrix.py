# 稀疏矩阵的压缩（矩阵中大部分元素为零）
from array.displayMatrix import display

# 声明稀疏矩阵
Sparse = [[15, 0, 0, 22, 0, -15], [0, 11, 3, 0, 0, 0],
          [0, 0, 0, -6, 0, 0], [0, 0, 0, 0, 0, 0],
          [91, 0, 0, 0, 0, 0], [0, 0, 28, 0, 0, 0]]
# display(Sparse)


def compress(matrix):
    m = len(matrix)     # 矩阵的行数
    n = len(matrix[0])      # 矩阵的列数
    non_zero = 0
    temp = 1

    for i in range(m):
        for j in range(n):
            if matrix[i][j] != 0:
                non_zero += 1
    # 声明最后输出的压缩矩阵
    result = [[None] * 3 for row in range(non_zero+1)]

    result[0][0] = m        # 储存矩阵的行数
    result[0][1] = n        # 储存矩阵的列数
    result[0][2] = non_zero  # 储存矩阵的非零项的总数

    for i in range(m):
        for j in range(n):
            if matrix[i][j] != 0:
                result[temp][0] = i
                result[temp][1] = j
                result[temp][2] = matrix[i][j]
                temp += 1

    return result


display(compress(Sparse))
