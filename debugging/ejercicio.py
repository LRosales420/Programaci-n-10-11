""" 
Encuentre los errores en el siguiente código y documente en el README, cuáles fueron los errores encontrados y cómo fueron solucionados.
Cree en la raíz del repositorio un directorio llamado debugging. Agregue este archivo y un README.md donde haga la descripción de los errores. 
"""

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def comparar_con_promedio(numeros, promedio):
    for num in numeros:
        if num > promedio:                  #Identación arreglada
            print(f"{num} es mayor que el promedio.")
        elif num < promedio:                #Identación arreglada
            print(f"{num} es menor que el promedio.")
        else:                               #Identación arreglada
            print(f"{num} es igual al promedio.")

# Pedir al usuario tres números
numeros = []
for i in range(3):
    num = input("Introduce un número: ")
    numeros.append(int(num)) #Convertir la "input" a un integer para poder hacer los calculos matemáticos.

# Calcular el promedio
promedio = calcular_promedio(numeros)

# Comparar cada número con el promedio
comparar_con_promedio(numeros, promedio)