# 通过list实现堆栈功能


class Stack():
    def __init__(self):
        self.__items = []

    # 判断栈是否为空,如果为空，返回True
    def is_empty(self):
        return self.__items == []

    # 将元素压入栈中
    def push(self, item):
        self.__items.append(item)

    # 推出栈顶元素
    def pop(self):
        self.__items.pop()

    # 返回栈顶元素
    def peek(self):
        length = len(self.__items)
        if length == 0:
            return None
        return self.__items[length - 1]

    # 返回栈的大小
    def size(self):
        return len(self.__items)

