try:
    # Tenta abrir o arquivo em modo leitura
    with open('notas.txt', 'r') as f:
        content = f.read()
        print(content)  # Imprime o conteúdo se o arquivo existir
except FileNotFoundError:
    # Se não existir, cria o arquivo com o texto especificado
    with open('notas.txt', 'w') as f:
        f.write("Arquivo criado.")
    # Agora lê e imprime o conteúdo recém-criado
    with open('notas.txt', 'r') as f:
        content = f.read()
        print(content)