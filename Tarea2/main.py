from Tarea2 import LCircularDoble

lista = LCircularDoble()
print("*" * 25)
lista.agregar_inicio(20)
lista.agregar_inicio(15)
lista.agregar_inicio(25)
lista.agregar_inicio(10)
lista.agregar_inicio(30)

lista.recorrer_inicia_fin()
print("*" * 25)

print('dato encontrado:',lista.buscar(30))
print("*" * 25)


