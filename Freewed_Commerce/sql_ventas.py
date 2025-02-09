#Conexión y CRUDs a base de datos --- Ventas



import sqlite3

class CRUD_Ventas():
    def __init__(self):
        self.conexion = sqlite3.connect('DB_OptiFood.db')
    
    def finalizar_compra(self,cantidad,total,fecha):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO orden (Cantidad, Total, Fecha)
        VALUES('{}','{}','{}')'''.format(cantidad,total,fecha)
        cursor.execute(bd)
        self.conexion.commit()
        cursor.close()


    def unitario(self, nombre):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM menu WHERE Nombre = ('{}')'''.format(nombre) 
        cursor.execute(bd)
        datos = cursor.fetchall()
        return datos

    def valores_combo(self):
        cursor = self.conexion.cursor()
        bd = "SELECT Nombre FROM menu"
        cursor.execute(bd)
        datos = [fila[0] for fila in cursor.fetchall()]
        return datos

    def mostrar_datos(self):
        cursor = self.conexion.cursor()
        bd = "SELECT * FROM orden"
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
    
   
    