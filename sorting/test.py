# 测试程序
import random
from sorting.bubbleSort import bubble
from sorting.heapSort import heap_sort
from sorting.insertSort import insert
from sorting.quickSort import quick
from sorting.radixSort import radix_sort
from sorting.selectionSort import select
from sorting.shellSort import shell


def test(func):
    for i in range(1, 101):
        arr = [None] * i

        for j in range(i):
            arr[j] = int(random.random() * 1000)

        # print(arr)
        arr = func(arr)

        for n in range(i-1):
            if arr[n] > arr[n+1]:
                print(func.__name__, end='')
                print('函数出现bug！')
                print('arr=', arr)
                return False
    print(func.__name__, end='')
    print('函数通过测试！')
    return True


test(bubble)
test(heap_sort)
test(insert)
test(quick)
test(radix_sort)
test(select)
test(shell)
