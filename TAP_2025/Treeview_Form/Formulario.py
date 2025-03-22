from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from db_script import DataBase
from datetime import datetime
import customtkinter as ct


class ControlMto(ct.CTk):


    def __init__(self):
        super().__init__()

        self.db1 = DataBase()
        self.title("Control de Mantenimiento")
        self.geometry("900x750")
        self.resizable(False, False)

        self.configurar_grid()
        self.crear_frames()
        self.crear_widgets()

    def configurar_grid(self):
        self.grid_columnconfigure(0, weight=1)
        for i in range(8):
            self.grid_rowconfigure(i, weight=1)

    def crear_frames(self):
        self.titulo = ct.CTkFrame(self, border_width=2)
        self.f1 = ct.CTkFrame(self, border_width=2)
        self.f2 = ct.CTkFrame(self, border_width=2)
        self.f3 = ct.CTkFrame(self, border_width=2)
        self.f4 = ct.CTkFrame(self, border_width=2)
        self.f5 = ct.CTkFrame(self, border_width=2)
        self.f6 = ct.CTkFrame(self, border_width=2)
        self.f7 = ct.CTkFrame(self, border_width=2)

        self.titulo.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
        self.f1.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
        self.f2.grid(row=2, column=0, sticky="nsew", pady=5, padx=5)
        self.f3.grid(row=3, column=0, sticky="nsew", pady=5, padx=5)
        self.f4.grid(row=4, column=0, sticky="nsew", pady=5, padx=5)
        self.f5.grid(row=5, column=0, sticky="nsew", pady=5, padx=5)
        self.f6.grid(row=6, column=0, sticky="nsew", pady=5, padx=5)
        #self.f7.grid(row=7, column=0, sticky="nsew", pady=5, padx=5)

    def crear_widgets(self):
        # Labels
        ct.CTkLabel(self.titulo, text="Control de Mantenimiento", text_color="White", font=("Helvetica", 25)).pack(padx=10, pady=10,side="left")
        ct.CTkLabel(self.f1, text="Nombre:", text_color="White").pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f2, text="Fecha:", text_color="White").pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f3, text="Clave:", text_color="White").pack(side="left", padx=10, pady=10)
        ct.CTkLabel(self.f4, text="Pago:", text_color="White").pack(side="left", padx=10, pady=10)

        # Entradas de texto
        self.entrada_nombre = ct.CTkEntry(self.f1,placeholder_text="Fulanito Alberto",width=400)
        self.entrada_nombre.pack(padx=20, pady=5, side="right")
        self.entrada_nombre.bind("<FocusIn>")

        self.entrada_fecha = ct.CTkEntry(self.f2, placeholder_text="07/03/25", width=400)
        self.entrada_fecha.pack(padx=20, pady=5, side="right")

        self.entrada_clave = ct.CTkEntry(self.f3, placeholder_text="OP001", show="", width=400)
        self.entrada_clave.pack(padx=20, pady=5, side="right")


        self.entrada_pago = ct.CTkEntry(self.f4, placeholder_text="$5000", width=400)
        self.entrada_pago.pack(padx=20, pady=5, side="right")



        #Buttons en f6

        self.button_send = ct.CTkButton(self.f5,text="Enviar",command=self.registrar_usuario,fg_color="#616362",hover_color="#84d658",text_color="black")
        self.button_send.pack(padx=10,pady=5,side="right")

        self.button_cancel = ct.CTkButton(self.f5,text="Cancelar",command=self.cancel,fg_color="#616362",hover_color="#d65858",text_color="black")
        self.button_cancel.pack(padx=10,pady=5,side="right")

        self.btn_modificar = ct.CTkButton(self.f5, text="Modificar", command=self.modificar_registro,fg_color="#616362",hover_color="#405c7c",text_color="black")
        self.btn_modificar.pack(padx=10, pady=5, side="right")

        self.btn_eliminar = ct.CTkButton(self.f5, text="Eliminar", command=self.eliminar_registro,fg_color="#616362",hover_color="#5c3a3f",text_color="black")
        self.btn_eliminar.pack(padx=10, pady=5, side="right")

        self.error_label = ct.CTkLabel(self.titulo,text=" ",font=("Helvetica",15),corner_radius=20)
        self.error_label.pack(side="right",padx=10,pady=10)

        # Barra de progreso (oculta al inicio)
        self.progress = ct.CTkProgressBar(self)
        self.progress.grid(row=8, column=0, padx=10, pady=10, sticky="ew")
        self.progress.set(0)  # Iniciar en 0

        # Style=Style()

        self.tv = Treeview(self.f6, columns=("Columna1", "Columna2","Columna3","Columna4"))
        # Style.configure("Treeview",rowheight=40)
        self.tv.heading("#0", text="No.")
        self.tv.heading("Columna1", text="Nombre")
        self.tv.heading("Columna2", text="Fecha")
        self.tv.heading("Columna3", text="Clave")
        self.tv.heading("Columna4", text="Pago")

        #Column tv configure
        self.tv.column("#0", width=2, minwidth=2, stretch=True)

        # tv.configure()
        self.tv.tag_configure('par', background='#302c2c', font=("Arial", 15),foreground="#4e585d")
        self.tv.tag_configure('impar', background='#28241c', font=("Arial", 15), foreground="#4e585d")

        self.tv.pack(side="top", fill="x", padx=5, pady=5)
        self.llenarTreeview()

        # Eventos bind
        self.entrada_nombre.bind("<FocusIn>", self.on_focus_in_name)
        self.entrada_nombre.bind("<FocusOut>", self.on_focus_out_name)
        self.entrada_fecha.bind("<FocusIn>", self.on_focus_in_fecha)
        self.entrada_fecha.bind("<FocusOut>", self.on_focus_out_fecha)
        self.entrada_pago.bind("<FocusIn>", self.on_focus_in_email)
        self.entrada_pago.bind("<FocusOut>", self.on_focus_out_email)
        self.entrada_clave.bind("<FocusIn>", self.on_focus_in_password)
        self.entrada_clave.bind("<FocusOut>", self.on_focus_out_password)

        self.bind("<Return>", self.registrar_usuario)
        self.bind("<Shift_L>", self.on_show_in_password)
        self.bind("<Shift_R>", self.on_show_in_password)

        self.entrada_nombre.bind("<KeyRelease>",self.validar_usuario)

        self.bind("<KeyRelease-Shift_L>", self.on_show_out_password)
        self.bind("<KeyRelease-Shift_R>", self.on_show_out_password)

        self.tv.bind("<ButtonRelease-1>", self.seleccionar_registro)

        self.bind("<Control-Return>",self.modificar_registro)

        # Configurar evento para el árbol (seleccionar fila)
        self.tv.bind("<<TreeviewSelect>>", self.on_item_select)

        # Configurar el evento para la tecla Supr
        self.bind("<Delete>", self.delete_record)

        self.selected_item = None

    def on_item_select(self, event):
        # Obtener el registro seleccionado
        selected_items = self.tv.selection()
        if selected_items:
            self.selected_item = selected_items[0]  # Guardamos el ID del item seleccionado

    def delete_record(self, event):
        # Verificar si hay un item seleccionado
        if self.selected_item:
            # Confirmar la eliminación
            confirm = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar este registro?")
            if confirm:
                # Eliminar el item
                self.tv.delete(self.selected_item)
                self.selected_item = None  # Restablecer la selección
                self.on_log_error_entry(message="Registro eliminado exitosamente")
        else:
            messagebox.showwarning("Advertencia", "Selecciona un registro primero.")

    def actualizar_treeview(self):
        for item in self.tv.get_children():
            self.tv.delete(item)

        users = self.db1.obtain_users()
        for index, item in enumerate(users, start=1):
            tag = "par" if index % 2 == 0 else "impar"
            self.tv.insert("", "end", text=index, values=(item[0], item[1], item[2], item[3]), tags=(tag,))
        self.progress.set(0)


    def cancel(self, event=None):
        self.entrada_nombre.delete(0, "end")

        self.entrada_fecha.delete(0, "end")

        self.entrada_clave.delete(0, "end")

        self.entrada_pago.delete(0, "end")

        self.on_log_error_entry(message="Registro actual cancelado")
        self.after(1500, self.hide_label)

    def llenarTreeview(self):
        users = self.db1.obtain_users()
        contador = 0
        for item in users:
            contador += 1
            if contador % 2 == 0:
                self.tv.insert("", END, text=contador, values=(item[0], item[1], item[2],item[3]), tags=("par",))
            else:
                self.tv.insert("", END, text=contador, values=(item[0], item[1],item[2],item[3]), tags=("impar",))
        return

    def seleccionar_registro(self, event):
        """Selecciona un registro del Treeview y lo muestra en los Entry"""
        item_seleccionado = self.tv.focus()  # Obtiene el ID del elemento seleccionado

        if item_seleccionado:
            valores = self.tv.item(item_seleccionado, "values")  # Obtiene los valores del registro
            if valores:
                self.entrada_nombre.delete(0, "end")
                self.entrada_nombre.insert(0, valores[0])

                self.entrada_fecha.delete(0, "end")
                self.entrada_fecha.insert(0, valores[1])

                self.entrada_clave.delete(0, "end")
                self.entrada_clave.insert(0, valores[2])

                self.entrada_pago.delete(0, "end")
                self.entrada_pago.insert(0, valores[3])
    def modificar_registro(self, event=None):
        """Modifica un registro seleccionado en la base de datos y lo actualiza en el Treeview"""
        item_seleccionado = self.tv.focus()

        if item_seleccionado:
            nuevo_nombre = self.entrada_nombre.get()
            nueva_fecha = self.entrada_fecha.get()
            nueva_clave = self.entrada_clave.get()
            nuevo_pago = self.entrada_pago.get()

            id_registro = self.tv.item(item_seleccionado, "text")  # Obtener el ID desde la columna #0

            if id_registro:  # Verificar si el ID es válido
                self.db1.refresh_table(id_registro, nuevo_nombre)  # Actualiza en la BD

                self.tv.item(item_seleccionado, text=id_registro,
                             values=(nuevo_nombre, nueva_fecha, nueva_clave, nuevo_pago))
                self.on_log_error_entry(message="Registro modificado exitosamente")
                self.after(1500, self.hide_label)

            else:
                self.on_log_error_entry(message="Error al modificar registro")
                self.after(1500, self.hide_label)

    def eliminar_registro(self):
        """Elimina un registro seleccionado del Treeview y de la base de datos"""
        item_seleccionado = self.tv.focus()

        if item_seleccionado:
            id_tree = self.tv.item(item_seleccionado, "text")
            id_registro = id_tree

            self.db1.eliminar_usuario(id_registro)  # Eliminar en la BD
            self.tv.delete(item_seleccionado)  # Eliminar en el Treeview
            self.on_log_error_entry(message="Registro eliminado exitosamente")
            self.after(1500, self.hide_label)


    def start_loading(self):
        """Inicia la simulación de carga al iniciar sesión"""
        self.progress.set(0)  # Reiniciar barra de progreso
        self.update_progress(0)  # Iniciar progreso


    def update_progress(self, value):
        """Simula el progreso y carga la nueva ventana"""
        if value < 1:
            value += 0.1  # Incremento del progreso
            self.progress.set(value)
            self.after(300, self.update_progress, value)  # Esperar 300ms y actualizar
        else:
            self.actualizar_treeview()  # Actualizar treeview

    def on_focus_in_fecha(self, event):
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.entrada_fecha.delete(0, "end")  # Elimina texto anterior
        self.entrada_fecha.insert(0, fecha_actual)  # Inserta la fecha y hora actual
        self.entrada_fecha.configure(text_color="white")
        self.error_label.configure(text="Fecha del registro", fg_color="#9197a1", text_color="black")
        self.after(1500, self.hide_label)

    def on_log_error_entry(self,text_color="white",message="Todos los campos son obligatorios.",fg_color="#d94b43"):
        self.error_label.configure(text=message,text_color=text_color,fg_color=fg_color,corner_radius=20)

    def hide_label(self):
        self.error_label.configure(text="",fg_color="transparent") # Oculta el Label


    def on_focus_in_name(self, e):
        self.entrada_nombre.configure(text_color="white")
        self.error_label.configure(text=" Nombre de pila ",fg_color="#9197a1",text_color="black")
        self.after(1500,self.hide_label)

    def on_focus_out_name(self, e):
        self.entrada_nombre.configure(text_color="gray")

    def on_focus_out_fecha(self, e):
        self.entrada_fecha.configure(text_color="gray")

    def on_focus_in_password(self, e):
        self.entrada_clave.configure(text_color="white")
        self.error_label.configure(text=" Almenos un caracter especial ",fg_color="#9197a1",text_color="black")
        self.after(1500,self.hide_label)


    def on_focus_out_password(self, e):
        self.entrada_clave.configure(text_color="gray")

    def on_show_in_password(self,event):
        self.entrada_clave.configure(show="")

    def on_show_out_password(self,event):
        self.entrada_clave.configure(show="*")

    def on_focus_in_email(self, e):
        self.entrada_pago.configure(text_color="white")
        self.error_label.configure(text=" Correo personal u institucional ",fg_color="#9197a1",text_color="black")
        self.after(1500,self.hide_label)


    def on_focus_out_email(self, e):
        self.entrada_pago.configure(text_color="gray")

    def validar_usuario(self, event=None):
        #Verificar en tiempo real si el usuario existe.
        user = self.entrada_nombre.get().strip()

        usuarios = self.db1.obtain_users()
        if any(user == u[0] for u in usuarios):
            self.error_label.configure(text="Usuario ya registrado", text_color="white",fg_color="#f04735")
        else:
            self.error_label.configure(text="Disponible para registrar", text_color="white",fg_color="green")


    def registrar_usuario(self,event=None):
        nombre = self.entrada_nombre.get()
        clave = self.entrada_clave.get()
        pago = self.entrada_pago.get()
        fecha = self.entrada_fecha.get()

        # Validaciones
        if not nombre or not fecha or not clave or not pago:
            self.on_log_error_entry(message="Todos los campos son obligatorios.")
            return

        # Verificar si el usuario ya existe en la base de datos

        if self.db1.user_exists(nombre):
            self.on_log_error_entry(message="El usuario ya existe.")
            self.after(1500, self.hide_label)
            return

        # Insertar usuario en la base de datos
        if self.db1.insert(nombre, fecha, clave, pago):
            self.on_log_error_entry(message=f"Usuario {nombre} registrado correctamente.", fg_color="#5ccc58")
            self.start_loading()
        else:
            self.on_log_error_entry(message="Error al registrar usuario")

app1 = ControlMto()
app1.mainloop()

