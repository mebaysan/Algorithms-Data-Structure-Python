"""
Saat Çevirme
* input  -> 129
* output -> 2 saat 9 dakika
"""


def saat_cevir(_saat):
    saat = _saat//60
    dakika = _saat % 60
    print(f'{saat} saat {dakika} dakika')


saat_cevir(129)
