dicionario = {

    'nome': 'chico',

    5: 'cinco',

    'lista': [1,6,7]

}

procChaves = dicionario.keys()

listChaves = list(procChaves)

print(dicionario)

print("Procurando a chave 'nome' no dicionario: ", 'nome' in dicionario)

print("Procurando a chave 5 no dicionario: ", 5 in dicionario)

print("Procurando a chave 'lista' no dicionario: ", 'lista' in dicionario)
