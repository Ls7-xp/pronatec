def idade_em_dias(idade):
    dias_por_ano = 365
    dias = idade * dias_por_ano
    return dias
idade = 98
print(f"A pessoa de {idade} anos viveu aproximadamente {idade_em_dias(idade)} dias.")