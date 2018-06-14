from array.displayMatrix import display


def calculate(matrix, sign=1):      # 计算上三角方阵部分的行列式值
    M = len(matrix)
    result = sign
    for i in range(M):
        result = result * matrix[i][i]
    print('前%d行方阵计算结果为：' % M, result)
    return result


def switch_tri(matrix, option='u'):     # 将M行*N列（M<=N）矩阵转换为前M*M为上三角矩阵
    M = len(matrix)
    N = len(matrix[0])
    sign = 1        # 矩阵的行列式前的正负号
    if M <= N:
        for count in range(M-1, 0, -1):
            if option == 'u':
                n = M - 1 - count
            else:
                n = count
            if matrix[n][n] == 0:       # 如果matrix[n][n]为0，则交换两行
                for s in range(count):      # 遍历寻找matrix[?][n]不为0的行
                    if option == 'u':
                        m = n + s + 1
                    else:
                        m = n - s - 1
                    if matrix[m][n] != 0:
                        sign = sign * -1
                        for z in range(N):      # 将矩阵两行相互交换
                            matrix[m][z], matrix[n][z] = matrix[n][z], matrix[m][z]
                        break
            for i in range(count):
                if option == 'u':
                    m = i + 1 + n
                else:
                    m = n - i - 1
                if matrix[m][n] != 0:
                    k = matrix[m][n] / matrix[n][n]
                    for j in range(N):
                        matrix[m][j] = matrix[m][j] - k * matrix[n][j]
        result = calculate(matrix, sign)     # 计算上三角方阵部分的行列式值
        display(matrix)
        return result
    else:
        print('请输入行小于列的矩阵')
        return 0
