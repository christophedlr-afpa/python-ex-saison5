import random

randomnumber: int = 0
number: int = -1
numberTesting: int = 0

randomnumber = random.randint(1, 100)

while number != randomnumber:
    numberTesting += 1
    print("Choisissez un nombre en 1 et 100 ")
    number = int(input())

    if number > randomnumber:
        print("Plus petit !")
    elif number < randomnumber:
        print("Plus grand !")

print("Vous avez trouvé, bravo !")
print("Il vous aura fallut "+str(numberTesting)+" essais pour y arriver.")
