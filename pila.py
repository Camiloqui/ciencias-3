class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa con una lista vacía
        self.items=[]

    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

f = open ('C:/Users/Camil/Documents/libros_desorden.txt','r')
mensaje=f.read()
mensaje.lower()
tupla=mensaje.lower().split(";")
mensaje1= tupla[1]
tupla2= Cola()
tupla3= Cola()
mensaje3=""
"""print(tupla,"\n")"""
for n in tupla:
    mensaje1=n
    tupla1=mensaje1.split(",")
    tupla2.encolar(tupla1[1])
    tupla3.encolar(tupla1[0])
#print(tupla2.items,"\n")

for recorrido in range(1,len(tupla2.items)):
    for posicion in range(len(tupla2.items) - recorrido):
        if tupla2.items[posicion]>tupla2.items[posicion+1]:
            temp=tupla2.items[posicion]
            tupla2.items[posicion]= tupla2.items[posicion+1]
            tupla2.items[posicion+1]=temp
            temp1=tupla3.items[posicion]
            tupla3.items[posicion]=tupla3.items[posicion+1]
            tupla3.items[posicion+1]=temp1
print(tupla2.items,"\n")
print(tupla3.items,"\n")
mensaje2= " ".join(tupla2.items)
for n in range(len(tupla2.items)):
    mensaje3=mensaje3+ "".join(tupla2.items[n])+"\n\t"
    mensaje3+= "".join(tupla3.items[n])+"\n"
print(mensaje3)
f = open('Libros_ordenados.txt','w')
f.write(mensaje3)
f.close()
