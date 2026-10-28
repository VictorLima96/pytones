s = input("Digite uma string: ")
vogais = "aeiou"
resultado = "".join(c.upper() if c in vogais else c for c in s)
print(resultado)
