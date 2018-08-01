# 建立单向列表
# 每个节点储存一个学生的相关信息。
# 姓名，学号，数学成绩，英语成绩。


class Student:
    def __init__(self, name=None, no=None, math=None, english=None):
        self.name = name
        self.no = no
        self.math = math
        self.english = english


class LinkList:
    def __init__(self):
        self.head = None
        self.length = 0

    # 向链表尾部添加节点
    def append(self, node):
        node.next = None
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        self.length += 1

    # 展示链表中所有节点
    def display(self, attr):
        if self.length:
            temp = self.head
            print(getattr(temp, attr))
            while temp.next:
                temp = temp.next
                print(getattr(temp, attr))
        else:
            print('链表中还没有节点！')

    # 判断是否为空,若不为空，则显示链表中有多少节点
    def is_empty(self):
        if self.length:
            print('节点数为：', self.length)
        else:
            print('此链表为空链表！')

    # 通过索引获得相应节点，head的索引为1
    def get_node_by_index(self, index):
        if index > self.length or index <= 0:
            print('索引超出范围！')
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            return temp

    # 在索引为index处插入一个节点,
    def insert(self, index, node):
        if index > self.length or index <= 0:
            print('索引超出范围！')
        else:
            temp = self.head
            if index == 1:
                inter = temp        # 中间变量
                self.head = node
                self.head.next = inter
            else:
                for i in range(index - 2):
                    temp = temp.next
                inter = temp.next       # 中间变量
                temp.next = node
                node.next = inter
            self.length += 1


a = Student('xiaohu', '1', '90', '80')
b = Student('xiaoming', '2', '70', '60')
c = Student('panghu', '3', '60', '50')
d = Student('afu', '4', '30', '60')
link = LinkList()
link.append(a)
link.append(b)
link.append(c)
# link.display('no')
link.insert(4, d)
node1 = link.get_node_by_index(2)
# print(node1.name)
# link.is_empty()
link.display('no')
