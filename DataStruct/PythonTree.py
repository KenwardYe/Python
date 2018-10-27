def binarytree(r):
    return [r, [], []]


def insertleft(root, newbranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newbranch, t, []])
    else:
        root.insert(1, [newbranch, [], []])
    return root


def insertright(root, newbranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newbranch, [], t])
    else:
        root.insert(2, [newbranch, [], []])
    return root


def getrootval(root):
    return root[0]


def setrootval(root, newval):
    root[0] = newval


def getleftchild(root):
    return root[1]


def getrightchild(root):
    return root[2]


def preorder(tree):
    if tree:
        print(tree.getrootval())
        preorder(tree.getleftchild())
        preorder(tree.getrightchild())


def postorder(tree):
    if tree:
        postorder(tree.getleftchild())
        postorder(tree.getrightchild())
        print(tree.getrootval())


def inorder(tree):
    if tree:
        inorder(tree.getleftchild())
        print(tree.getrootval())
        inorder(tree.getrightchild())


class BinaryTree:
    def __init__(self, rootobj):
        self.key = rootobj
        self.leftChild = None
        self.rightChild = None

    def insertleft(self, newnode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertright(self, newnode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getrightchild(self):
        return self.rightChild

    def getleftchild(self):
        return self.leftChild

    def setrootval(self, obj):
        self.key = obj

    def getrootval(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()


class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percup(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i //
                                                2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percup(self.currentSize)

    def percdown(self, i):
        while i * 2 <= self.currentSize:
            mc = self.minchild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc

    def minchild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delmin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percdown(1)
        return retval

    def buildheap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percdown(i)
            i -= 1


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasleftchild(self):
        return self.leftChild

    def hasrightchild(self):
        return self.rightChild

    def isleftchild(self):
        return self.parent and self.parent.leftChild == self

    def isrightchild(self):
        return self.parent and self.parent.rightChild == self

    def isroot(self):
        return not self.parent

    def isleaf(self):
        return not (self.rightChild or self.leftChild)

    def hasanychildren(self):
        return self.rightChild or self.leftChild

    def hasbothchildren(self):
        return self.rightChild and self.leftChild

    def replacenodedata(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasleftchild():
            self.leftChild.parent = self
        if self.hasrightchild():
            self.rightChild.parent = self


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentnode):
        if key < currentnode.key:
            if currentnode.hasleftchild():
                self._put(key, val, currentnode.leftChild)
            else:
                currentnode.leftChild = TreeNode(key, val, parent=currentnode)
        else:
            if currentnode.hasrightchild():
                self._put(key, val, currentnode.rightChild)
            else:
                currentnode.rightChild = TreeNode(key, val, parent=currentnode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentnode):
        if not currentnode:
            return None
        elif currentnode.key == key:
            return currentnode
        elif key < currentnode.key:
            return self._get(key, currentnode.leftChild)
        else:
            return self._get(key, currentnode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodetoremove = self._get(key, self.root)
            if nodetoremove:
                self.remove(nodetoremove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
                self.root = None
                self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def spliceout(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findsuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findmin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
            else:
                self.parent.rightChild = None
                succ = self.parent.findsuccessor()
                self.parent.rightChild = self
        return succ

    def findmin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self, currentnode):
        if currentnode.isLeaf():  # leaf
            if currentnode == currentnode.parent.leftChild:
                currentnode.parent.leftChild = None
            else:
                currentnode.parent.rightChild = None
        elif currentnode.hasBothChildren():  # interior
            succ = currentnode.findsuccessor()
            succ.spliceout()
            currentnode.key = succ.key
            currentnode.payload = succ.payload
        else:  # this node has one child
            if currentnode.hasLeftChild():
                if currentnode.isLeftChild():
                    currentnode.leftChild.parent = currentnode.parent
                    currentnode.parent.leftChild = currentnode.leftChild
                elif currentnode.isRightChild():
                    currentnode.leftChild.parent = currentnode.parent
                    currentnode.parent.rightChild = currentnode.leftChild
                else:
                    currentnode.replaceNodeData(currentnode.leftChild.key,
                                                currentnode.leftChild.payload,
                                                currentnode.leftChild.leftChild,
                                                currentnode.leftChild.rightChild)
            else:
                if currentnode.isLeftChild():
                    currentnode.rightChild.parent = currentnode.parent
                    currentnode.parent.leftChild = currentnode.rightChild
                elif currentnode.isRightChild():
                    currentnode.rightChild.parent = currentnode.parent
                    currentnode.parent.rightChild = currentnode.rightChild
                else:
                    currentnode.replaceNodeData(currentnode.rightChild.key,
                                                currentnode.rightChild.payload,
                                                currentnode.rightChild.leftChild,
                                                currentnode.rightChild.rightChild)