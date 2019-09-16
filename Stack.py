from LinkedList import LinkedList

class Stack:

    def __init__(self):
        print('Initialized Stack Class which is implemented using a LinkedList')
        self.ll = LinkedList()
        self.top = None

    def __len__(self):
        return len(self.ll)

    def push(self,value):
        self.ll.insert_start(value)
        self.top = self.ll.head.value

    def pop(self):
        if self.top == None:
            print('Stack is empty, Nothing to print!')
            return False
        else:
            element = self.ll.delete_start()
            if self.ll.head == None:
                self.top = None
            else:
                self.top = self.ll.head.value
            return element
    
    def peek(self):
        if self.top == None:
            print('Stack is Empty')
        else:
            print('Top Element of Stack {}' .format(self.top.value))

if __name__ == '__main__':
    s = Stack()
    print(len(s))
    s.push(5)
    print(len(s))
    s.push(1)
    print(len(s))
    s.push(2)
    print(len(s))
    s.push(3)
    print(len(s))
    s.push(4)
    print(len(s))
    s.pop()
    print(len(s))
    s.pop()
    print(len(s))
    s.pop()
    print(len(s))
    s.pop()
    print(len(s))
    s.pop()
    print(len(s))
    s.pop()
    print(len(s))

