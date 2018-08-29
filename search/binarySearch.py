# 二分查找法
# 数据格式为[1, 3, 5, 9, 10]


def binary_search(data, val):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if val < data[mid]:
            high = mid - 1
        elif val > data[mid]:
            low = mid + 1
        else:
            return mid
    return None
