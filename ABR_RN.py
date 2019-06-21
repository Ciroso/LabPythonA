import RandomArray as ra


class ABR_RN:
    def __init__(self):
        self.NIL = Node()
        self.NIL.leaf = True
        self.root = None
#        self.NIL.key = None
#        self.root.color = 0

    def insert(self, key):  # O(lg n)
        z = Node(key)
        y = self.NIL
        x = self.root
        while x is not None and x.leaf is False:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
            #z.isRoot = True
        elif y.leaf is False and z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.NIL
        z.right = self.NIL
        z.color = 1  # Red
        self.fixup(z)

    def fixup(self, z):  # O(1) per lg n livelli -> O(lg n)
        if (z.p is not None) and (z.p.p is not None):  # and (z.p.p.right is not None) and (z.p.p.left is not None):
            while z.p.color == 1:  # Red
                if z.p == z.p.p.left:
                    y = z.p.p.right
                    if y.color == 1:  # Red
                        z.p.color = 0  # Black
                        y.color = 0  # Black
                        z.p.p.color = 1  # Red
                        z = z.p.p
                    elif z == z.p.right:
                        z = z.p
                        self.leftRotate(z)
                    #if (z.p is not None) and (z.p.p is not None) and (z.p.p.right is not None) and (z.p.p.left is not None):
                    z.p.color = 0  # Black
                    z.p.p.color = 1  # Red
                    self.rightRotate(z)
                else:
                    y = z.p.p.left
                    if y.color == 1:  # Red
                        z.p.color = 0  # Black
                        y.color = 0  # Black
                        z.p.p.color = 1  # Red
                        z = z.p.p
                    elif z == z.p.left:
                        z = z.p
                        self.rightRotate(z)
                    #if (z.p is not None) and (z.p.p is not None) and (z.p.p.right is not None) and (z.p.p.left is not None):
                        z.p.color = 0  # Black
                        z.p.p.color = 1  # Red
                    self.leftRotate(z)
            self.root.color = 0  # Black

    def searchR(self, key, x):  # O(lg n)
        if x is None or key == x.key:
            return x
        if key < x.key:
            return self.searchR(key, x.left)
        else:
            return self.searchR(key, x.right)

    def searchI(self, key, x):  # O(lg n)
        while x is not None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def inorder_tree_walk(self, x):  # O(n)
        if x is not None and x.leaf is False:
            self.inorder_tree_walk(x.left)
            print("key = ", x.key)
            self.inorder_tree_walk(x.right)

    def min(self, x):  # O(lg n)
        while x.left is not None:
            x = x.left
        return x

    def max(self, x):  # O(lg n)
        while x.right is not None:
            x = x.right
        return x

    def transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left.NIL is False:
            y.left.p = x
        y.p = x.p
        if x.p.NIL is True:
            x.left = y
            #y.isRoot = True
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right.NIL is False:
            y.right.p = x
        y.p = x.p
        if x.p.NIL is True:
            x.left = y                              # FORSE??
            #y.isRoot = True
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x
        x.p = y


class Node:
    def __init__(self, key=None, left=None, right=None, p=None, color=0, leaf=False, isRoot = False):
        self.key = key
        self.left = left
        self.right = right
        self.p = p
        self.color = color  # 0 = Black, 1 = Red
        self.leaf = leaf
        self.isRoot = isRoot


if __name__ == "__main__":
    T = ABR_RN()
    collectionOfNode = ra.randomArray(100)
    for i in range(0, 100):
        T.insert(collectionOfNode[i])
    T.inorder_tree_walk(T.root)