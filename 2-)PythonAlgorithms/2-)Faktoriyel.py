"""
Faktoriyel Algoritma
* Faktoriyel => 4! => 4.3.2.1 => 24
* input = 4
* output = 24
"""

def faktoriyel(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    print(f'{n}! = {f}')

faktoriyel(4)