content = None
try:
    # Tenta ler com UTF-8
    with open('comentarios.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except UnicodeDecodeError:
    # Se falhar, tenta com Latin-1
    with open('comentarios.txt', 'r', encoding='latin-1') as f:
        content = f.read()

if content is not None:
    # Remove espaços duplos (loop para casos múltiplos)
    while '  ' in content:
        content = content.replace('  ', ' ')
    # Substitui reticências por ponto único
    content = content.replace('...', '.')
    # Salva o conteúdo processado
    with open('comentarios_limpos.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Arquivo limpo salvo com sucesso.")
else:
    print("Não foi possível ler o arquivo.")