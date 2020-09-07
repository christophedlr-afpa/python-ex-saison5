horseStarting: int = 0
horsePlayed: int = 0
x: int = 1
y: int = 1
n: int = 1
p: int = 1
result: int = 1

horseStarting = int(input("Nombre de chevaux partant :"))
print(str(horseStarting))
horsePlayed = int(input("Nombre de chevaux joués :"))

for i in range(1, horseStarting+1):
    n = n * i

for i in range(1, (horseStarting-horsePlayed)+1):
    result = result * i

x = n/result

for i in range(1, horsePlayed + 1):
    p = p * i

y = n/(p*result)

print("Dans l’ordre : une chance sur "+str(x)+" de gagner")
print("Dans le désordre : une chance sur "+str(y)+" de gagner")
