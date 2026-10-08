import os
import sys
# Garante que o Python ache o arquivo na mesma pasta
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import adicionar

if __name__ == "__main__":
    # Usamos o nome_do_modulo.nome_da_funcao
    print(adicionar.adicionar(["mouse"], "teclado"))

