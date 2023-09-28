#Input
bilangan = int(input('Input : '))

#Looping mengecek apakah i adalah faktor bilangan dari yang terbesar
print('Output:')
for i in range (bilangan+1,0,-1):
    if bilangan % i == 0:
#Cetak i jika merupakan faktor bilangan dari bilangan dari nilai terbesar
        print(i)
