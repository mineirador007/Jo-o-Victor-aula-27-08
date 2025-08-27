items = set()  # Set para itens únicos

for arquivo in ['lista_a.txt', 'lista_b.txt']:
    try:
        with open(arquivo, 'r') as f:
            for line in f:
                item = line.strip()
                if item:
                    items.add(item)
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado. Processando o outro se existir.")

# Ordena alfabeticamente
sorted_items = sorted(items)

# Salva no arquivo
with open('lista_unica.txt', 'w') as f:
    for item in sorted_items:
        f.write(item + '\n')
print("Arquivo lista_unica.txt gerado com itens únicos em ordem alfabética.")