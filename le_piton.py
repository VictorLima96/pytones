num_1 = input("Digite um número, fazendo o favor:")

num_2 = input("Digite um outro número, fazendo o favor:")

if num_1 > num_2:
    print("O maior número entre {0} e {1} é {2}".format(num_1, num_2, num_1))
elif num_2 > num_1:
    print("O maior número entre {0} e {1} é {2}".format(num_1, num_2, num_2))
else:
    print("Vixe Maria, tu digitou o mesmo número.")

input("Pressione Enter para fechar...")