price: int = -1
amountPay: int = 0
listPrice = []
total: int = 0
numberTenEuros: int = 0
numberFiveEuros: int = 0
numberOneEuros: int = 0

while price != 0:
    price = int(input("Donnez un prix : "))
    listPrice.append(price)

for amount in listPrice:
    total += amount

print("Vous devez payer "+str(total)+" €")
amountPay = int(input("Combien donnez-vous : "))
totalTemp = amountPay-total

tempTenEuros = totalTemp//10
print(str(tempTenEuros))
numberTenEuros += tempTenEuros
totalTemp -= (numberTenEuros*10)

tempFiveEuros = totalTemp//5
numberFiveEuros += tempFiveEuros
totalTemp -= (numberFiveEuros*5)

tempOneEuros = totalTemp
numberOneEuros += tempOneEuros
totalTemp -= numberOneEuros

print("Le marchand vous a rendu : " + str(numberTenEuros) + " billets de 10 €, " + str(
    numberFiveEuros) + " billets de 5€, " + str(numberOneEuros) + " pièces de 1 €")
