

lista = []
repetidos = []


for i in range(50):
    num = int(input("Digite um numero: "))
    lista.append(num)

for i in range(len(lista)):
    numCompara = lista[i]
    
    for j  in range(i + 1,len(lista)):
        if numCompara == lista[j]:
            if i not in repetidos:
                repetidos.append(i)
                repetidos.append(j)

if len(repetidos)> 0:
    print("Numeros repetidos nas seguintes posições:")

    for posicao in repetidos:
        print(f"Posicao: {posicao+1}, Numero: {lista[posicao]}")
else:
    print("Não tem nenhum repetido")