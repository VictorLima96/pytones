# Abre ambos os arquivos ao mesmo tempo para escrita ('w')
with open('pares.txt', 'w') as arquivo_pares, open('impares.txt', 'w') as arquivo_impares:
    
    # Passa por todos os números de 0 até 999
    for numero in range(1000):
        
        # Se for par, grava no arquivo de pares
        if numero % 2 == 0:
            arquivo_pares.write(f"{numero}\n")
            
        # Se for ímpar, grava no arquivo de ímpares
        else:
            arquivo_impares.write(f"{numero}\n")

print("Arquivos 'pares.txt' e 'impares.txt' gerados com sucesso!")