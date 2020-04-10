"""
Bazı problemler ünlüdür. Mesela bir listedeki sayıları küçükten büyüğe dizmeye çalışmak.
Problem ünlü olduğu için de algoritması da ünlüdür ve isimleri vardır.
 * Problem   -> Sayıları küçükten büyüğe dizmek
 * Algoritma -> Sorting

"""

# Soru: 1'den n'e kadar olan sayıları dön, karelerini al topla ve toplamı return et

def toplam_kare(n):
    toplam = 0
    for x in range(1, n+1):
        toplam += x**2
    return toplam


def toplam_kare2(n):
    return (n*(n+1)*(2*n+1))/6

"""
2 algoritma da aynı sonucu veriyor, o zaman hangisi daha iyi?
Büyük ihtimalle toplam_kare2 daha hızlı çalışacak. Fakat herkesde farklı sonuçlar verecek.
O yüzden bu 2 algoritmayı zamana göre karşılaştırmak yanlış olur.

"""