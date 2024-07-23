from collections import deque, defaultdict
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self,val):
        if val < self.value:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value)

    def find(self,val):
        if val < self.value:
            if self.left is None:
                return False
            else:
               return self.left.find(val)
        elif val > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(val)
        else:
            return True

    def height(self):
        if self is None:
            return -1

        leftmax = self.left.height() if self.left else -1
        rightmax = self.right.height() if self.right else -1

        return 1 + max(leftmax,rightmax)

    def leftview(self):
        if not self:
            return

        queue = deque([(self,0)])
        maxlevel = -1
        while queue:
            node, level = queue.popleft()
            if level > maxlevel:
                print(node.value)
                maxlevel = level
            if node.left:
                queue.append((node.left,level + 1))
            if node.right:
                queue.append((node.right,level + 1))

    def rightview(self):
        if not self:
            return

        queue = deque([(self,0)])
        maxlevel = -1
        while queue:
            node,level = queue.popleft()
            if level > maxlevel:
                print(node.value)
                maxlevel = level
            if node.right:
                queue.append((node.right,level+1))
            if node.left:
                queue.append((node.left,level+1))

    def topview(self):

        if not self:
            return

        hmap = {}
        queue = deque([(self,0)])
        while queue:
            node,level = queue.popleft()
            if level not in hmap:
                hmap[level] = node.value

            if node.left:
                queue.append((node.left,level -1))
            if node.right:
                queue.append((node.right,level+1))
        for i in hmap:
            print(hmap[i])
    def levelorder(self):

        if not self:
            return
        queue = deque([self])
        result = []
        while queue:
            level_res = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level_res.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_res)
        return result

    def vertical_order(self):
        if not self:
            return []
        vertical_dict = defaultdict(list)
        queue = deque([(self, 0)])
        while queue:
            node, hd = queue.popleft()
            vertical_dict[hd].append(node.value)

            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        sorted_vertical = sorted(vertical_dict.items())
        return [values for hd, values in sorted_vertical]


root= int(input('root'))
tree = TreeNode(root)
tree.insert(3)
tree.insert(6)
tree.insert(1)
tree.insert(8)
tree.insert(2)
tree.insert(9)


# tree.postorder()
# print(tree.find(1))
# print(tree.height())

# print(tree.leftview())
# print(tree.rightview())
# print(tree.topview())
# print(tree.levelorder())
# print(tree.vertical_order())