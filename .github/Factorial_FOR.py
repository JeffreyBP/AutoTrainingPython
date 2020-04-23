#Programa para  generar lel factorial de los N enteros indicados por el usuario usando FOR.

valor: int=0
repetir=''
while repetir != '0':
    valor = int(input("Ingrese el valor del FACTORIAL N a calcular: "))
    factorial=1
    print("\t\tVALOR DEL FACTORIAL", valor, " NUMEROS.")
    for i in range(1, valor+1):
        factorial= factorial*i
        print("Valor del factorial ", i, " equivale a: ", factorial, ".", end="\n")


    repetir=input("\n\tPara generar otra lista Descendente  presione cualquier tecla, para salir 0: ")