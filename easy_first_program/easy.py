
name = "rafal"
age = 40
friends = ["dawid", "kamil", "partyk"]
family = {"dad": "Cesiek", "mum": "Anna", "sister": "Partycja", "brother": "Kacper"}

for family_memeber, name_of_memeber in family.items():
    print(f"My {family_memeber} name is {name_of_memeber}!!!! fuck yeah!")

x=0
while x<3:
    print(friends[x])
    x+=1

sentence = f"my name is {name} and I am very old: {age} :( !"
print(sentence)

