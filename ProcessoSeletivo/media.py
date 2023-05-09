


lista = [23.6, 37.9, 25.1,19.0, 29.8]

menor = lista[0]
maior = lista[0]
soma = 0

for num in lista:
    if num < menor:
        menor = num
    if num > maior:
        maior = num
    soma += num

media = soma/len(lista)

print("a) A menor temperatura é: ",menor)
print("b) A maior temperatura é: ", maior)
print("c) A media de temperaturas é: ",media)

