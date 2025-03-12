not1=float(input("digite sua primeira nota"))
not2=float(input("digite sua segunda nota"))
not3=float(input("digite sua terceira nota"))
not4=float(input("digite sua quarta nota"))

soma=(not1 + not2 + not3 + not4)/4
if(soma<7.0):
    print("reprovado")
else:
    print("aprovado")
print(soma)