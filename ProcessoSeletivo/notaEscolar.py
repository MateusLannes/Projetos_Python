
def calculaNota(lista):
    notas = []
    for i in lista:
        if (i >= 38):
            num = i
            while ((num % 5) != 0):
                num += 1
            if (num - i < 3):
                notas.append(num)
            else:
                notas.append(i)
        else:
            notas.append(i)
    return notas

       
lista = [73, 67,38 ,33]
notas = calculaNota(lista)
print(notas)


