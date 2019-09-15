#Depth First Search Implementation

from Stack import Stack

stack = Stack() 

def dfs(root, value, flag = False):

    if root == None:
        return
    elif flag == True:
        return True
    else:
        stack.push(root)
        print('Pushed {}' .format(root.value))
        while len(stack) > 0:
            element = stack.pop()
            print('Popped {}' .format(element.value))
            if element.value == value:
                print('Value was found')
                flag = True
                break
            if element.left:
                flag = dfs(element.left,value,flag)
            if element.right:
                flag = dfs(element.right,value,flag)
    
    return flag

if __name__ == '__main__':
    from BinarySearchTree import BinarySearchTree
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(4)
    bst.insert(2)
    bst.insert(3)
    bst.insert(7)
    bst.insert(6)
    bst.insert(8)
    bst.insert(10)

    print(dfs(bst.root,2))
    print(dfs(bst.root,3))
    print(dfs(bst.root,7))
    print(dfs(bst.root,6))
    print(dfs(bst.root,8))
    print(dfs(bst.root,9))