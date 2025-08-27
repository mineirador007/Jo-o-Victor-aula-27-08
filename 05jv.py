items = set()  # Set para itens únicos

for arquivo in ['lista_a.txt', 'lista_b.txt']:
    try:
        with open(arquivo, 'r') as f:
            for line in f:
                item = line.strip()
                if item:
                    items.add(item)
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado. Prosseguindo sem ele.")

# Ordena os itens
sorted_items = sorted(items)

# Salva no novo arquivo
with open('lista_uniq.txt', 'w') as f:
    for item in sorted_items:
        f.write(item + '\n')
print("Arquivo lista_uniq.txt gerado com itens únicos ordenados.")