class ABR:
    def __init__(self):
        self.root = None

    def insert(self, key):  # O(h) con h = lg n  nel caso migliore e  h = n nel caso peggiore
        z = Node(key)
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def searchR(self, key, x):  # O(h)
        if x is None or key == x.key:
            return x
        if key < x.key:
            return self.searchR(key, x.left)
        else:
            return self.searchR(key, x.right)

    def searchI(self, key, x):  # O(h) (più veloce del ricorsivo)
        while x is not None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

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


class Node:
    def __init__(self, key=None, left=None, right=None, p=None):
        self.key = key
        self.left = left
        self.right = right
        self.p = p

