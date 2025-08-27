try:
    # Abre o arquivo em modo leitura
    with open('frases.txt', 'r') as f:
        lines = f.readlines()  # Lê todas as linhas
        # Conta linhas não vazias após remover espaços
        non_empty = sum(1 for line in lines if line.strip())
        print(f"Quantidade de linhas não vazias: {non_empty}")
except PermissionError:
    # Mensagem amigável para erro de permissão
    print("Permissão negada para acessar o arquivo. Verifique as configurações de acesso.")