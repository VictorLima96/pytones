soma = 0
quantidade = 0

while True:
    n = int(input("Digite um número (0 para sair): "))

    if n == 0:
        break

    soma = soma + n
    quantidade = quantidade + 1

print(f"Quantidade: {quantidade}")
print(f"Soma: {soma}")

if quantidade > 0:
    print(f"Média: {soma / quantidade}")
else:
    print("Média: 0")

input("Pressione Enter para fechar o programa...")