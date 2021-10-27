## 1. SORU 

def Power(number, param):
    answer = 1
    if param >= 0 :
        for i in range(param):
            answer = answer * number
        print(answer)

    else :
        param = param * -1
        for i in range(param):
            answer = answer * number
        print(1/answer)

print("İlk önce sayınızı girin, sonra kuvvet değerini girin.")
number = int(input("Sayı:"))
param = int(input("Kuvvet:"))
Power(number,param)

