# 希尔排序法

# 稳定排序法
# 空间复杂度为最佳，只需要一个额外空间O(1)


def shell(data):
    length = len(data)
    jmp = length // 2       # jmp为设置的间距的位移量
    k = 1                   # 打印计数
    while jmp != 0:
        for i in range(jmp, length):
            tmp = data[i]
            j = i - jmp
            while tmp < data[j] and j >= 0:
                data[j + jmp] = data[j]
                j = j - jmp
            data[jmp + j] = tmp
        print('第%d次排序后的结果是：' % k, data)
        k += 1
        jmp = jmp // 2
