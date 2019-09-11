from LinkedList import LinkedList

class Queue:

    def __init__(self):
        print('Initialized Queue Class. This is implemented using a linkedlist!')
        self.queue = LinkedList()

    def __len__(self):
        return len(self.queue)

    def enqueue(self,value):
        self.queue.insert_end(value)

    def dequeue(self):
        if self.queue.head == None:
            print('Queue is empty, Nothing to print!')
            return False
        else:
            element = self.queue.delete_start()
            return element
    
if __name__ == '__main__':
    q = Queue()

        
