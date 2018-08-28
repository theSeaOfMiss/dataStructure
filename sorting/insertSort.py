# 插入排序法

# 稳定排序法
# 空间复杂度为最佳，只需要一个额外空间O(1)


def insert(data):
    length = len(data)
    for i in range(1, length):
        tmp = data[i]       # 暂存需要插入的数据
        count = i - 1       # 已经插入的数据个数-1
        while count >= 0 and tmp < data[count]:
            data[count + 1] = data[count]
            count -= 1
        data[count + 1] = tmp
    return data
