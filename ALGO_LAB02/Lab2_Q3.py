## 3. SORU
unsorted = [13,65,48,0,3,7,5,13,16,44,96,34,61,73,37]

def change(dizi):
    x = len(dizi)
    temp = dizi[0]
    dizi[0] = dizi [x - 1]
    dizi[x - 1] = temp
    print(dizi)
change(unsorted)
