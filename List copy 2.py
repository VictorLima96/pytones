L = []

while True:

    palavra = input("Digite uma palavra: ")

    if palavra == "":
        break
    if not palavra in L:
        L.append(palavra)

print("Palavras digitadas:", L)

for palavra in L:
    print(palavra)