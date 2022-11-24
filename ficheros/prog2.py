archivo = open("archivo.txt")
i = 1
for linea in archivo:
    linea = linea.rstrip("\\n")
    print( " %4d: %s" % (i, linea))
    i+=1
archivo.close()

archivo = open("archivo.txt")
for i, linea in enumerate(archivo):
    linea = linea.rstrip("\\n")
    print( " %4d: %s" % (i+1, linea))
archivo.close()

saludo = open("saludo", "w")
saludo.write("""
print "Hola Mundo"
""")
saludo.close()