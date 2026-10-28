s = input("Digite uma string: ")
normalizada = s.lower().replace(" ", "")
if normalizada == normalizada[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
