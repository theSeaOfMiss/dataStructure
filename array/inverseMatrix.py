from array.displayMatrix import display
from array.switchTri import switch_tri
from array.makeMatrix import make_matrix
from array.switchE import switch_e
from copy import deepcopy


# 求矩阵的逆
def inverse_matrix(matrix):
    if not matrix:
        matrix = make_matrix()
    copy_matrix = deepcopy(matrix)
    # display(matrix)
    M = len(matrix)
    N = len(matrix[0])
    if M != N:
        print('请输入n阶矩阵。')
        return []
    result = switch_tri(copy_matrix)
    if result != 0:     # result不等于0，则方阵可逆
        n = 2 * N
        ele_list = []
        for i in range(M):
            for j in range(n):
                if j < M:
                    ele_list.append(matrix[i][j])
                else:
                    if j - M == i:
                        ele_list.append(1)
                    else:
                        ele_list.append(0)
        ass_matrix = make_matrix(M, n, ele_list)
        # display(ass_matrix)
        switch_e(ass_matrix)
        # display(ass_matrix)
        inv_matrix = [[0] * N for row in range(N)]
        for i in range(N):
            for j in range(N):
                inv_matrix[i][j] = ass_matrix[i][j+N]
        print('矩阵的逆为：')
        display(inv_matrix)
        return inv_matrix
    else:
        print('矩阵不可逆')
        return []
