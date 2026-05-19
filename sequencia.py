# Sequência Fibonacci
numero = int(input("Quantos termos? "))
a, b = 0, 1
for i in range(numero):
    print(a, end=" ")
    a, b = b, a + b