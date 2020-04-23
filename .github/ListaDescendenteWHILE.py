
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
    valor = int(input("Ingrese el tamaño de la lista descendente a generar: "))

    print("\t\tVALORES DE LA LISTA DESCENDENTE DE ", valor, " CARDINAL.")
    while 1<valor:
        print(valor,",", end=" ")
        if valor%10==0:
            print("\n")
        valor = valor - 1
    print(valor,".")

    repetir=input("\n\tPara generar otra lista Descendente  presione cualquier tecla, para salir 0: ")