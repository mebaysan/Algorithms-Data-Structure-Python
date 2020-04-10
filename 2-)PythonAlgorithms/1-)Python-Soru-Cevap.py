"""
1-) Deep Copy ve Shallow Copy arasındaki farklar?
* Deep Copy: orjinal objeyi başka yeni bir objeye kopyalar ama orjinal obje
    değiştirilirse yeni obje değiştirilmez
* Shallow Copy: orjinal objeyi yeni bir objeye kopyalar fakat orjinal obje değişirse yeni obje de değişir
"""
import copy
eski_liste = [[1, 1, 1], [2, 2, 2]]
yeni_liste = copy.deepcopy(eski_liste)  # deep copy
print(f"Deep Copy\tEski liste: {eski_liste}\tYeni liste: {yeni_liste}")
shallow_liste = copy.copy(eski_liste)  # shallow copy
eski_liste[0][1] = 11
print(f"Shallow Copy\tEski liste: {eski_liste}\tYeni liste: {shallow_liste}")


"""
2-) Tuple ve List arasındaki fark?
* Liste değişkendir
* Tuple değişmez
"""

"""
3-) Python'da Memory yönetimi nasıldır
* Python özel bir heap space'e sahiptir. Bu nedenle bizim erişimimiz yoktur
* Ama core API ile bazı özelliklerine erişim sağlayabiliriz

4-) help() ve dir() fonksiyonları arasındaki fark nedir
* help() fonksiyonu dökümanı string olarak sergiler
* dir() fonksiyonu istenilen objenin tüm özelliklerini metotlarını sergiler
ex: help(copy)
ex: dir(copy)

5-) Monkey Patching Nedir?
* Kod run-time'da iken bir class'ı yada modülü değiştirmeye yarar
* Genelde bug ayıklamak için kullanılır
"""

"""
6-) *args ve **kwargs kavramları nelerdir?
* Bazı durumlarda fonksiyonlar kaç adet parametre alacağını bilemeyiz. Bu durumlarda *args kullanırız
* Sözlük gibi kullanmak istersek **kwargs kullanırız
"""


def deneme(*args):
    for each in args:
        print(each)


deneme(1, 2, 3, 4, 5)


def return_django(**kwargs):
    for each in kwargs:
        print(f"{each} değeri -> {kwargs[each]}")


context = {
    'articles': 'Articleler',
    'user': 'request.user'
}
return_django(context=context, isim='baysan')

"""
7-) Negative index nedir?
* normalde index 0'dan saymaya başlar, negative index ise tersten saymaya başlar
"""
liste = [1,2,3,4,5]
print(f"positive index -> {liste[0]}")
print(f"negative index -> {liste[-1]}")

"""
8-) Listeyi nasıl random yaparsın?
"""
from random import shuffle
mylist = [0,1,2,3,4,5,6,7,8,9]
shuffle(mylist) # listeyi random eder
print(mylist)

"""
9-) join ve split fonksiyonları ne işe yarar?
* join  -> stringlerde her karakterden sonra istenilen stringi ekler --> 'eklenen_str'.join('eklenecek_str')
* split -> stringleri verilen karaktere göre parçalar --> 'parcalanacak_str'.split('filtre_str')
"""
yeni = "sd".join("deneme")
print(yeni)
print(yeni.split('sd'))

"""
10-) Keywords Identifier olarak kullanılabilir mi?
* int bir keyword'dur ve identifier(tanımlayıcı) olarak kullanılamaz
"""

"""
11-) Leading ve Trailing Whitespace ne demek?
* Bir string var  -> degisken = ' BAYSAN '
* Bunun başında ve sonunda boşluklar var
* Başındaki boşluğa leading whitespace
* Sonundaki boşluğa trailing whitespace
"""
degisken = ' Baysan '
degisken.lstrip() # Leading(soldaki) boşlukları yok eder
degisken.rstrip() # Trailing(sağdaki) boşlukları yok eder
degisken.strip()  # Hem Leading hem de Trailing yok eder


"""
12-) Bir stringi büyük ve küçük harfe nasıl çevirirsin?
* degisken.lower()
* degisken.upper()
"""

"""
13-) Python'da pass-break-continue nasıl kullanılır?
* Bir fonksiyon tanımladık fakat henüz içini doldurmadıysak pass kullanırız
* Belirli bir koşul sağlanınca döngüyü kırmak(bitirmek) istersek break kullanırız
* Belirli bir koşul sağlanınca döngüyü devam ettirmek istersek continue kullanırız
"""
"""
14-) // % ** işaretleri ne anlama gelir?
* // -> operatör olarak geçer ve bölme işleminin integer kısmını döndürür
* %  -> operatör, bölme işleminin kalan kısmını döndürür
* ** -> operatör, üssü (power) anlamındadır
"""

"""
15-) Membership operatör nedir?
* 'an' in 'Baysan'
* 'na' not in 'Baysan'
"""

print('an' in 'Baysan') # içinde var mı
print('na' not in 'Baysan') # içinde yoksa true döndürür