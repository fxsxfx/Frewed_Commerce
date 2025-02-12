import datetime
from tkinter import Tk, Button, Entry, Label, ttk, StringVar, Scrollbar, Frame, messagebox, DoubleVar, IntVar
import tkinter
from sql_ventas import CRUD_Ventas
from time import strftime
import pandas as pd
import menu_principal
import pronostico
import tickets 
import historial_ventas

def salir_ventas():
    ventana.destroy()
    menu_principal.mostrar_menuPrincpal()

def ir_pronostico():
    ventana.destroy()
    pronostico.mostrar_pronostico()

def ir_tickets():
    ventana.destroy()
    tickets.mostrar_tickets()
    
def ir_historial():
    ventana.destroy()
    historial_ventas.mostrar_historial()


class Ventana(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.nombre = StringVar()
        self.IdOrden = StringVar()
        self.cantidad = IntVar()
        self.cantidadTotal = 0
        self.total = 0
        

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=5)
        self.base_datos = CRUD_Ventas()

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

        Button(self.frame_titulo, text='REGRESAR', font = ('Arial', 9, 'bold'), command=salir_ventas, fg='black', bg = '#C3C3C3', width=20, bd=3).grid(column=0, row=0, pady=5)
        Button(self.frame_titulo, text='PRONOSTICO', font = ('Arial', 9, 'bold'), command=ir_pronostico, fg='black', bg = '#C3C3C3', width=20, bd=3).grid(column=2, row=0, pady=5)
        Button(self.frame_titulo, text='TICKETS', font = ('Arial', 9, 'bold'), command=ir_tickets, fg='black', bg = '#C3C3C3', width=20, bd=3).grid(column=3, row=0, pady=5)
        Button(self.frame_titulo, text='HISTORIAL VENTAS', font = ('Arial', 9, 'bold'), command=ir_historial, fg='black', bg = '#C3C3C3', width=20, bd=3).grid(column=4, row=0, pady=5)
        Label(self.frame_titulo, text= 'Ventas', bg='#E0E0E0', fg='black', font=('Kaufmann BT', 28, 'bold')).grid(columnspan=5, column=0, row=1, pady=5)

        Label(self.frame_uno, text= 'Opciones', bg='#E0E0E0', fg='black', font=('Kaufmann BT', 13, 'bold')).grid(column=2, row=0)

        Label(self.frame_uno, text= 'Datos', bg='#E0E0E0', fg='black', font=('Kaufmann BT', 13, 'bold')).grid(columnspan=2, column=0, row=0, pady=5)
        Label(self.frame_uno, text= 'Nombre Platillo', bg='#E0E0E0', fg='black', font=('Kaufmann BT', 13, 'bold')).grid(column=0, row=1, pady=5)
        Label(self.frame_uno, text= 'Cantidad', bg='#E0E0E0', fg='black', font=('Kaufmann BT', 13, 'bold')).grid(column=0, row=2, pady=5)

        self.etiquetaTotal = Label(self.frame_uno, text= 'Total a pagar: $', bg='white', fg='black', font=('Kaufmann BT', 18, 'bold'), bd=3, relief='groove', highlightbackground="black", highlightthickness=1, padx=5, pady=5)
        self.etiquetaTotal.grid(column=1, row=3, pady=5)

        Entry(self.frame_uno, textvariable=self.cantidad , font=('Kaufmann BT', 12), highlightbackground="black", highlightthickness=1).grid(column=1, row=2)

        datos = self.base_datos.valores_combo()
        opciones_platillo = datos
        self.combo_platillo = ttk.Combobox(self.frame_uno, values=opciones_platillo, font=('Kaufmann BT', 12))
        self.combo_platillo.set(opciones_platillo[0])
        self.combo_platillo.grid(row=1, column=1)
        self.nombre = self.combo_platillo.get()

        #BOTONES DE FUNCIONES DE LA DERECHA
        Button(self.frame_uno, text='AGREGAR A ORDEN', font= ('Arial', 9, 'bold'), bg= 'midnightblue', fg='white', width=20, bd=3, command=self.agregar_orden).grid(column=2, row=1, pady=5, padx=5)
        Button(self.frame_uno, text='LIMPIAR CAMPOS', font= ('Arial', 9, 'bold'), bg= 'midnightblue', fg='white', width=20, bd=3, command=self.limpiar_campos).grid(column=2, row=2, pady=5, padx=5)
        Button(self.frame_uno, text='FINALIZAR COMPRA', font= ('Arial', 9, 'bold'), bg= 'midnightblue',fg='white', width=20, bd=3, command=self.finalizar_compra).grid(column=2, row=3, pady=5, padx=5)

        estilo_tabla = ttk.Style()
        estilo_tabla.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black', background='#78A8F6')
        estilo_tabla.map('Treeview', background=[('selected', 'deep sky blue')], foreground=[('selected','black')] )
        estilo_tabla.configure('Heading', background='white', foreground='#357CF1', padding=3, font=('Arial', 10, 'bold'))

        self.tabla = ttk.Treeview(self.frame_dos)
        self.tabla.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_dos, orient = 'horizontal', command=self.tabla.xview)
        ladox.grid(column=0, row=1, sticky='ew')
        ladoy = ttk.Scrollbar(self.frame_dos, orient = 'vertical', command=self.tabla.yview)
        ladoy.grid(column=1, row=0, sticky='ns')
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        self.tabla['columns'] = ('Cantidad', 'PrecioUnitario', 'PrecioAgrupado')
        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Cantidad', minwidth=100, width=120, anchor='center')
        self.tabla.column('PrecioUnitario', minwidth=100, width=120, anchor='center')
        self.tabla.column('PrecioAgrupado', minwidth=100, width=105, anchor='center')

        self.tabla.heading('#0', text="Nombre", anchor='center')
        self.tabla.heading('Cantidad', text="Cantidad", anchor='center')
        self.tabla.heading('PrecioUnitario', text="PrecioUnitario", anchor='center')
        self.tabla.heading('PrecioAgrupado', text="PrecioAgrupado", anchor='center')

        self.tabla.bind("<Double-1>", self.eliminar_datos)


    
    def agregar_orden(self):
        if self.cantidad.get() <= 0 or self.cantidad.get() is None or self.cantidad.get() == "":
            messagebox.showerror("Cantidad", "Seleccione al menos la cantidad de 1")
        else:
            precio = self.obtenerPrecioUnitario(self.combo_platillo.get())
            cant = self.cantidad.get()
            precioAgrupado = precio * cant
            self.cantidadTotal = (self.cantidadTotal + cant)
            self.total = (self.total + precioAgrupado)
            self.etiquetaTotal.config(text='Total a pagar: ${}'.format(self.total),  bg='white', fg='black', font=('Kaufmann BT', 18, 'bold'), bd=3, relief='groove', highlightbackground="black", highlightthickness=1, padx=5, pady=5)       
            datos = [self.combo_platillo.get(), self.cantidad.get(), precio, precioAgrupado]
            print("Datos a insertar en la tabla:", datos)
            self.tabla.insert("", "end", values=datos)
            print("Valores en la tabla después de agregar:", self.tabla.item(self.tabla.get_children()[0], "values"))

    def obtenerPrecioUnitario(self, nombre):
        datos = self.base_datos.unitario(nombre)
        res = 1
        i= -1
        for dato in datos:
            i = i+1
            print(datos[i][1:2][0])
            res = datos[i][3:4][0]
        return res
    
    def finalizar_compra(self):
        self.limpiar_campos()
        cant = self.cantidadTotal
        tot = self.total
        fecha = str(strftime('%d-%m-%y %H:%M:%S'))
        self.base_datos.finalizar_compra(cant, tot, fecha)
        self.cantidadTotal = 0
        self.total = 0
        self.etiquetaTotal.config(text='Total a pagar: ${}'.format(self.total),  bg='white', fg='black', font=('Kaufmann BT', 18, 'bold'), bd=3, relief='groove', highlightbackground="black", highlightthickness=1, padx=5, pady=5)
        self.tabla.delete(*self.tabla.get_children())
        messagebox.showinfo("Compra Finalizada", "Compra realizada con éxito")
        self.generar_ticket()  # Llama a la función para generar el ticket después de finalizar la compra

    def obtener_fila(self,event):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        self.nombre.set(self.data['text'])
        self.check_var.set(self.data['values'][0])
        self.precio.set(self.data['values'][1])
        self.calorias.set(self.data['values'][2])

    def eliminar_datos(self,event):
        self.limpiar_campos()
        item = self.tabla.focus()
        seleccion = self.tabla.item(item, 'values')
        print("Fila seleccionada:", seleccion)
        item = self.tabla.selection()[0]
        x = messagebox.askquestion('Informacion', '¿Desea eliminar?')
        if x == 'yes' :
            self.tabla.delete(item)
            
            self.total = self.total - int(seleccion[2])
            self.etiquetaTotal.config(text='Total a pagar: ${}'.format(self.total),  bg='white', fg='black', font=('Kaufmann BT', 18, 'bold'), bd=3, relief='groove', highlightbackground="black", highlightthickness=1, padx=5, pady=5)
    
    def agregar_datos(self):
        nombre = self.nombre.get()
        disponibilidad = self.check_var.get()
        precio = self.precio.get()    
        calorias = self.calorias.get()
        datos = (disponibilidad, precio, calorias)
        if nombre and disponibilidad and precio and calorias !='':
            self.tabla.insert('', 0, text=nombre, values=datos)
            self.base_datos.insertar_datos(nombre, disponibilidad, precio, calorias)
            self.limpiar_campos()

    
    def actualizar_tabla(self):
        self.limpiar_campos()
        datos = self.base_datos.mostrar_datos()
        self.tabla.delete(*self.tabla.get_children())
        i= -1
        for dato in datos:
            i = i+1
            print(datos[i][1:2][0])
            print(datos[i][2:5])
            self.tabla.insert('',i,text = datos[i][1:2][0], values=datos[i][2:5])

    def actualizar_datos(self):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        nombre = self.data['text']
        datos = self.base_datos.mostrar_datos()
        for fila in datos:
            Id = fila[0]
            nombre_bd= fila[1]
            if nombre_bd == nombre:
                if Id != None:
                    nombre = self.nombre.get()
                    disponibilidad = self.check_var.get()
                    precio = self.precio.get()
                    calorias = self.calorias.get()
                    if nombre and precio and calorias != '':
                        self.base_datos.actualiza_datos(Id,nombre,disponibilidad,precio,calorias)
                        self.tabla.delete(*self.tabla.get_children())
                        datos = self.base_datos.mostrar_datos()
                        i = -1
                        for dato in datos:
                            i=i+1
                            self.tabla.insert('',i,text= datos[i][1:2][0], values=datos[i][2:5])
        self.limpiar_campos()


    def limpiar_campos(self):
        self.combo_platillo.current(0)
        self.cantidad.set('')

    def guardar_datos(self):
        self.limpiar_campos()
        datos = self.base_datos.mostrar_datos()
        i = -1
        nombre,disponibilidad,precio,calorias= [],[],[],[]
        for dato in datos:
            i=i+1
            nombre.append(datos[i][1])
            disponibilidad.append(datos[i][2])
            precio.append(datos[i][3])
            calorias.append(datos[i][4])
        fecha = str(strftime('%d-%m-%y_%H-%M-%S'))
        datos = {'Nombres':nombre, 'Disponibilidad':disponibilidad, 'Precio':precio, 'Calorias':calorias }
        df = pd.DataFrame(datos,columns= ['Nombres', 'Disponibilidad', 'Precio', 'Calorias'])
        df.to_excel((f'MENU {fecha}.xlsx'))
        messagebox.showinfo('Informacion', 'Datos guardados')

def mostrar_ventas():
    global ventana
    ventana = Tk()
    ventana.title('Ventas')
    ventana.minsize(height=400, width=600)
    ventana.geometry('800x500+250+100')
    # ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))
    app = Ventana(ventana)
    #app.actualizar_tabla()
    ventana.mainloop()

if __name__ == "__main__":
    mostrar_ventas()
