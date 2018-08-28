# 快速排序法

# 不稳定排序法
# 空间复杂度最差为O(n), 最佳为O(log2n)


def quick(data):
    def assist(d, start, end):
        if start < end:
            i, j = start, end
            base = d[i]      # 设置基准数

            while i < j:

                # 从左向右寻找第一个小于基准数的下标
                while (i < j) and (d[j] >= base):
                    j -= 1

                d[i] = d[j]

                # 从右向左寻找第一个大于基准数的下标
                while (i < j) and (d[i] <= base):
                    i += 1

                d[j] = d[i]

            d[i] = base

            assist(d, start, i - 1)
            assist(d, j + 1, end)
        
    assist(data, 0, len(data)-1)
    return data
