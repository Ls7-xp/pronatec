def converter_dolar_para_real(valor_dolar):
    taxa_conversao = 5.79
    valor_real = valor_dolar* taxa_conversao
    return valor_real
valor_dolar = 777
valor_em_real = converter_dolar_para_real(valor_dolar)
print(f"${valor_dolar} equivale a R${valor_em_real:.2f}.")