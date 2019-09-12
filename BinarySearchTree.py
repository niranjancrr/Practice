
class BinarySearchTree:

    class Node:
        left = None
        value = None
        right = None

        def __init__(self, value):
            self.value = value

    def __init__(self):
        print('Binary Search Tree Class Initialized!')
        self.root = None

    def _insert_helper(self,root,newnode):

        if self.root == None:
            self.root = newnode
        else:
            if newnode.value < root.value:
                if root.left == None:
                    root.left = newnode
                    return
                else:
                    self._insert_helper(root.left,newnode)
            else:
                if root.right == None:
                    root.right = newnode
                    return
                else:
                    self._insert_helper(root.right,newnode)
    
    def insert(self, value):

        newnode = self.Node(value)
        self._insert_helper(self.root,newnode)
        self.inorder_traversal(self.root)

    def preorder_traversal(self,root=None):

        if not root:
            return
        else:
            print(' {} ' .format(root.value))
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def inorder_traversal(self,root=None):

        if not root:
            return
        else:
            self.inorder_traversal(root.left)
            print(' {} ' .format(root.value))
            self.inorder_traversal(root.right)

    def postorder_traversal(self,root=None):

        if not root:
            return
        else:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(' {} ' .format(root.value))

    def _mirror_helper(self,root=None):

        if root == None:
            return
        else:
            self._mirror_helper(root.left)
            self._mirror_helper(root.right)
            root.left,root.right = root.right,root.left

    def mirror(self):

        self.inorder_traversal(self.root)
        self._mirror_helper(self.root)
        self.inorder_traversal(self.root)

    def _height_helper(self,root=None):
        if root == None:
            return 0
        else:
            leftheight = self.height(root.left)
            rightheight = self.height(root.right)
            return max(leftheight,rightheight) + 1

    def height(self):
        return self._height_helper(self.root)
        
            


