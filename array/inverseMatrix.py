from array.displayMatrix import display
from array.switchTri import switch_tri
from array.makeMatrix import make_matrix
from copy import deepcopy
from array.switchE import switch_e


def inverse_matrix():
    matrix = make_matrix()
    copy_matrix = deepcopy(matrix)
    display(matrix)
    M = len(matrix)
    N = len(matrix[0])
    if M != N:
        print('请输入方阵。')
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
        display(ass_matrix)
        switch_e(ass_matrix)
        display(ass_matrix)
    else:
        print('矩阵不可逆')
        return []


inverse_matrix()




