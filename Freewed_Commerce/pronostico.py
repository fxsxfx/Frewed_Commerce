import tkinter as tk
from tkinter import messagebox
import csv
import random
from datetime import datetime  # Importa el módulo datetime
import ventas

def salir_pronostico():
    root.destroy()
    ventas.mostrar_ventas()


class ProgramaPrincipal:
    def __init__(self, root, guisos):
        self.root = root
        self.root.title("Recomendaciones de guisos")

        self.guisos = guisos
        
        # Cambia el color de fondo de la ventana principal
        self.root.configure(bg="purple")

        # Creación del contenedor principal
        self.frame = tk.Frame(root, bg="#F4F4F4")  # Cambia el color de fondo
        self.frame.pack(padx=10, pady=10)

        # Mensaje de bienvenida con la fecha actual
        self.mostrar_mensaje_bienvenida()

        # Etiquetas y entradas
        self.label_nombre = tk.Label(self.frame, text="Nombre del guiso:", bg="#F4F4F4")  # Cambia el color de fondo
        self.label_nombre.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.entry_nombre = tk.Entry(self.frame)
        self.entry_nombre.grid(row=1, column=1, pady=5, padx=5)

        self.label_ventas = tk.Label(self.frame, text="Cantidad de ventas:", bg="#F4F4F4")  # Cambia el color de fondo
        self.label_ventas.grid(row=2, column=0, pady=5, padx=5, sticky="w")
        self.entry_ventas = tk.Entry(self.frame)
        self.entry_ventas.grid(row=2, column=1, pady=5, padx=5)

        self.label_perdidas = tk.Label(self.frame, text="Cantidad de pérdidas:", bg="#F4F4F4")  # Cambia el color de fondo
        self.label_perdidas.grid(row=3, column=0, pady=5, padx=5, sticky="w")
        self.entry_perdidas = tk.Entry(self.frame)
        self.entry_perdidas.grid(row=3, column=1, pady=5, padx=5)

        self.label_kg = tk.Label(self.frame, text="Cantidad de kg utilizados:", bg="#F4F4F4")  # Cambia el color de fondo
        self.label_kg.grid(row=4, column=0, pady=5, padx=5, sticky="w")
        self.entry_kg = tk.Entry(self.frame)
        self.entry_kg.grid(row=4, column=1, pady=5, padx=5)

        # Botones
        self.btn_agregar = tk.Button(self.frame, text="Agregar guiso", command=self.agregar_guiso, bg="#4CAF50", fg="white")  # Cambia el color de fondo y el color del texto
        self.btn_agregar.grid(row=5, column=0, columnspan=2, pady=10)

        self.btn_recomendaciones = tk.Button(self.frame, text="Mostrar recomendaciones", command=self.mostrar_recomendaciones, bg="#008CBA", fg="white")  # Cambia el color de fondo y el color del texto
        self.btn_recomendaciones.grid(row=6, column=0, columnspan=2, pady=10)

        self.btn_regresar = tk.Button(self.frame, text="Regresar", bg="gray", fg="white", command=salir_pronostico)  # Nuevo botón de regreso
        self.btn_regresar.grid(row=7, column=0, columnspan=2, pady=10)  # Ajusta el diseño del botón de regreso

        # Área de texto para recomendaciones
        self.recomendaciones_text = tk.Text(self.frame, height=10, width=40, bg="#E6E6E6", fg="#333")  # Cambia el color de fondo y el color del texto
        self.recomendaciones_text.grid(row=8, column=0, columnspan=2, pady=10)

    def mostrar_mensaje_bienvenida(self):
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        mensaje_bienvenida = f"Pronostico de Ventas Optifood\nFecha y hora: {fecha_actual}"
        self.label_bienvenida = tk.Label(self.frame, text=mensaje_bienvenida, bg="orange", fg="white", font=("Helvetica", 16))
        self.label_bienvenida.grid(row=0, column=0, columnspan=2, pady=10)

    def agregar_guiso(self):
        nombre_guiso = self.entry_nombre.get()
        ventas_guiso = self.entry_ventas.get()
        perdidas_guiso = self.entry_perdidas.get()
        kg_guiso = self.entry_kg.get()

        if not es_valor_numerico(ventas_guiso) or not es_valor_numerico(perdidas_guiso) or not es_valor_numerico(kg_guiso):
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos en las entradas correspondientes (nombre del guiso, ventas de guiso y pérdidas de guiso).")
            return

        ventas_guiso = int(ventas_guiso)
        perdidas_guiso = int(perdidas_guiso)
        kg_guiso = float(kg_guiso)

        self.guisos[nombre_guiso] = (ventas_guiso, perdidas_guiso, kg_guiso)

        # Llamada a la función para guardar los datos con la fecha
        guardar_datos(nombre_guiso, ventas_guiso, perdidas_guiso, kg_guiso)

        self.entry_nombre.delete(0, tk.END)
        self.entry_ventas.delete(0, tk.END)
        self.entry_perdidas.delete(0, tk.END)
        self.entry_kg.delete(0, tk.END)

        messagebox.showinfo("Éxito", "El guiso se agregó correctamente")

    def mostrar_recomendaciones(self):
        if not self.guisos:
            messagebox.showinfo("Guisos más demandados", "No hay guisos registrados.")
            return

        max_ventas = 0
        guisos_mas_demandados = []

        for guiso, (ventas, perdidas, kg) in self.guisos.items():
            if ventas > max_ventas:
                max_ventas = ventas

        for guiso, (ventas, perdidas, kg) in self.guisos.items():
            if ventas == max_ventas:
                guisos_mas_demandados.append((guiso, kg))

        messagebox.showinfo("Guisos más demandados", "\n".join([f"Nombre: {guiso}, Cantidad de kg utilizados: {kg}" for guiso, kg in guisos_mas_demandados]))

        porcentaje_agregado = 0
        self.recomendaciones_text.delete(1.0, tk.END)
        self.recomendaciones_text.insert(tk.END, "Recomendaciones para disminuir pérdidas:\n\n")
        for guiso, (ventas, perdidas, kg) in self.guisos.items():
            self.recomendaciones_text.insert(tk.END, f"Nombre: {guiso}\nVentas: {ventas}\nPérdidas: {perdidas}\nCantidad de kg utilizados: {kg}\n")
            valor_recomendado = kg + random.uniform(0, 1.5)
            porcentaje_agregado = ((valor_recomendado / kg) * 100) - 100
            if perdidas == 0:
                self.recomendaciones_text.insert(tk.END, "Estas cantidades utilizadas dan buen rendimiento\n\n")
            else:
                self.recomendaciones_text.insert(tk.END, f"Cantidad recomendada para disminuir pérdidas: {round(valor_recomendado, 2)}\n")
                self.recomendaciones_text.insert(tk.END, f"Un {round(porcentaje_agregado, 2)}% más de lo utilizado anteriormente\n\n")

# Nueva función para guardar los datos en un archivo CSV con la fecha y etiquetas
def guardar_datos(nombre_guiso, ventas, perdidas, kg):
    try:
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtiene la fecha y hora actual
        with open('datos_guisos.csv', 'a', newline='') as file:
            writer = csv.writer(file)

            # Agrega una fila con etiquetas para identificar cada columna si el archivo está vacío
            if file.tell() == 0:
                writer.writerow(["Fecha", "Nombre del guiso", "Ventas", "Pérdidas", "Cantidad de kg utilizados"])

            # Agrega los datos correspondientes
            writer.writerow([fecha_actual, nombre_guiso, ventas, perdidas, kg])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar los datos: {e}")

def es_valor_numerico(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def mostrar_pronostico():
    global root
    guisos={}
    root = tk.Tk()
    root.geometry('+450+100')
    ProgramaPrincipal(root, guisos)
    root.mainloop()

if __name__ == "__main__":
    mostrar_pronostico()

