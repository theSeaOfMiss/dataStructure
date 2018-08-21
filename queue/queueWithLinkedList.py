# 通过链表实现队列功能

from linkedList.singleLinkedList import LinkList


class Node:
    def __init__(self, data):
        self.data = data


class Queue:
    def __init__(self):
        self.__link = LinkList()

    # 判断队列是否为空，如果为空，返回True
    def is_empty(self):
        return self.__link.is_empty()

    # 将新数据加入队列的末尾
    def enqueue(self, node):
        self.__link.append(node)

    # 删除队列前端的数据
    def dequeue(self):
        if self.is_empty():
            print('队列为空队列')
        else:
            self.__link.delete(1)

    # 若队列不为空，则返回头元素
    def peek(self):
        if self.is_empty():
            print('队列为空队列')
        else:
            return self.__link.get_node_by_index(1)

    # 返回队列大小
    def size(self):
        return self.__link.get_length()

