class Matrix:
    def __init__(self, m=0, n=0):
        try:
            m = int(m)
            n = int(n)
        except ValueError as e:
            print('输入错误类型， 错误类型以0处理。', e)
            m = 0
            n = 0
        self.m = m      # 矩阵的行数
        self.n = n      # 矩阵的列数

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


