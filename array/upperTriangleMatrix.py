# 右上三角形矩阵储存在一维数组中
# 此矩阵行数与列数相同。

from array.displayMatrix import display
import math

# 上三角矩阵的内容
A = [[7, 8, 12, 21, 9],
     [0, 5, 14, 17, 6],
     [0, 0, 7, 23, 24],
     [0, 0, 0, 32, 19],
     [0, 0, 0, 0, 8]]

print('上三角形矩阵：')
display(A)


def compress_to_1D(matrix):     # 定义一个将右上三角矩阵压缩为一维数组的函数
    m = len(matrix)  # 矩阵的行数
    n = len(matrix[0])  # 矩阵的列数

    if m != n:
        return []

    num = int(n * (1 + n) / 2)
    result = [None] * num
    index = 0

    for i in range(m):
        for j in range(n):
            if j >= i:
                result[index] = matrix[i][j]
                index += 1

    return result


print(compress_to_1D(A))


def get_value(i, j, arr):      # i、j为未压缩前下标（从零开始），arr为一维数组
    length = len(arr)
    n = int(math.sqrt(length * 2))
    if i >= n or j >= n:
        print('输入下标错误！')
        return None

    if j < i:
        print('此为右上三角形矩阵，第二个参数需大于等于第一个参数！')
        return None

    index = int(n * i + i * (1 - i) / 2 + j - i)
    return arr[index]


print(get_value(5, 3, compress_to_1D(A)))


