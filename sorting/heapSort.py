# 堆积排序法

# 不稳定排序法
# 空间复杂度为最佳，只需要一个额外空间O(1)


# 调整堆
def adjust_heap(lists, i, size):
    l_child = 2 * i + 1             # 二叉树第i个节点的左子节点
    r_child = 2 * i + 2             # 二叉树第i个节点的右子节点
    max_index = i                   # 二叉树第i个节点和其左右子节点中的最大值在list中的索引
    if i < size / 2:
        if l_child < size and lists[l_child] > lists[max_index]:
            max_index = l_child
        if r_child < size and lists[r_child] > lists[max_index]:
            max_index = r_child
        if max_index != i:
            lists[max_index], lists[i] = lists[i], lists[max_index]
            adjust_heap(lists, max_index, size)


# 创建堆积树
def build_heap(lists, size):
    for i in range(0, size//2)[::-1]:
        adjust_heap(lists, i, size)


# 堆排序
def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
        print('dd', lists)
    return lists
