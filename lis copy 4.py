 #Exemplofiltrandonumerospares
numeros=[1,2,3,4,5,6,7,8]

#Modotradicional
numeros_pares=[]

for numero in numeros:

    if numero%2==0:

        numeros_pares.append(numero)

#Usandolistcomprehension
numeros_pares_compr=[numero for numero in numeros if numero%2==0]

print(numeros_pares) #Saida:[2,4,6,8]

print(numeros_pares_compr) #Saida:[2, 4,6,8]