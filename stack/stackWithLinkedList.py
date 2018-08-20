from linkedList.singleLinkedList import LinkList


class Node:
    def __init__(self, data):
        self.data = data


class Stack:
    def __init__(self):
        self.__link = LinkList()

    # 判断是否为空,若不为空，则显示堆栈中有多少节点
    def is_empty(self):
        self.__link.is_empty()

    # 将元素压入栈中
    def push(self, node):
        self.__link.append(node)

    # 推出栈顶元素
    def pop(self):
        self.__link.delete(self.__link.get_length())

    # 返回栈顶元素
    def peek(self):
        length = self.__link.get_length()
        return self.__link.get_node_by_index(length)

    # 返回栈的大小
    def size(self):
        return self.__link.get_length()

