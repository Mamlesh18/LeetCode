class TreeNode:
    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
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
    def height(self):

        if not self:
            return -1

        left_height = self.left.height() if self.left else -1
        right_height = self.right.height() if self.right else -1

        return 1 + max(left_height, right_height)

n = int(input("enter root node"))
tree = TreeNode(n)
k = int(input("enter how many values you want to put int a tree -> "))

for i in range(k):
    nu = int(input("emelents: "))
    tree.insert(nu)
print(tree.height())