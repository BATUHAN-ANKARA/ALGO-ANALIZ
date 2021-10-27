#8.SORU
x=int(input("X değerini giriniz:"))
n=int(input("n değerini giriniz:"))
t=1
f=1
i=1

while(True):

    if(n+1==i):
        print(t)
        break
    else:
        f=f*i
        t=t+(x**i)//f
        i+=1


