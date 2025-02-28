import customtkinter as ct

class ScrollableFrame(ct.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # Crear un Canvas dentro del Frame
        self.canvas = ct.CTkCanvas(self, width=450, height=250, bg="white")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Scrollbar para el Canvas
        self.scrollbar = ct.CTkScrollbar(self, command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Frame interno donde estarán los widgets
        self.inner_frame = ct.CTkFrame(self.canvas)
        self.window = self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Ajustar tamaño del Frame interno dinámicamente
        self.inner_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Agregar contenido al Frame
        for i in range(5):
            ct.CTkLabel(self.inner_frame, text=f"Prueba {i+1}", fg_color="gray",height=200,width=1470).pack(pady=5, padx=10, fill="x",expand=True)

app = ct.CTk()
app.geometry("500x300")
app.title("Frame con Scrollbar")

scroll_frame = ScrollableFrame(app)
scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

app.mainloop()