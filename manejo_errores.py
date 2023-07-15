print("Hola CaC")

print("\nDivisión de 2 numeros enteros")
numero1 = int(input("Ingrese dividendo: "))

while True:
    # para gestion de excepciones tenemos las clausulas try/except
    try:
        numero2 = int(input("Ingrese divisor: "))
        print("El resultado del cociente es: ", numero1/numero2)
        break
    except:
        print("No es posible dividir por cero")

