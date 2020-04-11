"""
Dynamic Array
* Boyutunu önceden belirlemek zorunda olmadığımız daha sonra eleman ekleyip çıkartabildiğimiz yapılar
* Growable and Resizable olarak tanımlanır
"""

import ctypes  # yeni array oluşturmak için kullanacağız


class DynamicArray(object):

    def __init__(self):  # initialize (constructor)
        self.n = 0  # eleman sayısı
        self.capacity = 1  # kapasite
        self.A = self.make_array(self.capacity)

    def __len__(self):
        # return eleman sayısı
        return self.n

    def __getitem__(self, k):
        # return index k'daki eleman
        if not 0 <= k < self.n:
            return IndexError(f'{k} index sınırları içerisinde değil')
        return self.A[k]

    def append(self, eleman):
        # eleman ekler array'e
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = eleman  # eleman ekle
        self.n += 1  # eleman sayısını bir ekler

    def _resize(self, new_cap):
        # array kapasitesi arttırılır
        yeni_array = self.make_array(new_cap)  # yeni arrayi yapar
        # eski array (A) içerisindeki değerleri yeni_array'e taşı
        for k in range(self.n):
            yeni_array[k] = self.A[k]
        self.A = yeni_array  # arrayi günceller
        self.capacity = new_cap  # kapasiteyi günceller

    def make_array(self, new_cap):
        # return yeni array
        return (new_cap*ctypes.py_object)()


dynamic_array = DynamicArray()  # instance oluşturduk

dynamic_array.append(1)  # element ekle (1)
print(dynamic_array[0])

dynamic_array.append(3)  # element ekle (1,3)
print(dynamic_array[0], dynamic_array[1])
