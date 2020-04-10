"""
Kayıp Basamak Bulma

* input  -> '10 - x = 4'
* output -> '6' 
"""


def kayip_basamak(string):
    # x bul replace et (0-9)
    # = bul
    # ='den önceki ve sonraki kısmı karşılaştır ( eval() methodu kullan )
    # eval('55') == eval('50+5')  -> eval bizim için str içerisindeki matematiksel işlemleri yapar
    # return
    for i in range(10): # 0,1,2,3,....9
        x = string.replace('x',str(i))
        c = string.index('=')
        if eval(x[:c]) == eval(x[c+1:]): # eşittire kadar olan kısım ile eşittirden sonraki kısmı karşılaştır
            # eval('10 - x') == eval('4')
            return str(i)
    

print(kayip_basamak('10 - x = 4'))
print(kayip_basamak('1x * 11 = 121'))
print(kayip_basamak('1x0 / 3 = 50'))