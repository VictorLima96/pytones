# Inicializa o vetor de contadores para cada sistema operacional (índices 0 a 5)

counts = [0] * 6

# Nomes dos sistemas operacionais correspondentes aos índices

os_names = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]

while True:

    n = int(input("Digite o número do Sistema Operacional (0 para sair): "))

    if n == 0:

        break

    if n < 1 or n > 6:

        print("Valor inválido. Digite um número entre 0 e 6.")

        continue

    counts[n-1] += 1

total = sum(counts)

if total == 0:

    print("Nenhum voto foi registrado.")

else:

    # Encontra o índice do sistema operacional com mais votos

    max_index = 0

    for i in range(1, 6):

        if counts[i] > counts[max_index]:

            max_index = i

    # Calcula a porcentagem (arredondada para o inteiro mais próximo)

    percentage = round((counts[max_index] / total) * 100)

    print(f"O Sistema Operacional mais votado foi o {os_names[max_index]}, com {counts[max_index]} votos, correspondendo a {percentage}% dos votos.")