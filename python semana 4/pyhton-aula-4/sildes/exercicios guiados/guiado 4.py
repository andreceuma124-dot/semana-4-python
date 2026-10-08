# Exercício 4: conjunto sem duplicatas
texto = input("Palavras separadas por espaço: ")
palavras = texto.split()
# set() elimina os repetidos
unicos = set(palavras)
print("Digitadas:", len(palavras))
print("Unicas:", len(unicos))
print(sorted(unicos))