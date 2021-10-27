#7.SORU
# sayi =int(input("1'den 100'e kadar olan asal sayiları hangi sayiya kadar görmek istersiniz:"))
sayi=1
adet = 0
while(sayi<100):
    if(sayi == 2 or sayi == 3 or sayi== 5 or sayi == 7):
        adet+=1
        sayi+=1
    elif(sayi%2==0 or sayi%3==0 or sayi%5==0 or sayi%7==0):
        sayi+=1
    elif(sayi == 1):
        sayi+=1
    else:
        sayi+=1
        adet+=1
print(int(adet))


# Bir diğer yöntem
# sayi=1
# adet = 0
# while(sayi<100):
#     if(sayi == 2 or sayi == 3 or sayi== 5 or sayi == 7):
#         adet+=1
#         sayi+=1
#     elif(sayi%2==0):
#         sayi+=1
#     elif(sayi%3==0):
#         sayi+=1
#     elif(sayi%5==0):
#         sayi+=1
#     elif(sayi%7==0):
#         sayi+=1
#     elif(sayi == 1):
#         sayi+=1
#     else:
#         sayi+=1
#         adet+=1
# print(int(adet))