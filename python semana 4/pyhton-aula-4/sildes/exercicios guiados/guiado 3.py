# Exercício 3: ordenar a lista
texto = input("Números separados por espaço: ")
numeros = [int(x) for x in texto.split()]

numeros.sort()  # ordem crescente
print("Crescente:", numeros)

# Copia ordenada ao contrário
print("Decrescente:", sorted(numeros, reverse=True))
