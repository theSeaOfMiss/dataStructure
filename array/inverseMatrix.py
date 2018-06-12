from array import displayMatrix as Display
from array import switch

N = int(input('请输入方阵的阶数：'))
matrix = [[None] * N for row in range(N)]       # 声明N*N的数组arr并将所有元素设置为None
Display.display(matrix)
element = input('请输入方阵的元素(按行展开，以空格分开): ')
ele_list = element.strip(' ').split(' ')
length = len(ele_list)

for i in range(N):      # 将输入变成int
    for j in range(N):
        index = i * N + j
        if index < length:
            try:
                ele = float(ele_list[index])
            except ValueError as e:
                print('输入错误类型， 错误类型以0处理', e)
                ele = 0
        else:
            ele = 0
        matrix[i][j] = ele
print('n阶方阵为：', matrix)

Display.display(matrix)
switch.switch(matrix)
print('/n')
Display.display(matrix)


