senha_correta = "1327"

while True:
    senha_digitada = input("Digite a senha")
    if senha_digitada == senha_correta:
        print("Acesso permitido")
        break
    else:
        print("Senha incorreta, tente novamente")
