"""
Entendiendo el tearoff:
tearoff = 1 : línea punteada en la parte superior, y si el usuario hace clic en ella,
el submenú se "desprende" y se convierte en una ventana flotante separada.

tearoff = 0 : El submenú no se puede desprender, lo que da una apariencia más tradicional y fija.

"""

import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Menú Tearoff")

menu_bar = tk.Menu(root)

# Menú con tearoff habilitado (se puede desprender)
menu1 = tk.Menu(menu_bar, tearoff=1)
menu1.add_command(label="Opción 1")
menu1.add_command(label="Opción 2")

# Menú sin tearoff (no se puede desprender)
menu2 = tk.Menu(menu_bar, tearoff=0)
menu2.add_command(label="Opción A")
menu2.add_command(label="Opción B")

menu_bar.add_cascade(label="Menú 1 (tearoff=1)", menu=menu1)
menu_bar.add_cascade(label="Menú 2 (tearoff=0)", menu=menu2)

root.config(menu=menu_bar)
root.mainloop()
