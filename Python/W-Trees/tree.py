class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
    
    def emptyTree(self):
        self.left = None
        self.right = None
        self.data = None
        return self

    def makeTree(self, x, l, r):
        self.data = x
        self.left = l
        self.right = r
        return self
    
    def root(self):
        if self.data is None:
            raise ValueError("root is None")
        return self.data
    
    def left(self):
        if self.left is None:
            raise ValueError("left is None")
        return self.left
    
    def right(self):
        if self.right is None:
            raise ValueError("right is None")
        return self.right
    
    def isLeaf(self):
        return self.left is None and self.right is None
    
    def __str__(self):
        return str(self.data)
