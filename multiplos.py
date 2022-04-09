print("Calcular todos los multiplos introducidos por el usuario")
valorn=int(input("Digite un numero para sacar el multiplo: "))
valorm=int(input("Digite un numero para tomar la cantidad a sacar del multiplo: "))

def generar_multiplos(valorn,valorm):
    return [valorn * i for i in range(1,valorm + 1)]
print(generar_multiplos(valorn,valorm))
