print("Hola CaC")

print("\nDivisión de 2 numeros enteros")

while True:
    # para gestion de excepciones tenemos las clausulas try/except
    try:
        numero1 = int(input("Ingrese dividendo: "))
        numero2 = int(input("Ingrese divisor: "))
        print("El resultado del cociente es: ", numero1/numero2)
        break
    except ZeroDivisionError:
        print("No es posible dividir por cero")
    except ValueError:
        print("Valor ingresado no válido. Ingrese un numero")
try: 
    import test.py
except ModuleNotFoundError:
    print("El modulo que se dea importar no existe")
