
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

    def preorder_traversal(self,root=self.root):

        if not root:
            return

        print(' {} ' .format(root.value),end = '')
        self.inorder_traversal(root.left)
        self.inorder_traversal(root.right)

    def inorder_traversal(self,root=self.root):

        if not root:
            return

        self.inorder_traversal(root.left)
        print(' {} ' .format(root.value),end = '')
        self.inorder_traversal(root.right)

    def postorder_traversal(self,root=self.root):

        if not root:
            return

        self.inorder_traversal(root.left)
        self.inorder_traversal(root.right)
        print(' {} ' .format(root.value),end = '')
        


            


