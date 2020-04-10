"""
İki algoritmayı karşılaştırırken runtime'a göre karşılaştırmamalıyız. CPU sebebiyle farklılık gösterebilir
Big-O kavramı bir fonksiyonun büyümesini ifade eder
Runtime nasıl büyür onu karşılaştırmak istiyoruz

"""

"""
                        Big O | Omega | Theta
Big O: yazdığımız kodun en kötü durumda nasıl çalıştığını test etmek için
Omega: yazdığımız kodun en iyi durumda nasıl çalıştığını test etmek için
Theta: mid case senaryo (ne iyi ne kötü senaryolar)

"""

#                                      Big-O Örnekleri
"""
O(1) Constant
    * Constant çünkü input size'dan bağımsız
    * input size çok büyük olsaydı sonuç değişmeyecekti
"""


def constant_big_o(liste):  # algoritma input boyutundan bağımsız olduğu için 'Constant'
    print(liste[0])


constant_big_o([-5, 1, 3, 2, 3, 4, 56, 7, 123, 213])


"""
O(n) Linear
    * Bu fonksiyon linear zamanda çalışır. Yani algoritma içerisindeki operasyon sayısı input size ile doğru orantılı
    * Mesela eğer input size 5 olsaydı, print fonksiyonu 5 kez çağırılacaktı, 2 olsaydı 2 kez
"""


def linear_big_o(liste):
    for deger in liste:
        print(deger)


linear_big_o([1, 2, 3, 4, 5])


"""
O(n^3) Cubic
    * Nested loop'lardan oluşan 3 tane for döngüsü kullanacağız
    * Yani n^3 işlem yapacağız
    * İnput size 3 için, 27 tane işlem yapacağız
"""


def cubic_big_o(liste):
    for item_1 in liste:
        for item_2 in liste:
            for item_3 in liste:
                print(item_1, item_2, item_3)
cubic_big_o([1,2,3])