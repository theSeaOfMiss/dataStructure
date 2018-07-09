# 定义一个生成矩阵的函数


def gen_matrix(M=0, N=0, ele_list=[]):      # 生成M行N列矩阵
    try:
        M = int(M)
        N = int(N)
        if type(ele_list) != list:
            return [[]]
    except ValueError as e:
        print('输入错误类型。', e)
        return [[]]

    if M == 0 & N == 0:
        try:
            M = int(input('请输入矩阵的行数：'))
            N = int(input('请输入矩阵的列数：'))
        except ValueError as e:
            print('输入错误类型。', e)
            return [[]]
    if M < 0 | N < 0:
        print('请输入大于零的行数或列数')
        return [[]]

    matrix = [[None] * N for row in range(M)]       # 声明M*N的数组arr并将所有元素设置为0

    length = len(ele_list)
    if length == 0:
        for i in range(M):
            for j in range(N):
                try:
                    matrix[i][j] = float(input('a%d%d=' % (i, j)))
                except ValueError as e:
                    print('输入类型错误。', e)
                    return [[]]
        return matrix

    for i in range(M):
        for j in range(N):
            index = i * N + j
            if index < length:
                try:
                    ele = float(ele_list[index])
                except ValueError as e:
                    print('输入错误类型， 错误类型以0处理。', e)
                    ele = 0
            else:
                ele = 0
            matrix[i][j] = ele
    return matrix
