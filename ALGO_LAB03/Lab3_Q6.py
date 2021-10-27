#6. SORU
sayı=int(input("Decimal sayıyı girin:"))
i=0
top=0
while(True):
    if(sayı>=2):
        top=top+((sayı%2)*(10**i))
        sayı=sayı//2
        i+=1
    else:
        top=top+(sayı*(10**i))
        break
print(int(top))

