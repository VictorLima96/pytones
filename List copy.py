L = []

somaPar = 0

somaImpar = 0

for i in range(5):

    x = int(input())

    L.append(x)

print(L.reverse())

for i in range(4, -1, -1):

    print(L[i], end="")
