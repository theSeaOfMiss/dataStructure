N = 2
# 声明2*2的数组arr并将所有元素设置为None
arr = [[None] * N for row in range(N)]
print('|a11 a12|')
print('|a21 a22|')
arr[0][0] = input('请输入a11：')
arr[0][1] = input('请输入a12：')
arr[1][0] = input('请输入a21：')
arr[1][1] = input('请输入a22：')
# 求二阶行列式的值
a11 = int(arr[0][0])
a12 = int(arr[0][1])
a21 = int(arr[1][0])
a22 = int(arr[1][1])
result = a11 * a22 - a12 * a21
print('|%d %d|' %(a11, a12))
print('|%d %d|' %(a21, a22))
print('行列式的值=%d' %result)