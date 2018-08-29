# 冒泡排序法

# 稳定排序法
# 空间复杂度为最佳，只需要一个额外空间O(1)


def bubble(data):
    length = len(data)
    for i in range(length, 0, -1):
        flag = 1
        for j in range(i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                flag = 0
        if flag:
            break
        # print('第%d次排序后的结果是：' % (length - i + 1), data)
    # print('最终结果为：', data)
    return data
