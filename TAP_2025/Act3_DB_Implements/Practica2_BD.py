from tkinter import *
from tkinter.ttk import Treeview, Style
import customtkinter as ct
from customtkinter import CTkFrame, CTkLabel

"""
Este es un codigo de ejemplo de como poder obtener las tuplas de la base de datos e implementarlo 
en un lista de consulta en tkinter.

"""


usuarios = [("paquito","paquito123"),
            ("tribilin","tribilin123"),
            ("elbryan","elbryan123"),
            ("mariacarey","mariacarey123")
            ]

#def agregarUsuario(user,pad)

def llenarTreeview():
    contador = 0
    for item in usuarios:
        contador +=1
        if contador%2==0:
            tv.insert("",END,text=contador,values=(item[0],item[1]),tags=("par",))
        else:
            tv.insert("",END,text=contador,values=(item[0],item[1]),tags=("impar",))
    return

def mimetodo():
    print("Diste click")
    return

root = ct.CTk()
root.geometry("500x600")
header=CTkFrame(root,bg_color="cyan")
tvContainer=CTkFrame(root)
header.pack(fill=BOTH,expand=True)
tvContainer.pack(fill=BOTH,expand=True)

titulo = CTkLabel(header,bg_color="cyan",text=" R E G I S T R O S ",font=("Arial",20))
titulo.pack(padx=10)

#Style=Style()

tv=Treeview(tvContainer,columns=("Columna1","Columna2"))
#Style.configure("Treeview",rowheight=40)
tv.heading("#0",text="No.")
tv.heading("Columna1",text="Usuario")
tv.heading("Columna2",text="Password")
tv.column("#0",width=5,minwidth=5,stretch=True)
#tv.configure()
tv.tag_configure('par',background='lightyellow',font=("Arial",15))
tv.tag_configure('impar',background='lightgreen',font=("Arial",15),foreground="blue")

tv.pack(side="top",fill=X,padx=5,pady=5)
llenarTreeview()

root.mainloop()
