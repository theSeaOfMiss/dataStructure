# 显示矩阵
def display(matrix):
    M = len(matrix)
    N = len(matrix[0])
    for i in range(M):
        for j in range(N):
            print('%-5s' % (matrix[i][j]), ' ', end='')
        print('\n')
