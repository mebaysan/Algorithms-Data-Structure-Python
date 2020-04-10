

def rotate_array(array):
    # arrayin ilk elemanını bul. bu değer eski başlangıç değerimiz
    # output arrayin ilk elemanını bul
    # bizim arrayimizin ilk elemanını eski başlangıç indexi kabul et
    # while döngüsü ve counter ata
    # return
    eski_baslangic = array[0]
    yeni_baslangic = [str(array[eski_baslangic])]
    count = eski_baslangic + 1
    length = len(array)
    while count%length != eski_baslangic:
        yeni_baslangic.append(str(array[count%length]))
        count+=1
    return ''.join(yeni_baslangic)

print(rotate_array([4,5,6,7,8,9,10]))