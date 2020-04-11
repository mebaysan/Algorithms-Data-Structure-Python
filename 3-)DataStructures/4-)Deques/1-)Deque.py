"""
            Deque
* double endend queue olarak bilinir
* iki tane 'end', 'front' ve 'rear'a sahiptir
"""


class Deque:
    def __init__(self):
        # initialize
        self.items = []

    def is_empty(self):
        # boş mu değil mi
        return self.items == []

    def add_front(self, item):
        # Deque'ya front kısmından item ekler
        self.items.append(item)  # en sona ekler

    def add_rear(self, item):
        # deque'ya rear'dan item ekler
        self.items.insert(0, item)  # en başa ekler

    def remove_front(self):
        # deque front'tan item çıkartır (en sondan)
        c = self.items.pop()
        print(f'remove front ile -> {c}  çıktı')

    def remove_rear(self):
        # deque rear'dan item çıkartır (en baştan)
        c = self.items.pop(0)
        print(f'remove rear ile -> {c}  çıktı')

    def size(self):
        # deque size döner
        print(f'{len(self.items)} item var')


deque = Deque()
deque.add_front(1)
deque.add_rear('Ankara')
print(deque.items)
deque.remove_front()
print(deque.items)