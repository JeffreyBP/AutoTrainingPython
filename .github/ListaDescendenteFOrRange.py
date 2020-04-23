
#Programa para  generar los numeros de manera descendente desde el valor indicado por el usuario usando FOR.
def modulo(a, b):
  '''Funcion que calcula el
  residuo (modulo) de una division'''
  residuo = 0
  x = a // b
  residuo = a - (x * b)
  return residuo

valor: int=0
repetir=''
while repetir != '0':
    valor = int(input("Ingrese el tamaño de la lista descendente a generar: "))

    print("\t\tVALORES DE LA LISTA DESCENDENTE DE ", valor, " CARDINAL.")
    for i in range(valor,1,-1):
        print(i,",", end=" ")
        if i%10==0:
            print("\n")

    print(i-1,")")

    repetir=input("\n\tPara generar otra lista Descendente  presione cualquier tecla, para salir 0: ")