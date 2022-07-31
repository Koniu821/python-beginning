#lista = Tablica 
zmienna = 1
zmienna2 = "Abc"

lista = [1, 2, "c", "d","e"]
print(lista)
print(lista[0]) #odwłoanie się do wybranego elementu listy
lista[2] = 3 #modyfikowanie danych w tablicy
print(lista)
#tekst = "Hello World"
#print(tekst[1])
print(lista + ["f", "g"]) #dodawanie do listy tylko i włacznie na potrzeby print
print(lista * 3) #pomnożenie listy razy 3
print("Ilość elementów:", len(lista))#liczy liczbę elementów listy
lista.append("f") #dodawanie elementu do listy , zawsze na końcu
print(lista)
lista.append(["g", "h"]) #dodawanie listy do listy
print(lista)
print(lista[6][1]) #pobieranie elementów z drugiej listy ;
lista.insert(3,3) #dodawanie elementów we wskazane mmiejsce w liście
print(lista)
print ("Ilość: ", lista.count(3))#liczenie elementów takich samych w liście
print("Index: ", lista.index("f")) #zwracanie indexu wybranego elementu listy
lista.remove("f") # usuwanie elementu listy
print(lista)

lista2 =[1, 20, 35, -5, 0]
print("min: ", min(lista2))# pokazuje minimalną wartość z listy
print("max: ", max(lista2)) #pokazuje maxymalną wartość z listy
lista2.sort()# sortuje listę od najmniejszego do największego elementu 
print(lista2)
lista2.reverse()#odwracanie elementów listy
print(lista2)
lista2.clear() #czyści wszystkie elemety listy 
print(lista2)