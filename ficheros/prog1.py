def leer_fichero():
    file = open('archivo.txt', 'r')
    dato = file.read()
    print(dato)
    file.close()
leer_fichero()

def escribir_fichero():
    file = open('archivo.txt','a')
    dato="\nnew line 2"
    file.write(dato)
    file.close()

escribir_fichero()
leer_fichero()
archivo = open('archivo.txt')
for linea in archivo:
    print(linea)
