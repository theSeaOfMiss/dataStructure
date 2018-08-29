# 斐波拉契查找法

# 斐波拉契树

# 斐波拉契数
# def fib(n):
#     if n == 1 or n == 0:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)


def fibonacci_search(data, val):
    size = len(data)
    fib = [0, 1]      # 斐波那契数列的缓存

    while fib[-1] <= size:
        fib.append(fib[-1] + fib[-2])

    index = len(fib) - 2

    root = fib[index]

    while True:
        if index <= 0:
            return None

        if data[root-1] > val:
            root = root - fib[index-2]
            index -= 1
        elif data[root-1] < val:
            root = root + fib[index-2]
            index -= 2
            # root有可能大于data数组长度
            while root > size:
                root = root - fib[index - 2]
                index -= 1
        else:
            return root - 1
