def main():
    try:
        num = []
        for i in range(1, 4):
            valor = int(input(f"Digite o {i}º número inteiro: ").strip())
            num.append(valor)
        if len(set(num)) != 3:
            print("Erro: Os números diferem entre si.") 
            return

        num.sort(reverse=True)

        print("Números em ordem decrescente: ", num)

    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")
if __name__ == "__main__":
    main()

input("Pressione Enter para fechar...")