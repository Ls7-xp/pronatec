("Sem parâmetro e sem retorno")
def saudacao():
    print("Olá, bem-vindo!")


("Com parâmetro e sem retorno")
def saudacao(nome):
    print(f"Olá, {nome}!")
saudacao("Carlos")

("Sem parâmetro e com retorno")
def obter_saudacao():
    return "Olá, bem-vindo!"
mensagem = obter_saudacao() 
print(mensagem)  


("Com parâmetro e com retorno")
def somar(a, b):
    return a + b
resultado = somar(5, 3)  
print(resultado)  
