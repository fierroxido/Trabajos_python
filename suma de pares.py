print("Ingresar el numero inicial")
i = int(input("Ingrese el numero inicial"))
print("Ingrese el numero final")
f = int(input("Ingresa el numero final"))
suma = 0
print("**Los numeros pares del rango**")
while i <= f:
    if i % 2 == 0:
        print(i)
    i+=1
    suma=suma+1
print("La suma de los numeros es:", suma)