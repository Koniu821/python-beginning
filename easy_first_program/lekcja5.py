from random import randint #losuje randomowe liczby

#for  i in range(100): #pętla będzie tłumaczona  winnym odcinku 
   # print(randint(1,10))

los =randint(1,10)
odp = -1
i = 0
print ("Zgadnij liczbe z przedziału od 1 - 10")

while odp != los:
    i += 1
    odp = int(input("Podaj liczbę: ")) #input pobiera informacje od użytkownika 
    if  odp > los:
        print("Liczba jest mniejsza od Twojej")
    elif odp < los: 
        print("Liczba jest większa od Twojej")
print("Wygrałeś! Odgadłeś za ",i,"razem.")   