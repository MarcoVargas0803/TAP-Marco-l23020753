import customtkinter as ct
class MainApp(ct.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Main Window")

        self.label = ct.CTkLabel(self, text="Ventana Principal", font=("Arial", 18))
        self.label.pack(pady=20)
