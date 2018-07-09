# 将两个矩阵相乘
from array.displayMatrix import display


def matrix_mul(mat1, mat2):
    try:
        M1 = len(mat1)
        N1 = len(mat1[0])
        M2 = len(mat2)
        N2 = len(mat2[0])
    except ValueError as e:
        print('请传入合适的参数。', e)
        return [[]]

    if N1 != M2:
        print('第一个矩阵的列数和第二个矩阵的行数不相等。')
        return [[]]

    result = [[None] * N2 for row in range(M1)]
    for i in range(M1):
        for j in range(N2):
            temp = 0
            for k in range(N1):
                temp += mat1[i][k] * mat2[k][j]
            result[i][j] = temp
    display(result)
    return result
