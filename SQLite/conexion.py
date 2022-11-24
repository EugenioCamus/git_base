import sqlite3
conexion = sqlite3.connect("basespruebacurso.db")
cursor = conexion.cursor()
nombre = str
def obtener_clientes(id):
    sql = f"SELECT * FROM clientes WHERE id = {id};"
    cursor.execute(sql)
    clientes = cursor.fetchone()
    nombre = clientes[1]
    print(f"nombre : {clientes[1]}")
    print(f"correo : {clientes[3]}")
    print(nombre)


def obtener_usuarios(id):
    sql = f"SELECT * FROM usuarios WHERE id = {id};"
    cursor.execute(sql)
    usuario = cursor.fetchone()
    print(usuario[1])
    

lista = obtener_clientes(12)

obtener_usuarios(2)
    