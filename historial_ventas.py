import datetime
from tkinter import Tk, Button, Entry, Label, TkVersion, ttk
from tkinter import StringVar, Scrollbar, Frame, messagebox, DoubleVar, IntVar
import tkinter
from sql_ventas import CRUD_Ventas
from time import strftime
import pandas as pd
import ventas

def salir_historial():
    ventana.destroy()
    ventas.mostrar_ventas()

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
        self.frame_titulo = Frame(self.master, bg="#D29AFE", height=200, width=800)
        self.frame_titulo.grid(column=0, row=0, sticky='nsew')
        self.frame_dos = Frame(self.master, bg="#E6C5FF", height=300, width=800)
        self.frame_dos.grid(column=0, row=2, sticky='nsew')

        self.frame_titulo.columnconfigure([0,1,2,3,4], weight=1)
        self.frame_titulo.rowconfigure([0,1], weight=1)
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)

        Button(self.frame_titulo, text='REGRESAR', font = ('Arial', 9, 'bold'), command=salir_historial, fg='black', bg = '#C3C3C3', width=20, bd=3).grid(column=0, row=0, pady=5)
        Button(self.frame_titulo, text='EXPORTAR EXCEL', font = ('Arial', 9, 'bold'), command=self.guardar_datos, fg='black', bg = '#FEBD03', width=20, bd=3).grid(column=2, row=0, pady=5)
        Label(self.frame_titulo, text= 'Historial Ventas', bg='#D29AFE', fg='black', font=('Kaufmann BT', 28, 'bold')).grid(columnspan=5, column=0, row=1, pady=5)

       
        estilo_tabla = ttk.Style()
        estilo_tabla.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black', background='white')
        estilo_tabla.map('Treeview', background=[('selected', 'deep sky blue')], foreground=[('selected','black')] )
        estilo_tabla.configure('Heading', background='white', foreground='#357CF1', padding=3, font=('Arial', 10, 'bold'))

        self.tabla = ttk.Treeview(self.frame_dos)
        self.tabla.grid(column=0, row=0, sticky='nsew')
        ladox = ttk.Scrollbar(self.frame_dos, orient = 'horizontal', command=self.tabla.xview)
        ladox.grid(column=0, row=1, sticky='ew')
        ladoy = ttk.Scrollbar(self.frame_dos, orient = 'vertical', command=self.tabla.yview)
        ladoy.grid(column=1, row=0, sticky='ns')
        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        self.tabla['columns'] = ('Cantidad', 'Total', 'Fecha')
        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Cantidad', minwidth=100, width=120, anchor='center')
        self.tabla.column('Total', minwidth=100, width=120, anchor='center')
        self.tabla.column('Fecha', minwidth=100, width=105, anchor='center')

        self.tabla.heading('#0', text="Id Venta", anchor='center')
        self.tabla.heading('Cantidad', text="Cantidad", anchor='center')
        self.tabla.heading('Total', text="Total", anchor='center')
        self.tabla.heading('Fecha', text="Fecha", anchor='center')

        

    
    def actualizar_tabla(self):
        datos = self.base_datos.mostrar_datos()
        self.tabla.delete(*self.tabla.get_children())
        i= -1
        for dato in datos:
            i = i+1
            print(datos[i][0:1][0])
            print(datos[i][1:4])
            self.tabla.insert('',i,text = datos[i][0:1][0], values=datos[i][1:4])

    def guardar_datos(self):
        datos = self.base_datos.mostrar_datos()
        i = -1
        idVenta,cantidad,total,fecha= [],[],[],[]
        for dato in datos:
            i=i+1
            idVenta.append(datos[i][0])
            cantidad.append(datos[i][1])
            total.append(datos[i][2])
            fecha.append(datos[i][3])
        fecha = str(strftime('%d-%m-%y_%H-%M-%S'))
        datos = {'IdVenta':idVenta, 'Cantidad':cantidad, 'Total':total, 'Fecha':fecha }
        df = pd.DataFrame(datos,columns= ['IdVenta', 'Cantidad', 'Total', 'Fecha'])
        df.to_excel((f'REPORTE VENTAS {fecha}.xlsx'))
        messagebox.showinfo('Información', 'Datos guardados')


def mostrar_historial():
    global ventana
    ventana = Tk()
    ventana.title('Historial Ventas')
    ventana.minsize(height=400, width=600)
    ventana.geometry('800x500+250+100')
    # ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))
    app = Ventana(ventana)
    app.actualizar_tabla()
    ventana.mainloop()

if __name__ == "__main__":
    mostrar_historial()