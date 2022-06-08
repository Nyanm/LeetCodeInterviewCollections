import threading


class BoundedBlockingQueue(object):
    def __init__(self, capacity):
        self._capacity = capacity
        self._enqueuing = threading.Semaphore(self._capacity)
        self._dequeuing = threading.Semaphore(0)
        self._queue = []

    def enqueue(self, element):
        self._enqueuing.acquire()
        self._queue.append(element)
        self._dequeuing.release()

    def dequeue(self):
        self._dequeuing.acquire()
        res = self._queue.pop(0)
        self._enqueuing.release()
        return res

    def size(self):
        return len(self._queue)


if __name__ == '__main__':
    test = BoundedBlockingQueue(5)
    test.enqueue(1)
    test.enqueue(1)
    test.enqueue(1)
    test.enqueue(1)
    test.enqueue(1)
    test.enqueue(1)

