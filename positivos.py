#  Conte quantos números positivos foram digitados.
positivos = 0
numero = float(input('Digite um número: '))

while numero !=0:
    if numero > 0:
        positivos = positivos + 1
    numero = float(input("Digite o próximo número ou 0 para ver o resultado: "))

print(f"Você digitou {positivos} números positivos.")