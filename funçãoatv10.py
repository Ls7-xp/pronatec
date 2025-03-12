def calcular_litro_comprados(preco_litro, valor_desejado):
    litros_comprados = valor_desejado / preco_litro
    return litros_comprados
preco_litro = 6.19
valor_desejado = 50.90
litros = calcular_litro_comprados(preco_litro, valor_desejado)
print(f"Com R${valor_desejado:.2f}, serão comprados {litros:.2f} litros de combustível.")