class Tree:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
    def insert(self,value):
        if value<self.value:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.insert(value)

    def check(self,tree1,tree2):
        if tree1 is None and tree2 is None:
            return True

        if tree1!= None and tree2!= None:
            return (self.check(tree1.left,tree2.left) and self.check(tree1.right, tree2.right))

        return False




tre = Tree(10)
tre.insert(20)
tre.insert(20)


tre2 = Tree(10)
tre2.insert(20)
tre2.insert(20)


print(tre.check(tre,tre2))