# 转置矩阵
from array.displayMatrix import display

arrA = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

N = 4
# 声明4*4数组arr
arrB = [[None] * N for row in range(N)]

print('原设置的矩阵内容')
display(arrA)

# 进行矩阵转置的操作
for i in range(4):
    for j in range(4):
        arrB[i][j] = arrA[j][i]

print('转置后矩阵的内容')
display(arrB)
