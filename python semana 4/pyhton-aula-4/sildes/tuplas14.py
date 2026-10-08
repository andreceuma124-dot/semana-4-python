# Tupla inicial de exemplo
ponto = (10, 20, 10, 5, 30)
print(f"Tupla inicial: {ponto}\n")

# 1. count(valor) - Conta quantas vezes o valor aparece
qtd = ponto.count(10)
print(f"1. count(10): O número 10 aparece {qtd} vezes na tupla.")

# 2. index(valor) - Retorna o índice da primeira ocorrência
posicao = ponto.index(20)
print(f"2. index(20): O valor 20 está na posição/índice {posicao}.")

# 3. len(tupla) - Retorna o total de elementos
tamanho = len(ponto)
print(f"3. len(ponto): A tupla possui {tamanho} elementos.")

# 4. max(tupla) e min(tupla) - Maior e menor valor
maior = max(ponto)
menor = min(ponto)
print(f"4. max(ponto) e min(ponto): Maior valor = {maior} | Menor valor = {menor}.")

# 5. sum(tupla) - Soma todos os elementos numéricos
total = sum(ponto)
print(f"5. sum(ponto): A soma de todos os elementos é {total}.")

# 6. sorted(tupla) - Retorna uma nova lista ordenada (a tupla original não muda)
ordenados = sorted(ponto)
print(f"6. sorted(ponto): Retorna a lista ordenada {ordenados}.")

# 7. tuple(iterável) - Converte uma lista de volta para tupla
lista_exemplo = [1, 2, 3]
nova_tupla = tuple(lista_exemplo)
print(f"7. tuple([1, 2, 3]): Converteu a lista no tipo {type(nova_tupla)} -> {nova_tupla}")
