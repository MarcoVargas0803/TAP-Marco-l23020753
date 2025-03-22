import customtkinter as ct
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración de apariencia
ct.set_appearance_mode("System")
ct.set_default_color_theme("blue")

# Configuración de correo
EMAIL_SENDER = "marcocontacto0803@gmail.com"
EMAIL_PASSWORD = "jovy sqrc ximy miuv"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # TLS

# Creación de la ventana principal
app = ct.CTk()
app.title("Correo")
app.geometry("450x700")
app.resizable(False, False)

# Configuración de columnas y filas
app.grid_columnconfigure(0, weight=1)
for i in range(3):
    app.grid_rowconfigure(i, weight=1)

# Creación de Frames
titulo = ct.CTkFrame(app, fg_color="black", border_width=2)
f1 = ct.CTkFrame(app, fg_color="black", border_width=2)
f2 = ct.CTkFrame(app, fg_color="black", border_width=2)
f3 = ct.CTkFrame(app, fg_color="black", border_width=2)
f4 = ct.CTkFrame(app, fg_color="black", border_width=2)

# Posicionamiento de los Frames
titulo.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
f1.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)
f2.grid(row=2, column=0, sticky="nsew", pady=5, padx=5)
f3.grid(row=3, column=0, sticky="nsew", pady=5, padx=5)
f4.grid(row=4, column=0, sticky="nsew", pady=5, padx=5)

# Labels
P_titulo = ct.CTkLabel(titulo, text="REGISTRO", text_color="White", anchor="w", font=("Arial", 50))
P1 = ct.CTkLabel(f1, text="To: ", text_color="Red", anchor="w")
P2 = ct.CTkLabel(f2, text="Subject", text_color="Red", anchor="w")

# Posicionamiento de Labels
P_titulo.pack(padx=10, pady=10)
P1.pack(side="left", padx=10, pady=10)
P2.pack(side="left", padx=10, pady=10)

# Entradas de texto
entrada_nombre = ct.CTkEntry(f1, width=40)  # Campo para destinatario
entrada_nombre.pack(padx=20, pady=5, fill="x", expand=True)

entrada_apellido = ct.CTkEntry(f2, width=40)  # Campo para asunto
entrada_apellido.pack(padx=20, pady=5, fill="x", expand=True)

# Scrollbar en f3
scrollbar = ct.CTkScrollbar(f3)
scrollbar.pack(side="right", fill="y")

text_box = ct.CTkTextbox(f3, height=100, wrap="word", yscrollcommand=scrollbar.set)
text_box.pack(padx=10, pady=10, fill="both", expand=True)
scrollbar.configure(command=text_box.yview)


# Slider en f4
def slider_callback(value):
    slider_label.configure(text=f"Nivel de urgencia: {int(value)}")


slider = ct.CTkSlider(f4, from_=0, to=100, command=slider_callback)
slider.pack(pady=10, padx=10, fill="x", expand=True)

slider_label = ct.CTkLabel(f4, text="Valor: 0")
slider_label.pack()


# Función para enviar correo
def enviar_correo():
    destinatario = entrada_nombre.get()
    asunto = entrada_apellido.get()
    mensaje = text_box.get("1.0", "end").strip()

    if not destinatario or not asunto or not mensaje:
        print("Error: Todos los campos deben estar llenos.")
        return

    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = destinatario
        msg["Subject"] = asunto
        msg.attach(MIMEText(mensaje, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, destinatario, msg.as_string())
        server.quit()

        print("Correo enviado con éxito.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")


# Botón para enviar el correo
btn_enviar = ct.CTkButton(f4, text="Enviar Correo", command=enviar_correo, fg_color="white", text_color="black",
                          hover_color="green")
btn_enviar.pack(pady=10)

# Ejecución de la ventana
app.mainloop()
