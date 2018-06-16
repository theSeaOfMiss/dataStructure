def make_matrix(M=0, N=0, ele_list=[]):      # 生成M行N列矩阵
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
    matrix = [[0] * N for row in range(M)]       # 声明M*N的数组arr并将所有元素设置为0
    # display(matrix)
    if len(ele_list) == 0:
        element = input('请输入方阵的元素(按行展开，以空格分开): ')
        ele_list = element.strip(' ').split(' ')
    length = len(ele_list)
    for i in range(M):      # 将输入变成float，加入矩阵中
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
