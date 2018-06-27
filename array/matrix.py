from array.makeMatrix import make_matrix
from array.inverseMatrix import inverse_matrix
from array.displayMatrix import display
from array.switchTri import switch_tri
from copy import deepcopy


class Matrix:
    def __init__(self, m=0, n=0, ele_list=[]):
        try:
            m = int(m)
            n = int(n)
        except ValueError as e:
            print('行数与列数输入错误类型， 错误类型以0处理。', e)
            m = 0
            n = 0
        self.m = m      # 矩阵的行数
        self.n = n      # 矩阵的列数
        self.matrix = make_matrix(m, n, ele_list)

    def add_matrix(self, matrix):
        if isinstance(matrix, Matrix):      # 判断matrix是不是Matrix的实例
            pass
        else:
            pass

    def sub_matrix(self, matrix):
        if isinstance(matrix, Matrix):  # 判断matrix是不是Matrix的实例
            pass
        else:
            pass

    def mul_matrix(self, matrix):
        if isinstance(matrix, Matrix):  # 判断matrix是不是Matrix的实例
            pass
        else:
            pass

    def inv_matrix(self):       # 求矩阵的逆矩阵
        ass_matrix = deepcopy(self.matrix)      # 辅助矩阵，为了不改变self.matrix
        inv_matrix = inverse_matrix(ass_matrix)
        return inv_matrix

    def display_matrix(self):       # 在控制台显示矩阵
        display(self.matrix)

    def switch_tri(self):       # 将矩阵化为三角矩阵
        ass_matrix = deepcopy(self.matrix)
        tri_matrix = switch_tri(ass_matrix)
        return tri_matrix
