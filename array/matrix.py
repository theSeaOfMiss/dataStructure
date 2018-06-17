from array.makeMatrix import make_matrix
from array.inverseMatrix import inverse_matrix
from array.displayMatrix import display


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
        inv_matrix = inverse_matrix(self.matrix)
        return inv_matrix

    def display_matrix(self):       # 在控制台显示矩阵
        display(self.matrix)
