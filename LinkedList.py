class LinkedList:

    class Node:
        value = None
        next = None
        def __init__(self,value):
            self.value = value

    def __init__(self):
        print('Initialized class')
        self.head = None
        self.len = 0
    
    def __len__(self):
        return self.len

    def insert_start(self,value):

        newnode = self.Node(value)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        self.len += 1
        self.printlist()

    def insert_end(self,value):

        newnode = self.Node(value)
        if self.head == None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
        self.len += 1
        self.printlist()
    
    def delete_start(self):

        if self.head == None:
            print('List is empty, nothing to delete!')
            return False
        else:
            tobedeleted = self.head
            self.head = self.head.next
            element = tobedeleted.value
            del(tobedeleted)
            self.len -= 1
            self.printlist()
            return element

    def delete(self,value):

        flag = False

        if self.head == None:
            print('List is empty, nothing to delete')
            return False

        else:
            temp = self.head
            if self.head.value == value:
                self.head = self.head.next
                flag = True
                element = temp.value
                self.len -= 1
                del(temp)
            else:
                while temp.next!=None:
                    if temp.next.value == value:
                        tobedeleted = temp.next
                        temp.next = temp.next.next
                        element = tobedeleted.value
                        self.len -= 1
                        del(tobedeleted)
                        flag = True
                        break
                    else:
                        temp = temp.next

            self.printlist()
        if flag != True:
            print('Element was not found. Nothing to delete')
            return None
        else:
            return element


    def reverse(self):

        if self.head == None:
            print('List is empty. Nothing to reverse!')
        else:
            prev = None
            curr = self.head
            next = None
            while curr!=None:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            self.head = prev
            self.printlist()

    def printlist(self):

        if self.head == None:
            print("List is empty, nothing to print")
        else:
            temp = self.head
            while temp.next != None:
                print('{} -> ' .format(temp.value),end='')
                temp = temp.next
            
            print('{} -> ' .format(temp.value))

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_start(5)
    print(len(ll))
    ll.insert_start(4)
    print(len(ll))
    ll.insert_end(6)
    print(len(ll))
    ll.insert_end(7)
    print(len(ll))
    ll.insert_end(8)
    print(len(ll))
    ll.insert_start(3)
    print(len(ll))
    ll.insert_start(2)
    print(len(ll))
    ll.insert_start(1)
    print(len(ll))
    ll.delete_start()
    print(len(ll))
    ll.delete_start()
    print(len(ll))
    ll.delete_start()
    print(len(ll))
    ll.delete(8)
    print(len(ll))
    ll.delete(7)
    print(len(ll))
    ll.delete(6)
    print(len(ll))
    ll.delete(5)
    print(len(ll))
    ll.delete(3)
    print(len(ll))
    ll.delete(4)
    print(len(ll))
    ll.delete(3)
    print(len(ll))
    ll.delete_start()
    print(len(ll))
    ll.delete_start()
    print(len(ll))
            