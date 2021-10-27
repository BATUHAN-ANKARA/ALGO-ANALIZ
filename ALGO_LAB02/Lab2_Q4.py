## 4. SORU

def Swap(dizi,loc1,loc2):
    temp = dizi[loc1]
    dizi[loc1] = dizi [loc2]
    dizi[loc2] = temp
    print(dizi)

unsorted = [13,65,48,0,3,7,5,13,16,44,96,34,61,73,37]
print("Dizi 15 elemandan oluşmaktadır bu nedenle 0-14 indis numaralarına göre yerlerini değiştirmek istediğiniz indis numaralarını girin:")
indis1 = int(input("İndis 1:"))
indis2 = int(input("İndis 2:"))

Swap(unsorted,indis1,indis2)


