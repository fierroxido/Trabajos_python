print("Calcule las potencias de 2")
base=2
exponente=int(input("Digite un numero entero para poder sacar un exponente: "))

def generar_potencias(base,exponente):
    resultado=1
    for i in range(exponente):
        resultado *= base
    return resultado


print(generar_potencias(base,exponente))
