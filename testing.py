class Queue:
    def __init__(self):
        self.list_queue = [] # queue is implemented here
    
    def enqueue(self,item):
        self.list_queue.append(item) # adding new data to the end of the queue

    def dequeue(self):
        return self.list_queue.pop(0)

    def size(self):
        return len(self.list_queue)

lst = ['poo', 'ste', 'sim', 'nic','luo', 'ibr', 'sie', 'zhe']
m = 3
print(lst)
def who_wins(m, players):
    q = Queue()
    
    q.list_queue = players

    while q.size() > 1:
        for _ in range(m):
            q.enqueue(q.dequeue())
        q.dequeue()
        print(q.list_queue)
    return q.list_queue

who_wins(m, lst)