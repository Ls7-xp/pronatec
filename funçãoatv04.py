def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 6.0:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
       
    return media, situacao
nota1 = 8.0
nota2 = 7.0
nota3 = 6.5
media, situacao = calcular_media(nota1, nota2, nota3)
print(f"Média: {media:.2f} - Situação: {situacao}")