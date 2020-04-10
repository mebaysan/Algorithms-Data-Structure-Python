"""
* Insignificant constant
* Linear Big-O input size ile doğru orantılı
* İlk örnekte Big-O = O(n)
* İkinci örnekte Big-O = O(2n)
* 2 burada Insignificant Constant olarak geçer ve bu sabit sayıyı ihmal edebiliriz.
* Yani her 2 durum içinde Big-O = O(n)
"""

def linear_big_o(liste):
    for deger in liste:
        print(deger)

linear_big_o([1,3]) # O(n)


def linear_big_o_2(liste):
    for deger in liste:
        print(deger)
    for deger in liste:
        print(deger)

linear_big_o_2([1,3]) # O(2n)