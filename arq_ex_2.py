import random

# --- PARTE 1: Criar o arquivo com 100 números aleatórios ---
# Geramos uma lista de 100 números aleatórios entre 1 e 1000
numeros_aleatorios = [random.randint(1, 1000) for _ in range(1000)]

# Convertemos os números para texto e juntamos todos usando um espaço " "
linha_unica = " ".join(map(str, numeros_aleatorios))

# Gravamos a linha única no arquivo
with open('numeros.txt', 'w', encoding='utf-8') as arquivo_escrita:
    arquivo_escrita.write(linha_unica)

print("Arquivo 'numeros.txt' criado com sucesso com 100 números!")


# --- PARTE 2: Função para ler o arquivo e retornar a somatória ---
def somar_numeros_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_leitura:
            # Lê o conteúdo completo do arquivo (que é uma única linha)
            conteudo = arquivo_leitura.read()
            
            # .split() divide o texto em uma lista de strings usando o espaço como separador
            lista_strings = conteudo.split()
            
            # Converte cada string de volta para número inteiro
            lista_numeros = [int(num) for num in lista_strings]
            
            # Retorna a soma de todos os itens da lista
            return sum(lista_numeros)
            
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return 0

# --- Executando a função e mostrando o resultado ---
resultado_soma = somar_numeros_do_arquivo('numeros.txt')
print(f"A somatória de todos os números dentro do arquivo é: {resultado_soma}")
