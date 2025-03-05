from tkinter import Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import StringVar, Scrollbar, Frame, messagebox
from sql_inventario import CRUD_Inventario
from time import strftime
import pandas as pd
import menu_principal

def salir_invetario():
    ventana.destroy()
    menu_principal.mostrar_menuPrincpal()


class Ventana(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.nombre = StringVar()
        self.cantidadI = StringVar()
        self.unidadMed = StringVar()
        self.categoria = StringVar()
        self.proveedor = StringVar()

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=5)
        self.base_datos = CRUD_Inventario()

        self.widgets()

    def widgets(self):
        self.frame_titulo = Frame(self.master, bg="#E0E0E0", height=200, width=800)
        self.frame_titulo.grid(column=0, row=0, sticky='nsew')
        self.frame_uno = Frame(self.master, bg="#E0E0E0", height=200, width=800)
        self.frame_uno.grid(column=0, row=1, sticky='nsew')
        self.frame_dos = Frame(self.master, bg="#E0E0E0", height=300, width=800)
        self.frame_dos.grid(column=0, row=2, sticky='nsew')

        self.frame_titulo.columnconfigure([0,1,2,3,4], weight=1)
        self.frame_titulo.rowconfigure([0,1], weight=1)
        self.frame_uno.columnconfigure([0,1,2], weight=1)
        self.frame_uno.rowconfigure([0,1,2,3,4,5], weight=1)
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)

        Button(self.frame_titulo, text='REGRESAR', font=('Arial', 9, 'bold'), command=salir_invetario, fg='black', bg='#C3C3C3', width=20, bd=3).grid(column=0, row=0, pady=5)
        Label(self.frame_titulo, text='Inventario', bg='#E0E0E0', fg='black', font=('Oswald', 25, 'bold')).grid(columnspan=5, column=0, row=1)

        Label(self.frame_uno, text='Opciones', bg='#E0E0E0', fg='black', font=('Oswald', 13, 'bold')).grid(column=2, row=0)
        Button(self.frame_uno, text='REFRESCAR', font=('Arial', 9, 'bold'), command=self.actualizar_tabla, fg='white', bg='midnightblue', width=20, bd=3).grid(column=2, row=1, pady=5)

        Label(self.frame_uno, text='Datos', bg='#E0E0E0', fg='black', font=('Oswald', 13, 'bold')).grid(columnspan=2, column=0, row=0, pady=5)
        Label(self.frame_uno, text='Nombre', bg='#E0E0E0', fg='black', font=('Oswald', 13, 'bold')).grid(column=0, row=1, pady=5)
        Label(self.frame_uno, text='CantidadI', bg='#E0E0E0', fg='black', font=('Oswald', 13, 'bold')).grid(column=0, row=2, pady=5)
        Label(self.frame_uno, text='Unidad Medida', bg='#E0E0E0', fg='black', font=('Oswald', 13, 'bold')).grid(column=0, row=3, pady=5)
        Label(self.frame_uno, text='Categoría', bg='#E0E0E0', fg='black', font=('Oswald', 13, 'bold')).grid(column=0, row=4, pady=5)
        Label(self.frame_uno, text='Proveedor', bg='#E0E0E0', fg='black', font=('Oswald', 13, 'bold')).grid(column=0, row=5, pady=5)

        Entry(self.frame_uno, textvariable=self.nombre, font=('Arial', 12), highlightbackground="black", highlightthickness=1).grid(column=1, row=1)
        Entry(self.frame_uno, textvariable=self.cantidadI, font=('Arial', 12), highlightbackground="black", highlightthickness=1).grid(column=1, row=2)
        Entry(self.frame_uno, textvariable=self.proveedor, font=('Arial', 12), highlightbackground="black", highlightthickness=1).grid(column=1, row=5)

        opciones_unidadMed = ["kg", "lt", "pza(s)", "paquete(s)"]
        self.combo_unidadMed = ttk.Combobox(self.frame_uno, values=opciones_unidadMed, font=('Arial', 12))
        self.combo_unidadMed.set(opciones_unidadMed[0])
        self.combo_unidadMed.grid(row=3, column=1)
        self.unidadMed = self.combo_unidadMed.get()

        opciones_cat = ["Vegetales", "Carnes", "Variado", "Limpieza"]
        self.combo_cat = ttk.Combobox(self.frame_uno, values=opciones_cat, font=('Arial', 12))
        self.combo_cat.set(opciones_cat[0])
        self.combo_cat.grid(row=4, column=1)
        self.categoria = self.combo_cat.get()

        Button(self.frame_uno, text='AÑADIR A INVENTARIO', font=('Arial', 9, 'bold'), bg='midnightblue', fg='white', width=20, bd=3, command=self.agregar_datos).grid(column=2, row=2, pady=5, padx=5)
        Button(self.frame_uno, text='LIMPIAR CAMPOS', font=('Arial', 9, 'bold'), bg='midnightblue', fg='white', width=20, bd=3, command=self.limpiar_campos).grid(column=2, row=3, pady=5, padx=5)
        Button(self.frame_uno, text='ACTUALIZAR DATOS', font=('Arial', 9, 'bold'), bg='midnightblue', fg='white', width=20, bd=3, command=self.actualizar_datos).grid(column=2, row=4, pady=5, padx=5)
        Button(self.frame_uno, text='EXPORTAR A EXCEL', font=('Arial', 9, 'bold'), bg='midnightblue', fg='white', width=20, bd=3, command=self.guardar_datos).grid(column=2, row=5, pady=5, padx=5)

        estilo_tabla = ttk.Style()
        estilo_tabla.configure("Treeview", font=('Helvetica', 10, 'bold'), foreground='black', background='white')
        estilo_tabla.map('Treeview', background=[('selected', 'midnightblue')], foreground=[('selected', 'white')])
        estilo_tabla.configure('Heading', background='#E0E0E0', foreground='#357CF1', padding=3, font=('Arial', 10, 'bold'))

        self.tabla = ttk.Treeview(self.frame_dos)
        self.tabla.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_dos, orient='horizontal', command=self.tabla.xview)
        ladox.grid(column=0, row=1, sticky='ew')
        ladoy = ttk.Scrollbar(self.frame_dos, orient='vertical', command=self.tabla.yview)
        ladoy.grid(column=1, row=0, sticky='ns')
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        self.tabla['columns'] = ('CantidadI', 'UnidadMed', 'Categoria', 'Proveedor')
        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('CantidadI', minwidth=100, width=120, anchor='center')
        self.tabla.column('UnidadMed', minwidth=100, width=120, anchor='center')
        self.tabla.column('Categoria', minwidth=100, width=105, anchor='center')
        self.tabla.column('Proveedor', minwidth=100, width=105, anchor='center')

        self.tabla.heading('#0', text="Nombre", anchor='center')
        self.tabla.heading('CantidadI', text="CantidadI", anchor='center')
        self.tabla.heading('UnidadMed', text="UnidadMed", anchor='center')
        self.tabla.heading('Categoria', text="Categoria", anchor='center')
        self.tabla.heading('Proveedor', text="Proveedor", anchor='center')

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
        self.tabla.bind("<Double-1>", self.eliminar_datos)

    def obtener_fila(self, event):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        self.nombre.set(self.data['text'])
        self.cantidadI.set(self.data['values'][0])
        self.combo_unidadMed.set(self.data['values'][1])
        self.combo_cat.set(self.data['values'][2])
        self.proveedor.set(self.data['values'][3])

    def eliminar_datos(self, event):
        self.limpiar_campos()
        item = self.tabla.selection()[0]
        x = messagebox.askquestion('Informacion', '¿Desea eliminar?')
        if x == 'yes':
            self.tabla.delete(item)
            self.base_datos.elimina_datos(self.data['text'])

    def agregar_datos(self):
        nombre = self.nombre.get()
        cantidadI = self.cantidadI.get()
        unidadMed = self.combo_unidadMed.get()
        categoria = self.combo_cat.get()
        proveedor = self.proveedor.get()
        datos = (cantidadI, unidadMed, categoria, proveedor)
        if nombre and cantidadI and unidadMed and categoria and proveedor != '':
            self.tabla.insert('', 0, text=nombre, values=datos)
            self.base_datos.insertar_datos(nombre, cantidadI, unidadMed, categoria, proveedor)
            self.limpiar_campos()

    def actualizar_tabla(self):
        self.limpiar_campos()
        datos = self.base_datos.mostrar_datos()
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for dato in datos:
            i = i + 1
            self.tabla.insert('', i, text=datos[i][1:2][0], values=datos[i][2:6])

    def actualizar_datos(self):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        nombre = self.data['text']
        datos = self.base_datos.mostrar_datos()
        for fila in datos:
            Id = fila[0]
            nombre_bd = fila[1]
            if nombre_bd == nombre:
                if Id is not None:
                    nombre = self.nombre.get()
                    cantidadI = self.cantidadI.get()
                    unidadMed = self.combo_unidadMed.get()
                    categoria = self.combo_cat.get()
                    proveedor = self.proveedor.get()
                    if nombre and cantidadI and unidadMed and categoria and proveedor != '':
                        self.base_datos.actualiza_datos(Id, nombre, cantidadI, unidadMed, categoria, proveedor)
                        self.tabla.delete(*self.tabla.get_children())
                        datos = self.base_datos.mostrar_datos()
                        i = -1
                        for dato in datos:
                            i = i + 1
                            self.tabla.insert('', i, text=datos[i][1:2][0], values=datos[i][2:6])
        self.limpiar_campos()

    def limpiar_campos(self):
        self.nombre.set('')
        self.cantidadI.set('')
        self.combo_unidadMed.set('kg')
        self.combo_cat.set('Vegetales')
        self.proveedor.set('')

    def guardar_datos(self):
        self.limpiar_campos()
        datos = self.base_datos.mostrar_datos()
        i = -1
        nombre, cantidadI, unidadMed, categoria, proveedor = [], [], [], [], []
        for dato in datos:
            i = i + 1
            nombre.append(datos[i][1])
            cantidadI.append(datos[i][2])
            unidadMed.append(datos[i][3])
            categoria.append(datos[i][4])
            proveedor.append(datos[i][5])
        fecha = str(strftime('%d-%m-%y_%H-%M-%S'))
        datos = {'Nombres': nombre, 'Cantidad': cantidadI, 'UnidadMed': unidadMed, 'Categoria': categoria, 'Proveedor': proveedor}
        df = pd.DataFrame(datos, columns=['Nombres', 'CantidadI', 'UnidadMed', 'Categoria', 'Proveedor'])
        df.to_excel((f'INVENTARIO {fecha}.xlsx'))
        messagebox.showinfo('Informacion', 'Datos guardados')


def mostrar_inventario():
    global ventana
    ventana = Tk()
    ventana.title('Inventario')
    ventana.minsize(height=400, width=600)
    ventana.geometry('800x500+250+100')
    app = Ventana(ventana)
    app.actualizar_tabla()
    ventana.mainloop()

if __name__ == "__main__":
    mostrar_inventario()