while True:

    try:
        n = int(input("Digite um número entre 0 e 10: "))

        if 0 <= n <= 10:
            print(f"Você digitou um número aceito: {n}")
            break

        print("Valor fora do intervalo!")

    except ValueError:
        print("Digite um número inteiro válido!")

input("Pressione Enter para fechar o programa...")