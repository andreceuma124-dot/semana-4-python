# sistema_produtos.py

# 1. Lista de produtos
produtos = [
    {"nome": "Teclado Mecânico", "preco": 250.00, "categoria": "Periféricos"},
    {"nome": "Mouse Gamer", "preco": 120.50, "categoria": "Periféricos"},
    {"nome": "Monitor 24'", "preco": 899.90, "categoria": "Monitores"},
    {"nome": "Cadeira de Escritório", "preco": 450.00, "categoria": "Móveis"},
    {"nome": "Fone de Ouvido", "preco": 80.00, "categoria": "Áudio"}
]

# Filtragem por preço
limite_preco = float(input("Digite o valor para filtrar produtos acima deste preço: R$ "))
produtos_filtrados = [p for p in produtos if p["preco"] > limite_preco]

# 2. Ordenação e Categorias Únicas
produtos_crescente = sorted(produtos, key=lambda x: x["preco"])
produtos_decrescente = sorted(produtos, key=lambda x: x["preco"], reverse=True)
categorias_unicas = set(p["categoria"] for p in produtos)

# 3. Tupla com Estatísticas
precos = [p["preco"] for p in produtos]
estatisticas = (min(precos), max(precos), sum(precos) / len(precos))

# Relatório Final Formatado (f-strings)
print("\n" + "="*45)
print("          RELATÓRIO DE PRODUTOS          ")
print("="*45)

print(f"\n1. Produtos com preço acima de R$ {limite_preco:.2f}:")
for p in produtos_filtrados:
    print(f"  • {p['nome']} ({p['categoria']}) - R$ {p['preco']:.2f}")

print("\n2. Categorias Únicas (Set):")
for cat in sorted(categorias_unicas):
    print(f"  • {cat}")

print("\n3. Produtos por Ordem Crescente de Preço:")
for p in produtos_crescente:
    print(f"  • {p['nome']:<25} -> R$ {p['preco']:>7.2f}")

print("\n4. Produtos por Ordem Decrescente de Preço:")
for p in produtos_decrescente:
    print(f"  • {p['nome']:<25} -> R$ {p['preco']:>7.2f}")

print("\n5. Estatísticas Gerais (Tupla):")
print(f"  • Menor Preço : R$ {estatisticas[0]:.2f}")
print(f"  • Maior Preço : R$ {estatisticas[1]:.2f}")
print(f"  • Preço Médio : R$ {estatisticas[2]:.2f}")
print("="*45)