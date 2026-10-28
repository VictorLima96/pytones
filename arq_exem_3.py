# --- ETAPA 1: Ler da entrada padrão e gravar no arquivo ---
# Abrimos no modo 'a' (append) para adicionar contatos sem apagar os existentes.
# Se preferir que o arquivo comece do zero a cada execução, mude 'a' para 'w'.
with open('contatos.txt', 'a', encoding='utf-8') as arquivo:
    print("--- Cadastro de Contatos (Pressione ENTER com o nome vazio para parar) ---")
    
    while True:
        nome = input("Digite o nome: ").strip()
        
        # Condição de parada: se o nome for vazio, sai do laço
        if not nome:
            break
            
        telefone = input(f"Digite o telefone de {nome}: ").strip()
        
        # Grava o nome e o telefone na mesma linha, separados por uma vírgula
        arquivo.write(f"{nome}, {telefone}\n")

print("\nCadastro encerrado. Gravando dados...")


# --- ETAPA 2: Abrir o arquivo e mostrar os dados na tela ---
print("\n--- Lendo registros do arquivo 'contatos.txt' ---")
try:
    with open('contatos.txt', 'r', encoding='utf-8') as arquivo:
        # Lê linha por linha do arquivo
        for linha in arquivo:
            # Remove a quebra de linha \n e separa o nome do telefone usando a vírgula
            dados = linha.strip().split(', ')
            
            # Garante que a linha possui ambos os dados antes de exibir
            if len(dados) == 2:
                nome_salvo, telefone_salvo = dados
                print(f"Nome: {nome_salvo} | Telefone: {telefone_salvo}")
except FileNotFoundError:
    print("O arquivo 'contatos.txt' ainda não foi criado ou está vazio.")