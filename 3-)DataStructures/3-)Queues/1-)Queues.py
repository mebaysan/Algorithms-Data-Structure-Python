"""
                Queues
* rear kısmından (en üstten) veri eklenir (yatay düşünürsek soldan girer)
* front kısmından (en alt) veri çıkar (yatay düşünürsek sağdan çıkar)
* ilk giren ilk çıkar FIFO (first in first out)
* yemekhane sırası gibi düşünebiliriz
* Enqueue (veri eklemek) Dequeue(veri çıkartmak)
"""


class Queue:
    def __init__(self):
        # initialize (constructor)
        self.items = []
    def is_empty(self):
        # boş mu değil mi
        return self.items == []
    def enqueue(self,item):
        # queue'e item ekler
        self.items.insert(0,item) # hep başa ekler
    def dequeue(self):
        # queue'den item çıkartır
        cikan = self.items.pop()
        print(f'{cikan} elemanı çıktı')
    def size(self):
        # queue size döner
        print(f'{len(self.items)} item var')


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.size()
queue.dequeue() # 1 çıkar çünkü ilk girdi
