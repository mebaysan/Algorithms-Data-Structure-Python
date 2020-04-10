"""
Her kelimenin baş harfini büyütmek
* input  -> 'kod yazmak çok zevkli'
* output -> 'Kod Yazmak Çok Zevkli'
"""


def bas_harf_buyut(_kelime):
    kelimeler = _kelime.split(' ')
    for i in range(0, len(kelimeler)):
        kelimeler[i] = kelimeler[i][0].upper() + kelimeler[i][1:]
    kelime = ' '.join(kelimeler)
    print(f'{_kelime}  ->\t{kelime}')

# _kelime.title() -> bu işlevi görür :)

bas_harf_buyut('kod yazmak çok zevkli')
