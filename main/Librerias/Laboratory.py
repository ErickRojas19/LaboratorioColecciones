from custom_functions import temperature_methods
import statistics

ol = []
for i in range(0,12):
    
    try:
        temp = int(input("Digite las temperaturas de la Guajira: "))
        ol.append(temp)
    except ValueError:
        print("Solo se escriben números: ")

for i in range(0,12):

    try:
        temp = int(input("Digite las temperaturas de Santander: "))
        ol.append(temp)
    except ValueError:
        print("Solo se escriben números: ")

for i in range(0,12):

    try:
        temp = int(input("Digite las temperaturas de Nariño: "))
        ol.append(temp)
    except ValueError:
        print("Solo se escriben números: ")


guajira = ol[0:12]
santander = ol[12:24]
narino = ol[24:36]

meses = {0:"Enero", 1:"Febrero", 2:"Marzo", 3:"Abril", 4:"Mayo", 5:"Junio", 6:"Julio", 7:"Agosto", 8:"Septiembre", 9:"Octubre", 10:"Noviembre", 11:"Diciembre"}

print("\n")
print("\n")

promedio_guajira = temperature_methods.promedio(guajira)
promedio_santander = temperature_methods.promedio(santander)
promedio_narino = temperature_methods.promedio(narino)

print("\n")

print("El promedio de la temperatura de la Guajira {}".format(promedio_guajira))
print("El promedio de la temperatura de Santander es {}".format(promedio_santander))
print("El promedio de la temperatura de Nariño es {}".format(promedio_narino))

print("\n")
print("\n")

promedio_nacional = temperature_methods.promedio(guajira+santander+narino)
print("El promedio nacional es {}".format(promedio_nacional))

print("\n")
print("\n")

mes_caliente_guajita = temperature_methods.tem_mayor(guajira)
mes_caliente_santander = temperature_methods.tem_mayor(santander)
mes_caliente_narino = temperature_methods.tem_mayor(narino)

print("El mes mas caliente de la guajira es: {}".format(mes_caliente_guajita))
print("El mes mas caliente de Santander es: {}".format(mes_caliente_santander))
print("El mes más caliente de Nariño es: {}".format(mes_caliente_narino))

print("\n")
print("\n")

mas_alto_de_todos = [mes_caliente_guajita,mes_caliente_santander,mes_caliente_narino]
promedio_mas_alto=temperature_methods.promedio(mas_alto_de_todos)
print("El promedio de los departamentos más calientes es de {}".format(promedio_mas_alto))

print("\n")
print("\n")

departamento_mayor = [mes_caliente_guajita,mes_caliente_santander,mes_caliente_narino]
temperatura_promedio_mas_caliente=temperature_methods.tem_mayor(departamento_mayor)
print("El promedio más caliente de los 3 departamentos es {}".format(temperatura_promedio_mas_caliente))

print("\n")
print("\n")

mayor_total = temperature_methods.tem_mayor(departamento_mayor)
print("El mayor de todos es {}".format(mayor_total))
posicion = mas_alto_de_todos.index(mayor_total)
n_depar = ["guajira","Santander","Nariño"]
print("La temperatura mayor del departamento se representa en {}".format(meses[posicion]))
print("El departamento más caliente fue {}".format(n_depar[posicion]))

print("\n")
print("\n")

desvi1 = temperature_methods.desviacion(guajira)
desvi2 = temperature_methods.desviacion(santander)
desvi3 = temperature_methods.desviacion(narino)

print("La desviacion de la Guajira es de {}, de Santander es de {} y de Nariño es de {}".format(desvi1,desvi2,desvi3))