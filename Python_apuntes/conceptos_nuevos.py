# sirve para crear colas con listas

from collections import deque

from cupshelpers import Printer

tareas = [
    [6,'Distribución'],
    [2,'Diseño'],
    [1,'Concepción'],
    [7,'Mantenimiento'],
    [4,'Producción'],
    [3,'Planificación'],
    [5,'Pruebas'],]

#el metodo sort organiza las listas (en este caso por el numero)
print("tarea con metodo sort\t",tareas.sort())
print("tarea con metodo sorted\t",sorted(tareas))
cola = deque()
for rec in sorted(tareas):
    cola.append(rec[1])
print(cola)

#eliminar primer elemento de la cola
cola.popleft()

#la tupla es inmutable y el count va contar valores repetidos especificando el dato a buscar

tupla = (1,1,2,2,3,3)
print("Tupla \t",tupla)
print("Count en Tupla \t",tupla.count(3))

# los diccionarios tienen unmetodo llamado discard

dict = {"Andres","Juan","Carlos"}
print("Dict \t",dict)
dict.discard("Juan")
print("Discard en Dict \t",dict)

#los conjuntos son los set(), crea una lista o tupla en un conjunto sin repetidos

tupla = (1,1,2,2,3,3)
print("Tupla \t",tupla)
test = set(tupla)
print("Tupla con set \t",test)

#excepciones

try:
	n = float(input("Introduce un numero:"))
	5/n
except TypeError:
	print("No se puede dividir el niimero por una cadena”)
except ValueError:
	print("Debes introducir una cadena que sea un numero)
except ZeroDivisionError:
	print("No se puede dividir por cero, prueba otro nimero”)
except Exception as e:
	print( type(e).__name_")
