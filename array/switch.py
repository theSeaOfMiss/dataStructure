# 将M行*N列（M<=N）矩阵转换为前M*M为上三角矩阵
def switch(matrix):
    M = len(matrix)
    N = len(matrix[0])
    if M <= N:
        for count in range(M-1, 0, -1):
            n = M - 1 - count
            for i in range(count):
                m = i + 1 + n
                if matrix[m][n] != 0:
                    k = matrix[m][n] / matrix[n][n]
                    print('k=', k, i)
                    for j in range(N):
                        matrix[m][j] = matrix[m][j] - k * matrix[n][j]
                else:
                    pass
    else:
        print('请输入行小于列的矩阵')
