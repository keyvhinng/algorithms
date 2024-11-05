from queue import Queue

class MovingAverage:

    def __init__(self, size: int):
        self.sum = 0
        self.size = 0
        self.capacity = size
        self.q = Queue()
        

    def next(self, val: int) -> float:
        self.sum += val
        self.size += 1
        self.q.put(val)
        if self.size > self.capacity:
            num = self.q.get()
            self.sum -= num
            self.size -= 1
        return self.sum / self.size 
        
