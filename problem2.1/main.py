#Input
bilangan = int(input('Input : '))

#Looping mengecek apakah i adalah faktor bilangan
print('Output:')
for i in range(1,bilangan+1):
    if bilangan % i == 0:
#Cetak i jika merupakan faktor bilangan dari bilangan
        print(i)
