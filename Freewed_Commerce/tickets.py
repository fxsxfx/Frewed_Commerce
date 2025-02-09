import tkinter as tk
from tkinter import messagebox
import ventas  # Importa el módulo de ventas

def salir_tickets(root):
    root.destroy()
    ventas.mostrar_ventas()

class ProgramaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("OPTIFOOD - Ticket de Compra")
        
        self.productos = []
        self.precios = []
        self.cantidades = []
        
        self.create_widgets()
        
    def create_widgets(self):
        # Etiqueta y entrada para el producto
        self.lbl_producto = tk.Label(self.root, text="Producto:")
        self.lbl_producto.grid(row=0, column=0, padx=10, pady=5)
        self.txt_producto = tk.Entry(self.root)
        self.txt_producto.grid(row=0, column=1, padx=10, pady=5)
        
        # Etiqueta y entrada para la cantidad
        self.lbl_cantidad = tk.Label(self.root, text="Cantidad:")
        self.lbl_cantidad.grid(row=1, column=0, padx=10, pady=5)
        self.txt_cantidad = tk.Entry(self.root)
        self.txt_cantidad.grid(row=1, column=1, padx=10, pady=5)
        
        # Etiqueta y entrada para el precio
        self.lbl_precio = tk.Label(self.root, text="Precio:")
        self.lbl_precio.grid(row=2, column=0, padx=10, pady=5)
        self.txt_precio = tk.Entry(self.root)
        self.txt_precio.grid(row=2, column=1, padx=10, pady=5)
        
        # Botón para agregar producto
        self.btn_agregar = tk.Button(self.root, text="Agregar Producto", command=self.agregar_producto)
        self.btn_agregar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        # Lista para mostrar productos
        self.lst_productos = tk.Listbox(self.root)
        self.lst_productos.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        # Botón para generar ticket
        self.btn_generar_ticket = tk.Button(self.root, text="Generar Ticket", command=self.generar_ticket)
        self.btn_generar_ticket.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        # Botón para nuevo ticket
        self.btn_nuevo_ticket = tk.Button(self.root, text="Nuevo Ticket", command=self.nuevo_ticket)
        self.btn_nuevo_ticket.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        
        # Botón para salir a la ventana de ventas
        self.btn_salir = tk.Button(self.root, text="Salir", command=lambda: salir_tickets(self.root))
        self.btn_salir.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def agregar_producto(self):
        producto = self.txt_producto.get()
        try:
            precio = float(self.txt_precio.get())
            cantidad = int(self.txt_cantidad.get())
            if precio < 0:
                raise ValueError("El precio no puede ser negativo")
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a cero")
            
            self.productos.append(producto)
            self.precios.append(precio * cantidad)
            self.cantidades.append(cantidad)
            self.lst_productos.insert(tk.END, f"{producto} - {precio:.2f} x {cantidad} = {precio * cantidad:.2f}")
            
            self.txt_producto.delete(0, tk.END)
            self.txt_precio.delete(0, tk.END)
            self.txt_cantidad.delete(0, tk.END)
            self.txt_producto.focus()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un precio y una cantidad válidos.")
        
    def generar_ticket(self):
        total = sum(self.precios)
        
        # Encuentra el ancho máximo de cada columna
        max_ancho_producto = max(len(producto) for producto in self.productos + ["Producto"])
        max_ancho_precio = max(len(f"{precio/self.cantidades[i]:.2f}") for i, precio in enumerate(self.precios))
        max_ancho_cantidad = max(len(f"{cantidad}") for cantidad in self.cantidades + [0])
        max_ancho_total = max(len(f"{precio:.2f}") for precio in self.precios + [0.00])
        
        ticket = "----- OPTIFOOD -----\n"
        ticket += f"{'Producto':<{max_ancho_producto}} | {'Precio':<{max_ancho_precio}} | {'Cantidad':<{max_ancho_cantidad}} | {'Total':<{max_ancho_total}}\n"
        ticket += "-" * (max_ancho_producto + max_ancho_precio + max_ancho_cantidad + max_ancho_total + 9) + "\n"
        
        for i, (producto, precio, cantidad) in enumerate(zip(self.productos, self.precios, self.cantidades)):
            ticket += f"{producto:<{max_ancho_producto}} | {precio/cantidad:<{max_ancho_precio}.2f} | {cantidad:<{max_ancho_cantidad}} | {precio:<{max_ancho_total}.2f}\n"
        
        ticket += "-" * (max_ancho_producto + max_ancho_precio + max_ancho_cantidad + max_ancho_total + 9) + "\n"
        ticket += f"{'Total':<{max_ancho_producto}} | {'':<{max_ancho_precio}} | {'':<{max_ancho_cantidad}} | {total:<{max_ancho_total}.2f}\n"
        
        messagebox.showinfo("Ticket de Compra", ticket)
        
    def nuevo_ticket(self):
        # Limpiar listas y la lista visual de productos
        self.productos.clear()
        self.precios.clear()
        self.cantidades.clear()
        self.lst_productos.delete(0, tk.END)
        self.txt_producto.delete(0, tk.END)
        self.txt_precio.delete(0, tk.END)
        self.txt_cantidad.delete(0, tk.END)
        self.txt_producto.focus()
    
def mostrar_tickets():
    root = tk.Tk()
    app = ProgramaPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    mostrar_tickets()
