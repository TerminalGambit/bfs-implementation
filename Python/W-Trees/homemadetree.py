class Tree:
    def __init__(self, array=None, parcours=None):
        self.left = None
        self.right = None
        self.data = None
        if array is not None:
            self.makeTreeFromArray(array, parcours)
        
    def makeTreeFromArray(self, array, parcours):
        if len(array) == 0:
            self.emptyTree()
        else:
            if parcours == "prefix":
                pass
            elif parcours == "infix":
                pass
            elif parcours == "postfix":
                pass
            else:
                raise ValueError("parcours is not valid")

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
