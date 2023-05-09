num1 = int(input("Digite o primeiro numero"))


num2 = int(input("Digite o segundo numero"))

while num2 < num1:
    print("numero dois menor que o primeiro")
    num2 = int(input("Digite o segundo numero"))

soma = num1 + num2
print(f"soma dos numeros {num1} e {num2} é: {soma}" )
