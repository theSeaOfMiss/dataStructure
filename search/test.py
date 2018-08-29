# 测试程序
import random
from search.binarySearch import binary_search
from search.fibonacciSearch import fibonacci_search
from search.interpolationSearch import interpolation_search
from search.sequentialSearch import sequential_search


def test(func):
    for i in range(1, 101):
        arr = [None] * i

        arr[0] = 1
        for j in range(1, i):          # 第i次建立一个拥有i个数据的数组
            arr[j] = arr[j-1] + random.randint(1, 10)

        for n in range(i):
            index = func(arr, arr[n])
            # print('arr=', arr, ' ', 'index=', index, ' ', 'n=', n)

            if index != n:
                print(func.__name__, end='')
                print('函数出现bug！')
                print('arr=', arr, ' ', 'index=', index, ' ', 'n=', n)
                return False
    print(func.__name__, end='')
    print('函数没有检查出bug！')
    return True


test(binary_search)
test(interpolation_search)
test(sequential_search)
test(fibonacci_search)
