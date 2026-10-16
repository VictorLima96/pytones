a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

for linha in range (len(a)):
     for coluna in range(len(a[linha])):
          print([linha][coluna], end="")
     print()
 