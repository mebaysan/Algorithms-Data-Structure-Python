"""
Kelime Karıştırma
* input  -> 'ankara' == 'kaarna'
  output -> true

* input  -> 'ankara' == 'zarks'
  output -> false

"""


def kelime_karistirma(str1, str2):
    # str2'deki harflere erişim sağla
    for i in str2:
        if i not in str1:  # harf str1 içinde var mı
            return False
    return True


print(kelime_karistirma('ankara', 'kaarna'))
print(kelime_karistirma('ankara', 'zarks'))
