# Tabuada de um número
numero = int (input('Qual tabuada você deseja calcular? '))
print (f'Vamos calcular a tabuada do {numero}!')

for i in range (1,11):
    resultado = numero * i
    print (f'{numero} x {i} = {resultado}')