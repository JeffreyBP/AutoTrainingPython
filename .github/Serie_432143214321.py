    #Crea serie  4,3,2,1,4,3,2,1,4,3,2,1... que pueda indicar cuantos elementos a imprimir.
    #c=interruptor
    #w=interruptor
    repetir=''
    while repetir != '0':
        longitud=int(input("Ingrese el valor de lementos de la serie por desplegar: "))
        controlador=0
        interruptor=4
        iteracion=0
        while controlador<longitud:
            #para organizar impresiones con diez columnas
            if iteracion % 10 == 0:
                print("\n")
            iteracion=iteracion+1
            print(interruptor, ",", end=" ")
            if interruptor>1:
                interruptor=interruptor-1
            else:
                interruptor=4
            controlador=controlador+1
        repetir=input("\n\tPara generar otra cantidad de valores de la Serie presione cualquier tecla, para salir 0: ")