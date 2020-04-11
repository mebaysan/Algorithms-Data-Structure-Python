"""
            STACKS
* Ekleme - Çıkarma işleminin her zaman aynı yerden yapıldığı yapılara stack (yığın) denir
* Ekleme- Çıkarma işlemi hep top kısmından yapılır
* Top'ın tersi olan kısma base denir
* Son giren ilk çıkar LIFO (Last in First out)
* Karakteristik özelliği Push ve Pop işlemleridir.
* Üç ana işlemi vardır:
* Push -> yığının en tepesine eleman ekler
* Pop  -> yığının en sonundan eleman çıkar ()
* Top  -> yığının en tepesindeki elemanı gösterir
"""


class Stack:
    def __init__(self):
        # initialize (constructor)
        self.items = []

    def is_empty(self):
        # boş mu değil mi kontrol
        return self.items == []  # boolean operasyon, boş ise true değilse false
    def push(self,item):
        # stack içine item ekler
        self.items.append(item)
    def pop(self):
        # stack içerisinden en sondaki elemanı çıkarır (ilk gireni)
        self.items.pop()
    def top(self):
        # stack içerisinden en üstteki (son giren) elemanı verir
        print(f'en tepedeki eleman yani son giren -> {self.items[len(self.items)-1]}')
    def size(self):
        # stack boyutunu verir
        print(f"stack içerisinde {len(self.items)} eleman var")

stack = Stack()

stack.push(1)
stack.push(2)
stack.top()
stack.push(3)
stack.push(4)
stack.top()
stack.pop() # 4 çıkar çünkü en son girid ve en üstte
stack.top() # 3 döner çünkü 4 gitti 4'ten bir önce giren 3 idi

