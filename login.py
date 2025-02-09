from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import menu_principal

def signin():
    usuario=user.get()
    contra=contraseña.get()

    if usuario=='admin' and contra=='1234':
        root.destroy()
        menu_principal.mostrar_menuPrincpal()
        
    elif usuario!='admin' and contra!='1234':
        messagebox.showerror("Error", "Usuario y Contraseña incorrecto")

    elif usuario!='admin':
        messagebox.showerror("Error", "Usuario Incorrecto")

    elif contra!='1234':
        messagebox.showerror("Error","Contraseña Incorrecta")

def mostrar_login(): 

    global root,user,contraseña

    root=Tk()
    root.title('Login')
    root.geometry('800x500+250+100')
    root.configure(bg="#E0E0E0")
    root.resizable(False,False)

    encabezado=Label(root,text='Sistema Optifood',fg='black',bg='#E0E0E0',font=('Arial',30,'bold'))
    encabezado.place(x=410,y=10)

    frame1=Frame(root,width=350,height=800,bg='#B0B0B0')
    frame1.place(x=0,y=0)

    img= PhotoImage(file='imagenes/icon-login1.png')
    Label(frame1,image=img,bg='#B0B0B0').place(x=50,y=120)

    img_logo=Image.open('imagenes/logo.jpg').resize((100,100))
    logo= ImageTk.PhotoImage(img_logo)
    Label(frame1,image=logo,bg='#B0B0B0').place(x=0,y=0)

    frame=Frame(root,width=350,height=350,bg='#D0D0D0')
    frame.place(x=400,y=70)

    heading=Label(frame,text="Ingresa al sistema",fg='black',bg='#D0D0D0',font=('Arial',20,'bold'))
    heading.place(x=50,y=5)

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Usuario')

    user=Entry(frame,width=30,fg='black',border=2,bg='white',font=('Arial',11))
    user.place(x=50,y=100)
    user.insert(0,'Usuario')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    def on_enter(e):
        contraseña.delete(0, 'end')

    def on_leave(e):
        name=contraseña.get()
        if name=='':
            contraseña.insert(0,'Contraseña')

    contraseña=Entry(frame,width=30,fg='black',border=2,bg='white',font=('Arial',11),show='*')
    contraseña.place(x=50,y=180)
    contraseña.insert(0,'Contraseña')
    contraseña.bind('<FocusIn>', on_enter)
    contraseña.bind('<FocusOut>', on_leave)

    Button(frame,width=30,pady=7,text='Ingresar',bg='midnightblue',fg='white',font=('Arial', 12),border=5,command=signin).place(x=35,y=250)

    root.mainloop()