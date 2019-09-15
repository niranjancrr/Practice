
#Breadth First Search Implementation

from Queue import Queue

queue = Queue()

def bfs(root,value,flag=False):

    if root == None:
        return
    else:
        queue.enqueue(root)
        print('inserting root {}' .format(root.value))

        while len(queue) > 0:
            entry = queue.dequeue()
            print('dequeued {}' .format(entry.value))
            if entry.value == value:
                print('Value was found')
                flag = True
                break
            if entry.left:
                print('enqueued left {}' .format(entry.left.value))
                queue.enqueue(entry.left)
            if entry.right:
                print('enqueued right {}' .format(entry.right.value))
                queue.enqueue(entry.right)
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

    bfs(bst.root,3)



