# Exercício 1: criar lista de números
numeros = []  # lista vazia
qtd = int(input("Quantos números? "))

for i in range(qtd):
    n = int(input("Digite um número: "))
    numeros.append(n)  # insere no fim

print("Lista:", numeros)
print("Tamanho:", len(numeros))