import math
#Programa para  generar los numeros de manera ascendente hasta el indicado por el usuario.
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
    valor = int(input("Ingrese el tamaño de la lista ascendente a generar: "))
    i=0
    prod=0
    print("\t\tVALORES DE LA LISTA ASCENDENTE DE ", valor, " CARDINAL.")
    while i<valor-1:
        i=i+1
        print(i,",", end=" ")
        if i%10==0:
            print("\n")
    print(valor,".")

    repetir=input("\n\tPara generar otra lista ascendente  presione cualquier tecla, para salir 0: ")