from collections import deque
class TreeNode:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self,value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
    def pre_order(self):
        print(self.value,end = " ")
        if self.left:
            self.left.pre_order()

        if self.right:
            self.right.pre_order()

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(" -> ", self.value,end = "")

        if self.right:
            self.right.inorder_traversal()



    def post_order(self):

        if self.left:
            self.left.post_order()

        if self.right:
            self.right.post_order()

        print(" -> ", self.value,end = "")


    def find(self,value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:

            return True

    def height(self):
        if self is None:
            return -1

        left_height = self.left.height() if self.left else -1
        right_height = self.right.height() if self.right else -1

        return 1 + max(left_height, right_height)

    def traversal(self):
        q = []
        q.append(self)

        while len(q) != 0:
            current = q.pop(0)
            print(current.value)

            if current.left:
                q.append(current.left)

            if current.right:
                q.append(current.right)

    def top_view(self):
        if not self:
            return

        q = deque([(self, 0)])  # Use deque for efficient pop from both ends
        d = {}

        while q:
            current, hd = q.popleft()

            if hd not in d:
                d[hd] = current.value
                print(current.value)

            if current.left:
                q.append((current.left, hd - 1))

            if current.right:
                q.append((current.right, hd + 1))

    def level(self):
        if not self:
            return
        l = []

        q = deque([(self, 0)])  # (node, level)
        while q:
            current, level = q.popleft()
            #print(f"Node: {current.value}, Level: {level}")
            l.append(level)


            if current.left:
                q.append((current.left, level + 1))

            if current.right:
                q.append((current.right, level + 1))
        return max(l)


tree = TreeNode(10)
tree.insert(5)
tree.insert(11)
tree.insert(12)
tree.insert(7)
tree.insert(1)
tree.insert(10)
tree.insert(3)
tree.insert(3)
tree.insert(5)
tree.insert(5)
tree.insert(5)
print(tree)
# tree.inorder_traversal()
#
#
# tree.post_order()

# print(tree.find(1))
#
# print(tree.height())
#
# # print(tree.traversal())
#
# # print(tree.top_view())
#
# print(tree.level())