# 顺序查找法


def sequential_search(data, val):
    length = len(data)
    for i in range(length):
        if data[i] == val:
            return i
    return None
