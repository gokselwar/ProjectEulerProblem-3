print("Project Euler-Problem 3")
print("En buyuk asal böleni bulma")
sayi=int(input("Asal bölenini bulmak istediginiz sayiyi giriniz:"))

tam_bölenler=list()
asal_bölenler=list()

for i in range(2,sayi):
    if sayi%i==0:
        tam_bölenler.append(i)
        
"""Tam bölenler bulundu. şimdi sıra bu bölenlerden asal olanları ayırmakta"""

for item in tam_bölenler:
    kontrol = True
    for i in range(2,item-1,1):
        if item % i == 0:
            kontrol = False

    if kontrol == True:
            asal_bölenler.append(item)
print(asal_bölenler)