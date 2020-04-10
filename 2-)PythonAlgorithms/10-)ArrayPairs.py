"""
Array Çiftleri
* input  -> [5,6,6,5,3,3]
  output -> '3,3'

* input  -> [7,8,8,7,9,1,1,9]
  output -> 'ok'
"""


def array_pair(array):
    # stringe çevir
    # reverse pair olmayanları depola
    # eğer depo boş ise return 'ok'
    # eğer depo boş değil ise return depo
    new = ''
    for k in range(len(array)):
        new += str(array[k]) + ' ' # '5 6'
        if k % 2 == 1:
            new += ',' # 5 6 , 6 5 , 3 3
    new = new.split(' ,') # ['5 6', '6 5', '3 3', '']
    depo = []
    for i in new:
        if i[::-1] not in new: # içinde mi değil mi kontrol et
            for l in i.split(): # içinde değilse depo listesine ekle
                depo.append(l)
        elif i == i[::-1] and new.count(i)<2:
              for l in i.split():
                depo.append(l)
    if depo == []:
        return 'ok'
    return ','.join(depo)


print(array_pair([5,6,6,5,3,3]))
print(array_pair([7,8,8,7,9,1,1,9]))
