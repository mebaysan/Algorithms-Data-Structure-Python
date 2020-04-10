"""
Sıklık Bulma
* input  -> 'kkwcccddee'
* output -> '2k1w3c2d2e'
"""


def tekrar_bulma(string):
    i = 0
    final_string = ''
    while i < len(string):
        c = string[i]
        j = i+1
        compressed = [1, c]
        while j < len(string):
            if string[j] == c:
                compressed[0] += 1
            else:
                break
            j += 1
        final_string += ''.join(map(str, compressed))
        i = j
    print(final_string)


tekrar_bulma('kkwcccddee')
