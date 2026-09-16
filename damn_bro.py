def calc_media(nota1, nota2, nota3):

    media = (nota1 + nota2 + nota3) / 3

    return media

print("Digite as três notas do aluno: ")

nota1 = float(input("Digite {1}ª nota: "))

nota2 = float(input("Digite {2}ª nota: "))

nota3 = float(input("Digite {3}ª nota: "))

resultado = calc_media(nota1, nota2, nota3)

if resultado >= 7.0:
        print(f"A média é: {resultado:.1f} - Aprovado chefe, não fez mais que sua obrigação !!!!!")
else:    
        print(f"A média é: {resultado:.1f} - Reprovado chefe, você é muito burro !!!!!")

input("\nPressione Enter para fechar...")