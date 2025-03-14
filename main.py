#parcial

#Colonización de Marte – Envío de Recursos 
#El exitoso lanzamiento del Falcon Heavy como transporte confiable interplanetario, abrió las 
#posibilidades a la colonización interplanetaria, con primer objetivo el establecer 
#asentamientos humanos en Marte. 
#Para ello, se realizarán 15 lanzamientos de materiales necesarios para la colonización, que 
#estarán ubicados en las planicies (A)cidalia, (E)lysium y (U)topia. Cada #lanzamiento tiene un 
#cargamento de hasta 10.000 kg, pero por posibles daños durante el transporte, puede llegar 
#menos cantidad. También se puede dar el caso que no llegue ninguno de los 15 lanzamientos 
#a alguna de las planicies.

#Se requiere hacer un programa en Python que permita capturar para cada lanzamiento a cuál 
#planicie corresponde y cuánto material llegó, teniendo en cuenta el rango de valores válidos 
#para los lanzamientos. Si la planicie no es válida o el valor no está en el rango, debe repetirse 
#el ingreso del dato. 
# Posteriormente se generarán los siguientes resultados por cada planicie: 
# Cuantos lanzamientos llegaron a cada planicie 
# El total de material que llegó a cada planicie 
# El promedio de efectividad del transporte a cada planicie: total de material dividido por 
#la cantidad de lanzamientos. 
#El programa debe: 
# Realizar función CalculaPromedioEfectividad que recibe la cantidad de 
#lanzamientos que llegaron a cada planicie y la cantidad total de material entregado. La 
#función devuelve el promedio de material por lanzamiento. Son tres planicies, 
#entonces debe invocarse tres veces la función. 
# Debe visualizar de manera tabulada los resultados para cada planicie, es decir, en una 
#sola línea por cada planicie, escribir total lanzamientos, total material y promedio de 
#efectividad. 
# Debe tener control de excepciones en caso de se presenten errores por formato 
#inválido y posibles divisiones por cero.

print("Hola, este es un programa para calcular la efectividad de un transporte de materiales a Marte")


lanzamientos = 15
lanzamientos -= 1
def CalculaPromedioEfectividad(total_material, total_lanzamientos):
    try:
      lanzamientos = 15
      lanzamientosAcidalia = 0
      lanzamientosElysium = 0
      lanzamientosUtopia = 0
      while lanzamientos > 0:
        planicie = input("Ingrese la planicie donde se encuentra el lanzamiento (A=Acidalia, E=Elysium, U=Utopia): ")
        if planicie == "A":
            lanzamientosAcidalia += 1
        elif planicie == "E":
            lanzamientosElysium += 1
        elif planicie == "U":
            lanzamientosUtopia += 1
        else:
            print("Planicie inválida. Intentelo de nuevo por favor.")
            continue
        peso = int(input("Ingrese el peso del lanzamiento (entre 1000 y 10000 kg): "))
        if peso < 1000 or peso > 10000:
            print("Peso inválido. Ingrese un peso dentro del rango estipulado.")
            continue
            
        total_material += peso
      promedio_acidalia = lanzamientos + total_material / lanzamientosAcidalia
      print("Total de lanzamientos a Acidalia:", lanzamientosAcidalia)
      print("Total de material entregado a Acidalia:", total_material)
      print("Promedio de efectividad de Acidalia:", promedio_acidalia)
        
      promedio_elysium = lanzamientos + total_material / lanzamientosElysium
      print("Total de lanzamientos a Elysium:", lanzamientosElysium)
      print("Total de material entregado a Elysium:", total_material)
      print("Promedio de efectividad de Elysium:", promedio_elysium)
        
      promedio_utopia = lanzamientos + total_material / lanzamientosUtopia
      print("Total de lanzamientos a Utopia:", lanzamientosUtopia)
      print("Total de material entregado a Utopia:", total_material)
      print("Promedio de efectividad de Utopia:", promedio_utopia)

    
      
    except TypeError:
      print("Error de tipado")
    except ValueError:
      print("Error: Ingrese un valor numérico válido.")
    
  






