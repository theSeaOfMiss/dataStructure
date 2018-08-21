# 通过list实现队列的功能


class Queue:
    def __init__(self):
        self.items = []

    # 判断队列是否为空，如果为空，返回True
    def is_empty(self):
        return self.items == []

    # 将新数据加入队列的末尾
    def enqueue(self, item):
        self.items.append(item)

    # 删除队列前端的数据
    def dequeue(self):
        if self.is_empty():
            print('队列为空队列')
        else:
            value = self.items[0]
            self.items.remove(value)

    def peek(self):
        if self.is_empty():
            print('队列为空队列')
        else:
            return self.items[0]
            
    def size(self):
        return len(self.items)
