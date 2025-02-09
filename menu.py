from tkinter import Tk, Button, Entry, Label, TkVersion, ttk, PhotoImage
from tkinter import StringVar, Scrollbar, Frame, messagebox
import tkinter
from sql_menu import CRUD_Menu
from time import strftime
import pandas as pd
import menu_principal

def salir_menu():
    ventana.destroy()
    menu_principal.mostrar_menuPrincpal()


class Ventana(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.nombre = StringVar()
        self.disponibilidad = StringVar()
        self.precio = StringVar()
        self.calorias = StringVar()

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=5)
        self.base_datos = CRUD_Menu()

        self.widgets()

    def widgets(self):
        self.frame_titulo = Frame(self.master, bg="#357CF1", height=200, width=800)
        self.frame_titulo.grid(column=0, row=0, sticky='nsew')
        self.frame_uno = Frame(self.master, bg="#357CF1", height=200, width=800)
        self.frame_uno.grid(column=0, row=1, sticky='nsew')
        self.frame_dos = Frame(self.master, bg="#78A8F6", height=300, width=800)
        self.frame_dos.grid(column=0, row=2, sticky='nsew')

        self.frame_titulo.columnconfigure([0,1,2,3,4], weight=1)
        self.frame_titulo.rowconfigure([0,1], weight=1)
        self.frame_uno.columnconfigure([0,1,2], weight=1)
        self.frame_uno.rowconfigure([0,1,2,3,4,5], weight=1)
        self.frame_dos.columnconfigure(0, weight=1)
        self.frame_dos.rowconfigure(0, weight=1)

        Button(self.frame_titulo, text='REGRESAR', font = ('Arial', 9, 'bold'), command=salir_menu, fg='black', bg = '#C3C3C3', width=20, bd=3).grid(column=0, row=0, pady=5)
        Label(self.frame_titulo, text= 'Menú', bg='#357CF1', fg='black', font=('Kaufmann BT', 28, 'bold')).grid(columnspan=5, column=0, row=1, pady=5)

        Label(self.frame_uno, text= 'Opciones', bg='black', fg='white', font=('Kaufmann BT', 13, 'bold')).grid(column=2, row=0)
        Button(self.frame_uno, text='REFRESCAR', font = ('Arial', 9, 'bold'), command=self.actualizar_tabla, fg='black', bg = 'deep sky blue', width=20, bd=3).grid(column=2, row=1, pady=5)

        Label(self.frame_uno, text= 'Datos', bg='black', fg='white', font=('Kaufmann BT', 13, 'bold')).grid(columnspan=2, column=0, row=0, pady=5)
        Label(self.frame_uno, text= 'Nombre Platillo', bg='#357CF1', fg='black', font=('Rockwell', 13, 'bold')).grid(column=0, row=1, pady=5)
        Label(self.frame_uno, text= 'Precio', bg='#357CF1', fg='black', font=('Rockwell', 13, 'bold')).grid(column=0, row=2, pady=5)
        Label(self.frame_uno, text= 'Calorías', bg='#357CF1', fg='black', font=('Rockwell', 13, 'bold')).grid(column=0, row=3, pady=5)
        Label(self.frame_uno, text= 'Disponibilidad', bg='#357CF1', fg='black', font=('Rockwell', 13, 'bold')).grid(column=0, row=4, pady=5)

        Entry(self.frame_uno, textvariable=self.nombre , font=('Comic Sans MS', 12), highlightbackground="black", highlightthickness=1).grid(column=1, row=1)
        Entry(self.frame_uno, textvariable=self.precio , font=('Comic Sans MS', 12), highlightbackground="black", highlightthickness=1).grid(column=1, row=2)
        Entry(self.frame_uno, textvariable=self.calorias , font=('Comic Sans MS', 12), highlightbackground="black", highlightthickness=1).grid(column=1, row=3)
       
        self.check_var = tkinter.IntVar(value=1)
        self.checkbutton = ttk.Checkbutton(self.frame_uno, text="Disponible", variable=self.check_var).grid(column=1, row=4)
        # self.checkbutton.pack(pady=10)

        Button(self.frame_uno, text='AÑADIR A INVENTARIO', font= ('Arial', 9, 'bold'), bg= '#54FE2A', width=20, bd=3, command=self.agregar_datos).grid(column=2, row=2, pady=5, padx=5)
        Button(self.frame_uno, text='LIMPIAR CAMPOS', font= ('Arial', 9, 'bold'), bg= '#C3C3C3', width=20, bd=3, command=self.limpiar_campos).grid(column=2, row=3, pady=5, padx=5)
        Button(self.frame_uno, text='ACTUALIZAR DATOS', font= ('Arial', 9, 'bold'), bg= '#D133E7', width=20, bd=3, command=self.actualizar_datos).grid(column=2, row=4, pady=5, padx=5)
        Button(self.frame_uno, text='EXPORTAR A EXCEL', font= ('Arial', 9, 'bold'), bg= '#03BF00', width=20, bd=3, command=self.guardar_datos).grid(column=2, row=5, pady=5, padx=5)

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

        self.tabla['columns'] = ('Disponibilidad', 'Precio', 'Calorias')
        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Disponibilidad', minwidth=100, width=120, anchor='center')
        self.tabla.column('Precio', minwidth=100, width=120, anchor='center')
        self.tabla.column('Calorias', minwidth=100, width=105, anchor='center')

        self.tabla.heading('#0', text="Nombre", anchor='center')
        self.tabla.heading('Disponibilidad', text="Disponibilidad", anchor='center')
        self.tabla.heading('Precio', text="Precio", anchor='center')
        self.tabla.heading('Calorias', text="Calorias", anchor='center')

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)
        self.tabla.bind("<Double-1>", self.eliminar_datos)

    def obtener_fila(self,event):
        item = self.tabla.focus()
        self.data = self.tabla.item(item)
        self.nombre.set(self.data['text'])
        self.check_var.set(self.data['values'][0])
        self.precio.set(self.data['values'][1])
        self.calorias.set(self.data['values'][2])

    def eliminar_datos(self,event):
        self.limpiar_campos()
        item = self.tabla.selection()[0]
        x = messagebox.askquestion('Informacion', '¿Desea eliminar?')
        if x == 'yes' :
            self.tabla.delete(item)
            self.base_datos.elimina_datos(self.data['text'])

    
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
        self.nombre.set('')
        self.check_var.set(1)
        self.precio.set('')
        self.calorias.set('')

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

def mostrar_menu():
    global ventana
    ventana = Tk()
    ventana.title('Menú')
    ventana.minsize(height=400, width=600)
    ventana.geometry('800x500+250+100')
    # ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))
    app = Ventana(ventana)
    app.actualizar_tabla()
    ventana.mainloop()

if __name__ == "__main__":
    mostrar_menu()