#Conexión y CRUDs a base de datos --- Inventario



import sqlite3

class CRUD_Inventario():
    def __init__(self):
        self.conexion = sqlite3.connect('DB_OptiFood.db')
    
    def insertar_datos(self,nombre,cantidad,unidadM,categoria,proveedor):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO inventario (Nombre, Cantidad, UnidadMed, Categoria, Proveedor)
        VALUES('{}','{}','{}','{}','{}')'''.format(nombre,cantidad, unidadM, categoria, proveedor)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()


    def mostrar_datos(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM inventario"
        cursor.execute(bd)
        datos = cursor.fetchall()
        return datos
    
    def elimina_datos(self, nombre):
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM inventario WHERE Nombre = '{}' '''.format(nombre)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def actualiza_datos(self,ID,nombre,cantidad,unidadM,categoria,proveedor):
        cursor = self.conexion.cursor()
        bd = '''UPDATE inventario SET Nombre = '{}' , Cantidad = '{}', UnidadMed = '{}', Categoria = '{}', Proveedor = '{}' WHERE Id = '{}' '''.format(nombre,cantidad,unidadM,categoria, proveedor,ID)
        cursor.execute(bd)
        dato = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return dato
