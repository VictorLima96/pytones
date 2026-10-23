# 1. Abre o arquivo original para ler todas as linhas
with open('pares.txt', 'r', encoding='utf-8') as arquivo_origem:
    linhas = arquivo_origem.readlines()

# 2. Inverte a ordem da lista de linhas (o maior número vai para o topo)
# O fatiamento [::-1] cria uma cópia da lista de trás para frente
linhas_invertidas = linhas[::-1]

# 3. Salva o resultado no arquivo 'invertido.txt'
with open('invertido.txt', 'w', encoding='utf-8') as arquivo_destino:
    arquivo_destino.writelines(linhas_invertidas)

print("Arquivo 'invertido.txt' gerado com sucesso!")
print(f"Primeira linha: {linhas_invertidas[0].strip()} (Maior)")
print(f"Última linha: {linhas_invertidas[-1].strip()} (Menor)")
