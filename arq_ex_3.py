import random

# --- PASSO INICIAL: Criar o arquivo com 100 números aleatórios para o teste ---
# Geramos 100 números (com chance de repetição, ex: entre 1 e 50) em uma única linha
with open('numeros.txt', 'w', encoding='utf-8') as f:
    f.write(" ".join(str(random.randint(1, 50)) for _ in range(100)))


# --- FUNÇÃO 1: Ler o arquivo e salvar na lista 'num' ---
def ler_arquivo_para_lista(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        # Lê o conteúdo, divide pelos espaços e converte cada item para inteiro
        num = [int(x) for x in arquivo.read().split()]
    return num


# --- FUNÇÃO 2: Remover elementos repetidos mantendo uma nova lista ---
def remover_repetidos(lista_num):
    num_unicos = []
    for item in lista_num:
        if item not in num_unicos:
            num_unicos.append(item)
    return num_unicos


# --- FUNÇÃO 3: Gravar a lista num_unicos no novo arquivo ---
def gravar_lista_em_arquivo(lista_unicos, nome_arquivo_destino):
    with open(nome_arquivo_destino, 'w', encoding='utf-8') as arquivo:
        # Grava os números separados por espaço na mesma linha
        arquivo.write(" ".join(map(str, lista_unicos)))


# --- EXECUÇÃO DO FLUXO COMPLETO ---

# 1. Chamando a primeira função para ler o arquivo original
num = ler_arquivo_para_lista('numeros.txt')
print(f"Quantidade de números lidos do arquivo original: {len(num)}")

# 2. Chamando a segunda função para filtrar os repetidos
num_unicos = remover_repetidos(num)
print(f"Quantidade de números únicos encontrados: {len(num_unicos)}")

# 3. Chamando a terceira função para salvar o resultado
gravar_lista_em_arquivo(num_unicos, 'numeros_unicos.txt')
print("Arquivo 'numeros_unicos.txt' gerado com sucesso!")
