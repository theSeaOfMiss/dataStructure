# 选择排序法

# 不稳定排序法
# 空间复杂度为最佳，只需要一个额外空间O(1)


def select(data):
    length = len(data)
    for i in range(length-1):
        for j in range(i+1, length):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
        print('第%d次排序后的结果是：' % (i+1), data)
