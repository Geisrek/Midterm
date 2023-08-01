class Queue:
    def __init__(self) :
        self.queue=[]
    def enQueue(self,item):
        self.queue.append(item)
    def deQueue(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)
    def peekFirst(self):
        return self.queue[0]
    def peekLast(self):
        return self.queue[len(self.queue)-1]
    def sort_key(self,item):
        return int(item.getPriority())
    def bigerId(self):
        _sort_key=lambda item:int(item.getTikId()[4:])
        self.queue.sort(key=_sort_key)
        return self.queue[len(self.queue)-1]
    def Sorting(self):
      self.queue.sort(key=self.sort_key)
    def toString(self):
        for x in self.queue:
            print(x.toString())
    def size(self):
        return len(self.queue)
