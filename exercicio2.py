num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2

if soma > 20 and soma != 0:  # Verifica se a soma é maior que 20 e diferente de 0
    resultado = soma + 8
else:
    resultado = soma - 5


print("O resultado final é:", resultado)
