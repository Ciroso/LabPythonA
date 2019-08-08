class ABR:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.p = self.NIL
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.root = self.NIL

    def insert(self, key):  # O(lg n)
        z = Node(key)
        y = self.NIL
        x = self.root
        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.NIL
        z.right = self.NIL

    def searchI(self, key):  # O(h)
        x = self.root
        while x != self.NIL and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        if x == self.NIL:
            return False
        return True

    def inorder_tree_walk(self, x):  # O(n)
        if x is not None:
            self.inorder_tree_walk(x.left)
            print("key = ", x.key)
            self.inorder_tree_walk(x.right)

    def postorder_tree_walk(self, x):
        if x is not None:
            self.postorder_tree_walk(x.left)
            self.postorder_tree_walk(x.right)
            print("key = ", x.key)

    def preorder_tree_walk(self, x):
        if x is not None:
            print("key = ", x.key)
            self.preorder_tree_walk(x.left)
            self.preorder_tree_walk(x.right)

    def min(self, x):  # O(h)
        while x.left is not None:
            x = x.left
        return x

    def max(self, x):  # O(h)
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

    def successor(self, x):  # O(h)
        if x.right is not None:
            return self.min(x.right)
        y = x.p
        while (y is not None) and (x == y.right):
            x = y
            y = y.p
        return y

    def heightRecursive(self, node):
        def recursiveHeight(v):
            if v == self.NIL:
                return 0
            else:
                return max(recursiveHeight(v.left), recursiveHeight(v.right)) + 1
        return recursiveHeight(node) - 1


class Node:
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None
