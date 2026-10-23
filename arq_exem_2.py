# Abre o arquivo original para leitura ('r') e o novo arquivo para escrita ('w')
with open('pares.txt', 'r') as arquivo_pares, open('multiplos_4.txt', 'w') as arquivo_multiplos:
    
    # Percorre cada linha do arquivo de números pares
    for linha in arquivo_pares:
        
        # Converte a linha de texto para um número inteiro (removendo o '\n')
        numero = int(linha.strip())
        
        # Verifica se o número é divisível por 4 (resto igual a 0)
        if numero % 4 == 0:
            # Grava o número múltiplo de 4 no novo arquivo
            arquivo_multiplos.write(f"{numero}\n")

print("Arquivo 'multiplos_4.txt' gerado com sucesso!")