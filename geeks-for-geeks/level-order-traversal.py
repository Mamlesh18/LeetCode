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

    def bfs(self):
        if self is None:
            return []

        result = []
        queue =deque([self])

        while queue:
            node = queue.popleft()
            result.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result


tree = TreeNode(10)
tree.insert(2)
tree.insert(20)
tree.insert(30)
tree.insert(1)
tree.insert(5)
tree.insert(200)

print(tree.bfs())