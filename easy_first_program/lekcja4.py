#PĘTLE

i = 0

while True:   # pętla wykonuje się dopuki warunek jest spełniony
    i += 1
    if i % 2 == 1:
        continue
    print(i)
    if i > 10:
        break  #Kończy pętle
print("Koniec")    
