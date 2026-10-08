# Lista inicial
lista = [10, 20, 30, 10]
print(f"Lista inicial: {lista}\n")

# 1. append(40) - Adiciona 40 ao final
lista.append(40)
print(f"1. Após append(40): {lista}")

# 2. insert(1, 15) - Insere 15 na posição de índice 1
lista.insert(1, 15)
print(f"2. Após insert(1, 15): {lista}")

# 3. remove(20) - Remove a primeira ocorrência do valor 20
lista.remove(20)
print(f"3. Após remove(20): {lista}")

# 4. pop() - Remove e retorna o último elemento (40)
x = lista.pop()
print(f"4. Elemento removido com pop(): {x} | Lista atual: {lista}")

# 5. count(10) - Conta quantas vezes o valor 10 aparece na lista
qtd_dez = lista.count(10)
print(f"5. O valor 10 aparece {qtd_dez} vezes na lista.")

# 6. index(30) - Retorna o índice da primeira ocorrência do valor 30
indice_trinta = lista.index(30)
print(f"6. O valor 30 está no índice: {indice_trinta}")

# 7. sort() - Ordena a lista em ordem crescente
lista.sort()
print(f"7. Após sort(): {lista}")

# 8. reverse() - Inverte a ordem dos elementos da lista
lista.reverse()
print(f"8. Após reverse(): {lista}")