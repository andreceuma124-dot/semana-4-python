# Exercício 2: filtrar números pares
texto = input("Números separados por espaço: ")
numeros = [int(x) for x in texto.split()]
# Filtra os divisíveis por 2
pares = [n for n in numeros if n % 2 == 0]
print("Digitados:", numeros)
print("Pares:", pares)