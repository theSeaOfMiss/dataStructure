# 插值查找法


def interpolation_search(data, val):
    low = 0
    high = len(data) - 1
    if high == 0:
        if val == data[0]:
            return 0
        else:
            return None

    while low < high:
        # 插值查找法公式
        mid = low + int((high - low) * (val - data[low]) / (data[high] - data[low]))

        if val < data[mid]:
            high = mid - 1
        elif val > data[mid]:
            low = mid + 1
        else:
            return mid

    return None
