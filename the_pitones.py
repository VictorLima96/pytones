def max(num_1,num_2):

    if num_1 > num_2:

        return num_1
    
    else:

        return num_2

num_1 = float(input("Digite um número, fazendo o favor:"))

num_2 = float(input("Digite um outro número, fazendo o favor:"))

resultado = max(num_1,num_2)

print(f"O maior número entre {num_1} e {num_2} é {resultado}")

input("Pressione Enter para fechar...")