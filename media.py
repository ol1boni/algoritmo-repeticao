# Leia 5 números e calcule a média
soma = 0 
for i in range (1,6):
    numero = float(input(f'Digite o {i}º número: '))
    soma = soma + numero
    media = soma / 5
print(f"A soma dos números é: {soma}")
print(f"A média dos 5 números é: {media}")