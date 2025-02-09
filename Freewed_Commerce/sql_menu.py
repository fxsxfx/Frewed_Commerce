#Conexión y CRUDs a base de datos --- Menu



import sqlite3

class CRUD_Menu():
    def __init__(self):
        self.conexion = sqlite3.connect('DB_OptiFood.db')
    
    def insertar_datos(self,nombre,disponibilidad,precio,calorias):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO menu (Nombre, Disponibilidad, Precio, Calorias)
        VALUES('{}','{}','{}','{}')'''.format(nombre,disponibilidad, precio, calorias)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()


    def mostrar_datos(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM menu"
        cursor.execute(bd)
        datos = cursor.fetchall()
        return datos
    
    def elimina_datos(self, nombre):
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM menu WHERE Nombre = '{}' '''.format(nombre)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()

    def actualiza_datos(self,ID,nombre,disponibilidad,precio,calorias):
        cursor = self.conexion.cursor()
        bd = '''UPDATE menu SET Nombre = '{}' , Disponibilidad = '{}', Precio = '{}', Calorias = '{}' WHERE Id = '{}' '''.format(nombre,disponibilidad,precio,calorias,ID)
        cursor.execute(bd)
        dato = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return dato