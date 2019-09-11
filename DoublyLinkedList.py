class DoublyLinkedList:

    class Node:
        prev = None
        value = None
        next = None
        def __init__(self, value):
            self.value = value

    def __init__(self):
        self.head = None
        print('Initialized Class')

    def insert(self, value):
        newnode = self.Node(value)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp
        self.printlist()

    def delete(self,value):
        flag = False
        if self.head == None:
            print("List is Empty, Nothing to delete")
            return False
        else:
            temp = self.head
            #Delete head of List
            if temp.value == value:
                tobedeleted = temp
                if temp.next != None:
                    temp.next.prev = self.head.prev
                self.head = temp.next
                del(tobedeleted)
                flag = True
            else:
                while temp!=None:
                    if temp.value == value:
                        tobedeleted = temp
                        temp.prev.next = temp.next
                        if temp.next != None:
                            temp.next.prev = temp.prev 
                        del(tobedeleted)
                        flag = True
                        break
                    else:
                        temp = temp.next

        self.printlist()
        if not flag:
            print('Element was not found. Did not delete anything!')

    def printlist(self):
        if self.head == None:
            print('List is empty. Nothing to print!')
        else:
            temp = self.head
            print('None',end='')
            while temp.next != None:
                print(' <- {} -> ' .format(temp.value), end='')
                temp = temp.next
            print(' <- {} -> None' .format(temp.value))

    def reverse(self):
        if self.head == None:
            print('List is empty. Nothing to reverse!')
        else:
            prev = None
            curr = self.head
            next = None
            while curr != None:
                next = curr.next
                curr.next = prev
                curr.prev = next
                prev = curr
                curr = next
            self.head = prev
            self.printlist()

                 


        