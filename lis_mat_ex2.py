m = []

for num_linha in range(10):
     linha = []
     for num_coluna in range(15):
          linha.append(num_linha + num_coluna)
     m.append(linha)

     print(linha)

     print(linha[0])