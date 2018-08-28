# 基数排序法

# 稳定排序法
# 空间复杂度为O(np)，n为原始数据的个数，p为基底
import math


def radix_sort(lists, radix=10):
    size = len(lists)
    val = max(lists)        # lists中的最大值
    k = int(math.ceil(math.log(val, radix)))    # 循环数

    for i in range(k):
        bucket = [[] for row in range(radix)]
        for j in range(size):
            m = (lists[j] // (radix**i)) % 10      # m为相应位数的值，如36取十位数3
            bucket[m].append(lists[j])

        lists = []
        for l in bucket:
            lists += l

    if val % radix == 0:
        count = lists.count(val)
        for i in range(count):
            lists.remove(val)
            lists.append(val)
    return lists
