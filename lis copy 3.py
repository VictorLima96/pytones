numeros=[1,2,3,4,5,6,7,8]

def eh_par(num):

    return num%2==0

def quadrado(num):

    return num * num

quadrados_pares= map(quadrado, filter(eh_par,numeros))

print(list(quadrados_pares)) #Saida:[4,16,36,64]