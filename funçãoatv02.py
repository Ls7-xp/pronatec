def verificar_par_ou_impar(numero):
    if numero % 2==0:
        return "par"
    else:
        return "impar"
    
numero = 69
resultado = verificar_par_ou_impar(numero)
print(f"o número {numero} é {resultado}. ")