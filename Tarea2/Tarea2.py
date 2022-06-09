#lista Circular Doblemente Enlazada
#Eduardo Santos
#201800996

from nodo import Nodo

class LCircularDoble:
   
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False

    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__unirNodo()    

    def agregar_final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux

        self.__unirNodo()

    def __unirNodo(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero

    def recorrer_inicia_fin(self):
        aux = self.primero
        while aux:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break

    def recoorer_fin_inicio(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior
            if aux == self.ultimo:
                break

    def buscar(self, dato):
        aux = self.primero
        while aux:
            if aux.dato == dato:
                print("siguiente: ",aux.siguiente.dato)
                print("anterior: ",aux.anterior.dato)
                return dato          
                          
            else:
                aux = aux.siguiente
                if aux == self.primero:
                    return print("el valor no esta en la lista") 
                 
   