import string  # Para pontuação básica

try:
    with open('texto.txt', 'r') as f:
        content = f.read().lower()  # Converte para minúsculas
        # Remove pontuação substituindo por espaço
        for p in string.punctuation:
            content = content.replace(p, ' ')
        # Divide em palavras e usa set para únicas
        words = [word for word in content.split() if word]
        unique_count = len(set(words))
        print(f"Quantidade de palavras distintas: {unique_count}")
except FileNotFoundError:
    print("Arquivo texto.txt não encontrado.")