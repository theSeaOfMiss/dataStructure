# 基数排序法

# 稳定排序法
# 空间复杂度为O(np)，n为原始数据的个数，p为基底
import math


def radix_sort(data, radix=10):
    size = len(data)
    val = max(data)        # data中的最大值
    k = int(math.ceil(math.log(val, radix)))    # 循环数

    for i in range(k):
        bucket = [[] for row in range(radix)]
        for j in range(size):
            m = (data[j] // (radix**i)) % 10      # m为相应位数的值，如36取十位数3
            bucket[m].append(data[j])

        del data[:]
        for l in bucket:
            data += l

    if val % radix == 0:
        count = data.count(val)
        for i in range(count):
            data.remove(val)
            data.append(val)
    return data
