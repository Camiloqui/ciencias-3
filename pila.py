f = open ('C:/Users/estudiantes/Documents/libros_desorden.txt','r')
mensaje=f.read()
mensaje.lower()
tupla=mensaje.lower().split(";")
mensaje1= tupla[1]
tupla2=[]

for n in tupla:
    mensaje1=n
    tupla1=mensaje1.split(",")
    tupla2.append(tupla1[1])
print(tupla2)
