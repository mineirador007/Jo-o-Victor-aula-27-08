jogadores_times = {}  # Dicionário para armazenar {nome: time}
invalid_lines = []  # Lista para linhas inválidas

try:
    with open('jogadores_times.txt', 'r') as f:
        for line in f:
            line = line.strip()  # Remove espaços extras
            if not line:
                continue  # Ignora linhas vazias
            try:
                # Split na primeira vírgula
                nome, time = line.split(',', 1)
                jogadores_times[nome.strip()] = time.strip()
            except ValueError:
                # Se não houver vírgula, adiciona à lista de inválidas
                invalid_lines.append(line)
except FileNotFoundError:
    print("Arquivo jogadores_times.txt não encontrado.")

# Escreve as linhas inválidas no log
try:
    with open('linhas_invalidas.log', 'w') as log:
        for inv in invalid_lines:
            log.write(inv + '\n')
    print("Dicionário criado:", jogadores_times)
except Exception as e:
    print(f"Erro ao escrever o log: {e}")