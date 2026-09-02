x = int(input("Digite um número: "))

print("Valor da tabuada do número digitado é: ")
for i in range(1, 11):
    resultado = x * i
    print(f"{x} x {i} = {resultado}")

input("Pressione Enter para fechar...")