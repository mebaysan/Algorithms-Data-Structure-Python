"""
                                    Singly Linked List
* Singly Linked List, Linked List'lerin en basit formudur
* Node'ların toplandığı linear bir yapıdır
* Her bir node hem veri depolar hem de diğer node'a ulaşmak için bir adres (pointer) depolar (sahiptir)
* Head -> linked list'teki ilk node
* Tail -> linked list'teki son node
* Linked List içerisinde bir node'dan diğer node'a dolaşmaya 'traversing' denir
* predetermined fixed bir size'a sahiptir. Yani önceden boyut belirlenmiyor
* Linked List başına bir eleman eklemek istersek:
    -) Yeni node oluştur
    -) Node içerisindeki veriyi belirle
    -) Node'un adresini (pointer) önceki head olarak belirle
    -) Oluşturulan yeni node'u head olarak belirle
* Linked List sonuna bir eleman eklemek istersek:
    -) Yeni node oluştur
    -) Next referansı None olarak ayarla
    -) Tail'in next referansını bu yeni nod olarak ayarla
    -) Yeni eklenen node'u tail olarak ayarla
* Linked List baştan eleman çıkarmak istersek
    -) Çıkaracağımız node'dan sonraki node'u head reference yaparız. Yani head pointerı çıkarılan node'un adresinden sonraki adres yap
* Linked List sondan eleman çıkarmak istersek
    -) Singly Linked List'in son elemanını çıkarmak istersek listemizi doubly linked list yapmamız lazım!
"""


class Node(object):
    def __init__(self, value):
        # node oluştur: değer ve next pointer'a sahip olmalı
        self.value = value
        self.next_node = None

    def set_next_node(self, node):
        # next node'u set eder
        self.next_node = node

    def get_next_node(self):
        # bir sonraki node'u verir
        return self.next_node

    def get_node_value(self):
        # node içerisindeki değeri verir
        return self.value

istanbul = Node(value='34')
ankara = Node(value='06')
bolu = Node(value='14')

ankara.set_next_node(bolu) # ankara => bolu
print(ankara.get_next_node().get_node_value())
bolu.set_next_node(istanbul) # bolu => istanbul
print(bolu.get_next_node().get_node_value())
print(ankara.get_next_node().get_next_node().get_node_value()) # ankara => bolu => istanbul