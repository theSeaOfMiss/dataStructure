# 在控制台显示矩阵


def display(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            print('%-5s' % (matrix[i][j]), ' ', end='')
        print('\n')
