import  statistics

def promedio(lista):

    suma = 0
    cont = len(lista)

    for componente in lista:
        suma += componente

    ranges = suma/cont

    return ranges

def tem_mayor(lista):

    mayor = lista[0]

    for componente in lista:

        if componente > mayor:
            mayor = componente
    return mayor

def tem_menor(lista):

   if len(lista):
       menor = lista[0]
       for elemento in lista:
           if elemento < menor: 
               menor = elemento
               return menor

def desviacion(lista):


    desvi = statistics.stdev(lista)

    return desvi
