#Diseñar una clase Login, donde podamos instanciar las ventanas de login que queramos y podamos
#Pasar: Foto , fondo , textos:
#from PIL import Image
import customtkinter as ct

from PIL import Image

my_image = ct.CTkImage(light_image=Image.open("<path to light mode image>"),
                                  dark_image=Image.open("<path to dark mode image>"),
                                  size=(30, 30))

image_label = ct.CTkLabel(app, image=my_image, text="")  # display image with a CTkLabel

class Login:
    text_entry_name = "usuario"
    text_entry_password = "contraseña"
    text_entry_button_login = "iniciar sesión"
    text_entry_button_cancel = "cancelar"

    def __init__(self,text_entry_name,text_entry_password,text_entry_button_login,text_entry_button_cancel):
        self.app = ct.CTk()
        self.text_entry_name = text_entry_name
        self.text_entry_password = text_entry_password
        self.text_entry_button_login = text_entry_button_login
        self.text_entry_button_cancel = text_entry_button_cancel
        self.check_var1 = ct.IntVar()

        self.app.title("Login")

        # Tamaño y configuración de la ventana
        self.app.geometry("900x450")
        self.app.resizable(False, False)

        # Configuración de apariencia
        ct.set_appearance_mode("System")
        ct.set_default_color_theme("blue")

    def init_window(self):

        # Configuración de columnas y filas
        self.app.grid_columnconfigure(0, weight=1)
        for i in range(5):
            self.app.grid_rowconfigure(i, weight=1)

    def frame_creation(self):
        # Creación de Frames
        titulo = ct.CTkFrame(self.app, fg_color="gray", border_width=2)
        self.titulo = titulo
        f1 = ct.CTkFrame(self.app, fg_color="gray", height=100, width=200, border_width=2)
        f2 = ct.CTkFrame(self.app, fg_color="gray", border_width=2)
        f3 = ct.CTkFrame(self.app, fg_color="gray", border_width=2)
        f4 = ct.CTkFrame(self.app, fg_color="gray", border_width=2)
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.f4 = f4
        # Posicionamiento de los Frames
        titulo.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
        f1.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
        f2.grid(row=2, column=0, sticky="nsew", pady=5, padx=5)
        f3.grid(row=3, column=0, sticky="nsew", pady=5, padx=5)
        f4.grid(row=4, column=0, sticky="nsew", pady=5, padx=5)
    def labels_creation(self):
        P_titulo = ct.CTkLabel(self.titulo, text="Login", text_color="Red", anchor="w", font=("Arial", 50))

        # Posicionamiento de Labels
        P_titulo.pack(padx=10, pady=10, side="left")
    def entry_creation(self):
        entrada_usuario = ct.CTkEntry(self.f1, width=40, placeholder_text=self.text_entry_name)
        self.entrada_usuario = entrada_usuario
        entrada_usuario.pack(padx=20, pady=5, fill="x", expand=True)

        entrada_contra = ct.CTkEntry(self.f2, width=40, placeholder_text=self.text_entry_password)
        self.entrada_contra = entrada_contra
        entrada_contra.pack(padx=20, pady=5, fill="x", expand=True)

    def button_creation(self):
        login_botton = ct.CTkButton(self.f3, text=self.text_entry_button_login, fg_color="white", text_color="black", hover_color="grey",
                                    command=self.submit)
        login_botton.pack(padx=5, pady=5, side="left")

        cancel_botton = ct.CTkButton(self.f3, text=self.text_entry_button_cancel, fg_color="white", text_color="black", hover_color="grey",command=self.app.destroy)
        cancel_botton.pack(padx=5, pady=5, side="left")
    def checkbox_creation(self):
        checkbox4_1 = ct.CTkCheckBox(self.f4, text="Recordarme", variable=self.check_var1)
        checkbox4_1.pack(side="left", padx=20)

    def submit(self):
        nombre = self.entrada_usuario.get()
        apellido = self.entrada_contra.get()
        pertenece_a = []

        if self.check_var1.get():
            pertenece_a.append("Recordarme")

        print(f"Nombre: {nombre}")
        print(f"Apellido: {apellido}")

    def ejecution(self):
        self.init_window()
        self.frame_creation()
        self.labels_creation()
        self.entry_creation()
        self.button_creation()
        self.checkbox_creation()
        self.app.mainloop()

ventana1 = Login("user","password","login","quit")
ventana1.ejecution()


