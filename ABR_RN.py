class ABR_RN:
    def __init__(self):
        self.NIL = Node(None)
        self.NIL.color = 0
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
        z.color = 1  # Red
        self.fixup(z)

    def fixup(self, z):  # O(1) per lg n livelli -> O(lg n)
        while z.p.color == 1:  # Red
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == 1:  # Red
                    z.p.color = 0  # Black
                    y.color = 0  # Black
                    z.p.p.color = 1  # Red
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.leftRotate(z)
                    z.p.color = 0  # Black
                    z.p.p.color = 1  # Red
                    self.rightRotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == 1:  # Red
                    z.p.color = 0  # Black
                    y.color = 0  # Black
                    z.p.p.color = 1  # Red
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.rightRotate(z)
                    z.p.color = 0  # Black
                    z.p.p.color = 1  # Red
                    self.leftRotate(z.p.p)
        self.root.color = 0  # Black

    def searchI(self, key):  # O(lg n)
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
        if x != self.NIL:
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
        if y.left != self.NIL:
            y.left.p = x
        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.p = x
        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

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
        self.color = None    # 0 = Black, 1 = Red
        self.p = None
        self.left = None
        self.right = None


if __name__ == "__main__":
    T = ABR_RN()
    #collectionOfNode = ra.randomArray(100)
    for i in range(0, 10):
        print("nodo", i)
        T.insert(i+1)
    T.inorder_tree_walk(T.root)
