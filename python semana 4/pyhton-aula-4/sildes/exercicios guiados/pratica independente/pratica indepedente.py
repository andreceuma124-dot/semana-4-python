
# Exercício Integrador - Python

# 1. Criar lista de nomes
nomes = []
qtd = int(input("Quantos nomes deseja digitar? "))

for i in range(qtd):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

# 2. Remover duplicatas
unicos_set = set(nomes)

# 3. Ordenar alfabeticamente
nomes_ordenados = sorted(unicos_set)

# 4. Criar tupla com o primeiro e último nome
extremos = (nomes_ordenados[0], nomes_ordenados[-1])

# 5. Exibir relatório final
print("\n--- RELATÓRIO FINAL ---")
print(f"Total digitados: {len(nomes)}")
print(f"Total de únicos: {len(unicos_set)}")
print(f"Lista ordenada: {nomes_ordenados}")
print(f"Tupla (primeiro, último): {extremos}")