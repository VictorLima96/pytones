total = count = 0

while True:

    try:
        n = int(input("Digite um número: "))

        if 0 == n:
            break

        total += n

        count += 1

    except ValueError:
        print("Nenhum número foi digitado!")

if count > 0:
    media = total / count

print("Soma dos números digitados foi: ", total)

if count > 0:
    print("Média dos números digitados foi: ", media)

input("Pressione Enter para fechar o programa...")