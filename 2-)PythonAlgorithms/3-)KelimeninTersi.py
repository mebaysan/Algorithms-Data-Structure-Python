"""
Kelimenin Tersi

*Örnek:
    * input  = 'Baysan'
    * output = 'nasyaB'
"""

def kelime_terse(kelime):
    yeni_kelime = kelime[::-1] # baştan sona -1 ile git, yani en sondan başa
    #[1:12:3] -> 1. indexten başla, 12. indexe kadar 3'er 3'er atlayark git
    # str[start:stop:step]
    print(f'{kelime} tersi -> {yeni_kelime}')

kelime_terse('Baysan')