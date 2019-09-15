from Stack import Stack

class Qwith2Stacks:

    def __init__(self):
        #enqueue stack
        self.s1 = Stack()
        #dequeue stack
        self.s2 = Stack()
        self.length = 0

    def __len__(self):
        return self.length

    def enqueue(self,value):
        self.s1.push(value)
        self.length += 1
        return True

    def dequeue(self):
        while(len(self.s1)>0):
            self.s2.push(self.s1.pop())
        if len(self.s2) > 0:
            return self.s2.pop()
        else:
            print('Queue is Empty, Nothing to Dequeue')
            return False


if __name__ == '__main__':
    q = Qwith2Stacks()
    q.enqueue(5)
    q.enqueue(4)
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    print('dequeued {}' .format(q.dequeue()))
    print('dequeued {}' .format(q.dequeue()))
    print('dequeued {}' .format(q.dequeue()))
    print('dequeued {}' .format(q.dequeue()))
    print('dequeued {}' .format(q.dequeue()))
    print('dequeued {}' .format(q.dequeue()))






