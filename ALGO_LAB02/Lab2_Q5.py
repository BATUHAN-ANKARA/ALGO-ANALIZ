## SORU 5

unsorted = [13,65,48,0,3,7,5,13,16,44,96,34,61,73,37]

def Swap(dizi,loc1,loc2):
    temp = dizi[loc1]
    dizi[loc1] = dizi [loc2]
    dizi[loc2] = temp

def Bubble(dizi):
    uzunluk=len(dizi)
    

    for i in range(uzunluk - 1,0,-1):
        j = i - 1
        if(dizi[i]<dizi[j]):
            Swap(dizi,i,j)
            Bubble(dizi)



print(unsorted)
Bubble(unsorted)
print(unsorted)
    
