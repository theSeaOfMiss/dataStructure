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
        self.__head = None
        self.__length = 0

    # 向链表尾部添加节点
    def append(self, node):
        if self.is_exist(node):
            print('链表中已包含此数据，请勿重复添加')
            return

        node.next = None
        if not self.__head:
            self.__head = node
        else:
            temp = self.__head
            while temp.next:
                temp = temp.next
            temp.next = node
        self.__length += 1

    # 展示链表中所有节点
    def display(self, attr):
        if self.__length:
            temp = self.__head
            try:
                print(getattr(temp, attr))
            except ValueError as e:
                print('发生错误：', e)
            while temp.next:
                temp = temp.next
                try:
                    print(getattr(temp, attr))
                except ValueError as e:
                    print('发生错误：', e)
        else:
            print('链表中还没有节点！')

    # 判断是否为空,若不为空，则在控制台显示链表中有多少节点
    def is_empty(self):
        if self.__length:
            # print('节点数为：', self.__length)
            return False
        else:
            # print('此链表为空链表！')
            return True

    # 通过索引获得相应节点，head的索引为1
    def get_node_by_index(self, index):
        if index > self.__length or index <= 0:
            print('索引超出范围！')
        else:
            temp = self.__head
            for i in range(index-1):
                temp = temp.next
            return temp

    # 在索引为index处插入一个节点
    def insert(self, index, node):
        if self.is_exist(node):
            print('链表中已包含此数据，请勿重复添加')
            return

        if index > self.__length or index <= 0:
            print('索引超出范围！')
        else:
            temp = self.__head
            if index == 1:
                inter = temp        # 中间变量
                self.__head = node
                self.__head.next = inter
            else:
                for i in range(index - 2):
                    temp = temp.next
                inter = temp.next       # 中间变量
                temp.next = node
                node.next = inter
            self.__length += 1

    # 删除索引处的节点
    def delete(self, index):
        if index > self.__length or index <= 0:
            print('索引超出范围！')
        else:
            temp = self.__head
            if index == 1:
                inter = temp.next
                self.__head = inter
            else:
                for i in range(index - 2):
                    temp = temp.next
                inter = temp.next       # 将需要去掉的节点赋值给inter
                temp.next = inter.next
            self.__length -= 1
            print('成功删除节点%d' % index)

    # 更新索引处的节点
    def update(self, index, node):
        if self.is_exist(node):
            print('链表中已包含此数据，请勿重复添加')
            return

        if index > self.__length or index <= 0:
            print('索引超出范围！')
        else:
            temp = self.__head
            if index == 1:
                inter = temp.next
                self.__head = node
                node.next = inter
            else:
                for i in range(index - 2):
                    temp = temp.next
                inter = temp.next           # 将需要更新的节点赋值给inter
                temp.next = node
                node.next = inter.next
            print('成功更新节点%d' % index)

    # 判断节点是否在链表中存在, 如果存在返回True
    def is_exist(self, node):
        temp = self.__head
        for i in range(self.__length):
            if node == temp:
                return True
            temp = temp.next
        return False

    # 清空链表
    def clear(self):
        self.__head = None
        self.__length = 0
        print('已经清空链表！')

    # 返回链表长度
    def get_length(self):
        return self.__length

