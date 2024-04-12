class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add a new item to the queue, that is added at the rear of the queue"""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue"""
        if not self.is_empty():  # if the queue is not empty
            return self.queue.pop(0)  # remove the first element from the queue, i.e. fro front of the queue
        else:
            print("Queue is empty, cannot remove any item.")

    def is_empty(self):
        return len(self.queue) == 0

    @property
    def size(self):
        return len(self.queue)

    @property
    def front(self):
        if not self.is_empty():  # if the queue is not empty
            return self.queue[0]
        else:
            print("Queue is empty.")

    @property
    def rear(self):
        if not self.is_empty():  # if the queue is not empty
            return self.queue[-1]
        else:
            print("Queue is empty.")

    def display(self):
        return " -> ".join(map(str, self.queue))


if __name__ == "__main__":
    q = Queue()
    q.enqueue(12)
    q.enqueue(71)
    q.enqueue(45)

    print("Queue: ", q.display())

    print("Queue size:", q.size)
    print("Front of the queue:", q.front)
    print("Back of the queue:", q.rear)

    item = q.dequeue()
    print("Dequeued element:", item)
    print("Queue after dequeue: ", q.display())

    print("Queue size after dequeue:", q.size)
