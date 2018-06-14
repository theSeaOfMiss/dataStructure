from array.switchTri import switch_tri


def switch_e(matrix):
    result = switch_tri(matrix)
    if result == 0:
        print('矩阵不可单位化')
    else:
        M = len(matrix)
        N = len(matrix[0])
        if M <= N:
            switch_tri(matrix, 'l')
            for i in range(M):
                if matrix[i][i] != 1:
                    k = matrix[i][i]
                    for j in range(N):
                        matrix[i][j] = matrix[i][j] / k
        else:
            print('矩阵不符合要求')
