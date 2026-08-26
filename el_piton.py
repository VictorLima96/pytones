num_1 = input("Digite um número: ")

num_2 = input("Digite um outro número: ")

if num_1 > 0 and num_2 < 0:
    print("O {0} é positivo e o {1} é negativo.".format(num_1, num_2))
elif num_1 < 0 and num_2 > 0:
    print("O {0} é negativo e o {1} é positivo.".format(num_1, num_2))
else:
    print("Os números têm o mesmo sinal.")