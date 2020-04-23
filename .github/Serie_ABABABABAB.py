# Crea serie  A,B,A,B,A,B,A,B,A, ... que pueda indicar cuantos elementos a imprimir.

repetir = ''
while repetir != '0':
    longitud = int(input("Ingrese el valor de elementos de la serie por desplegar: "))
    controlador = 0
    interruptor = 4
    iteracion = 0
    while iteracion < longitud:
        # para organizar impresiones con diez columnas
        if iteracion % 10 == 0:
            print("\n")
        iteracion = iteracion + 1
        if iteracion % 2 == 0:
            print("B, ", end=" ")
        else:
            print("A, ", end=" ")

    repetir = input("\n\tPara generar otra cantidad de valores de la Serie presione cualquier tecla, para salir 0: ")
