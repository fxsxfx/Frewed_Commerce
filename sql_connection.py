#Conexión y CRUDs a base de datos



import sqlite3

class Comunicacion():
    def __init__(self):
        self.conexion = sqlite3.connect('DB_OptiFood.db')
    
    def insertar_datos(self,nombre,edad,correo,telefono):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO datos (Nombre, Edad, Correo, Telefono)
        VALUES('{}','{}','{}','{}')'''.format(nombre,edad,correo,telefono)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()


    def mostrar_datos(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM datos"
        cursor.execute(bd)
        datos = cursor.fetchall()
        return datos
    
    def elimina_datos(self, nombre):
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM datos WHERE Nombre = '{}' '''.format(nombre)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def actualiza_datos(self,ID,nombre,edad,correo,telefono):
        cursor = self.conexion.cursor()
        bd = '''UPDATE datos SET Nombre = '{}' , Edad = '{}', Correo = '{}', Telefono = '{}' WHERE Id = '{}' '''.format(nombre,edad,correo,telefono,ID)
        cursor.execute(bd)
        dato = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return dato



