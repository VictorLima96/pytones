import math

num = int(input("Digite um número: "))

mult = 0

for count in range(1,11):

    if(num % count == 0): 

        print("Múltiplo de", count)

        mult += 1

if(mult == 0):

    print(f"Você digitou {num} números primos de um total de 10 números.")

input("Pressione Enter para fechar...")