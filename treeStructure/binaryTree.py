# 因为相比于三叉树四叉树来说，二叉树的链接浪费率最低，
# 所以最常使用二叉树结构来取代其他树形结构

# 二叉排序树或者是一棵空树，或者是具有下列性质的二叉树：
# （1）若左子树不空，则左子树上所有结点的值均小于或等于它的根结点的值；
# （2）若右子树不空，则右子树上所有结点的值均大于或等于它的根结点的值；
# （3）左、右子树也分别为二叉排序树；

# 下面是二叉排序树的实现


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.__root = None

    def is_exist(self, data):
        ptr = self.__root
        while True:
            if ptr is None:
                return False
            if ptr.data == data:
                return True
            elif ptr.data > data:
                ptr = ptr.left
            else:
                ptr = ptr.right

    def add(self, node):
        if self.is_exist(node.data):
            print('二叉树中已有此节点')
            return
        if self.__root is None:
            self.__root = node
        else:
            current = self.__root     # 表示当前所在节点
            while True:
                if current.data > node.data:
                    if current.left is None:
                        current.left = node
                        return
                    current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        return
                    current = current.right

    # 遍历函数
    @staticmethod
    def __traversal(root, opt):
        if root is None:
            return []
        result = [root.data]
        left_data = Tree.__traversal(root.left, opt)
        right_data = Tree.__traversal(root.right, opt)
        if opt == 'INORDER':
            return left_data + result + right_data
        elif opt == 'POSTORDER':
            return left_data + right_data + result
        elif opt == 'PREORDER':
            return result + left_data + right_data

    # 中序遍历，左子树->树根->右子树
    def inorder(self):
        return Tree.__traversal(self.__root, 'INORDER')

    # 后序遍历
    def postorder(self):
        return Tree.__traversal(self.__root, 'POSTORDER')

    # 前序遍历
    def preorder(self):
        return Tree.__traversal(self.__root, 'PREORDER')

