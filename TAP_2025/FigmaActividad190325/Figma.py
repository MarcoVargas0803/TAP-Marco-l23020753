"""
##
#Figma : Diseñar una aplicación cualquiera que contenga:
·Dos botones
·Dos a tres entradas de datos
·Una imagen
·Una o dos etiquetas
·Una o dos funcionalidades

Es diseñarlo nadamàs, cuando se termine el diseño , se pasa al compañero para ser programado
y el que hayamos recibido, lo programamos.

en CTkinter hay que implementar la aplicaciòn.

"""

import customtkinter as ct
from PIL import Image
from abc import ABC, abstractmethod
from Translate_engine import TranslateEngine
import threading
ct.set_appearance_mode("light")  # default


class AbstractMainApp(ABC):

    @abstractmethod
    def configure_grid_main(self):
        pass

    @abstractmethod
    def frame_main_creation(self):
        pass

    @abstractmethod
    def progress_bar_creation(self):
        pass

    @abstractmethod
    def start_loading(self):
        pass

    @abstractmethod
    def update_progress(self, value):
        pass

    @abstractmethod
    def bind_creation(self):
        pass

class MainAppTraductor(ct.CTk,AbstractMainApp):
    def __init__(self):
        super().__init__()

        self.title("Google Traductor")
        self.geometry("850x450")
        self.resizable(False, False)
        #self.configure(fg_color="white")
        #self.set_appearance_mode("dark")
        #self.set_appearance_mode("light")

        self.translateEngine = TranslateEngine()
        self.configure_grid_main()
        self.configure_grid_title()
        self.frame_main_creation()
        self.imagen_title()
        self.imagen_reverse()
        self.progress_bar_creation()
        self.bind_creation()

        # Variable para evitar traducciones repetitivas con cada tecla presionada
        self.translation_pending = False


    def configure_grid_main(self):
        self.grid_rowconfigure(index=0,weight=0)
        self.grid_columnconfigure(index=(0,1,2),weight=1)
        self.grid_rowconfigure(index=(1,2,3),weight=1)

    def configure_grid_title(self):
        self.gridTitle = ct.CTkCanvas(self,bg="white")
        self.gridTitle.grid_columnconfigure(index=(0,1),weight=1)
        self.gridTitle.grid_rowconfigure(index=(0,1),weight=1)
        self.gridTitle.grid(column=0,row=0,sticky="nsew",columnspan=4)

    def imagen_title(self):
        try:
            image_login = ct.CTkImage(
                light_image=Image.open("google_t_logo.png"),
                dark_image=Image.open("google_t_logo.png"),
                size=(180, 90)
            )
        except FileNotFoundError:
            print("Imagen 'google_t_logo.png' no encontrada.")
            image_login = None

        image_label_traductor = ct.CTkLabel(self.gridTitle, image=image_login, text="")\
            if image_login else ct.CTkLabel(self.gridTitle,text="Sin imagen")

        image_label_traductor.grid(column=0,row=0,sticky="w",padx=10,pady=10)

    def imagen_reverse(self):
        try:
            self.image_reverse = ct.CTkImage(
                light_image=Image.open("reverse.png"),
                dark_image=Image.open("reverse.png"),
                size=(50, 50)
            )
        except FileNotFoundError:
            print("Imagen 'image_reverse' no encontrada.")
            self.image_reverse = None

        self.image_label_reverse = ct.CTkLabel(self, image=self.image_reverse, text="")\
            if self.image_reverse else ct.CTkLabel(self,text="Sin imagen")

        self.image_label_reverse.grid(column=2,row=2,sticky="w",padx=10,pady=10)

    def frame_main_creation(self):

        self.firstLanguageLabel = ct.CTkLabel(self,text="Selecciona el idioma de de entrada:",fg_color="lightgray",
                                        text_color="black",corner_radius=20,font=("Roboto",20))
        self.firstLanguageLabel.grid(column=0,row=1,sticky="ew",padx=25,pady=10)

        self.secondLanguageLabel = ct.CTkLabel(self, text="Selecciona el idioma de de entrada:", fg_color="lightgray",
                                        text_color="black", corner_radius=20, font=("Roboto", 20))
        self.secondLanguageLabel.grid(column=3, row=1, sticky="ew", padx=25,pady=10)

        self.list_languages = ["Español", "Inglés", "Portuguese", "Alemán", "Ruso", "Francés", "Italiano"]

        self.selectFirstLenguage = ct.CTkComboBox(self,fg_color="lightgray",values=self.list_languages,state="readonly",
                                                font=("Roboto",15),dropdown_font=("Roboto",15),dropdown_fg_color="white")

        self.selectFirstLenguage.grid(column=0,row=2,sticky="new",padx=40)
        
        self.selectSecondLanguage = ct.CTkComboBox(self, fg_color="lightgray", values=self.list_languages,state="readonly",
                                              font=("Roboto",15),dropdown_font=("Roboto",15),dropdown_fg_color="white")
        self.selectSecondLanguage.grid(column=3, row=2,sticky="new",padx=40)

        self.textboxFirstLanguage = ct.CTkTextbox(self,width=400,corner_radius=5,font=("Roboto",15),wrap="word")
        self.textboxFirstLanguage.grid(column=0,row=4,padx=5,pady=5)
        self.textboxFirstLanguage.insert("0.0","Ingresa el texto a traducir.. ")

        self.textboxSecondLanguage = ct.CTkTextbox(self, width=400, corner_radius=5,font=("Roboto",15),wrap="word",state="normal")
        self.textboxSecondLanguage.grid(column=3, row=4, padx=5, pady=5)
        self.textboxSecondLanguage.insert("0.0", " ")

    def delete_text_action(self):
        #Borrar texto anterior
        self.textboxSecondLanguage.delete("1.0","end")

    def delete_texts(self):
        self.textboxFirstLanguage.delete("1.0","end")
        self.textboxSecondLanguage.delete("1.0","end")

    def delete_comoboboxes(self):
        self.selectFirstLenguage.set("")
        self.selectSecondLanguage.set("")



    """def translate_text_action(self, event=None):
        try:
            text_to_translate = self.textboxFirstLanguage.get("1.0", "end-1c")
            first_language_set = self.selectFirstLenguage.get()
            second_language_set = self.selectSecondLanguage.get()

            if not text_to_translate.strip():
                return ""  # Evitar traducción vacía

            text_translated = self.translateEngine.translate_text(first_language_set, second_language_set,
                                                                  text_to_translate)
            return text_translated if text_translated else "Error en la traducción"

        except Exception as e:
            print(f"Error en la traducción: {e}")
            return "Error en la traducción"""

    def reverse_action(self): #Event button - 1
        firstText = self.textboxFirstLanguage.get("1.0","end-1c")
        secondText = self.textboxSecondLanguage.get("1.0","end-1c")

        firstcombotext = self.selectFirstLenguage.get()
        secondcombotext = self.selectSecondLanguage.get()

        self.delete_texts()

        self.textboxFirstLanguage.insert("1.0",secondText)
        self.textboxSecondLanguage.insert("1.0",firstText)

        self.delete_comoboboxes()

        self.selectFirstLenguage.set(secondcombotext)
        self.selectSecondLanguage.set(firstcombotext)

        self.on_keyrelease_translate()

    def progress_bar_creation(self):
        # Barra de progreso (oculta al inicio)
        self.progress = ct.CTkProgressBar(self, progress_color="#c999af")
        #self.progress.grid(column=0, row=4, padx=10, sticky="ew", columnspan=2)
        self.progress.set(0)  # Iniciar en 0

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
            return "carga realizada"

    def bind_creation(self):
        self.textboxFirstLanguage.bind("<Escape>",lambda e: self.on_focus_in_delete(self.textboxFirstLanguage))
        self.textboxSecondLanguage.bind("<Escape>",lambda e: self.on_focus_in_delete(self.textboxSecondLanguage))
        self.image_label_reverse.bind("<Enter>",lambda e: self.on_focus_in_label(self.image_label_reverse))
        self.image_label_reverse.bind("<Leave>",lambda e: self.on_focus_out_label(self.image_label_reverse))
        self.image_label_reverse.bind("<Button-1>",self.on_button_reverse)
        self.bind("<Return>", self.on_keyrelease_translate)

    def on_keyrelease_translate(self, event=None):
        print("probando")
        if not self.translation_pending:
            self.translation_pending = True
            self.after(100, self.perform_translation)  # Espera 500 ms antes de traducir

    def perform_translation(self):
        self.translation_pending = False  # Reseteamos la bandera
        thread = threading.Thread(target=self.translate_and_update, daemon=True)
        thread.start()

    def translate_and_update(self):
        text_to_translate = self.textboxFirstLanguage.get("1.0", "end-1c").strip()
        if not text_to_translate:
            return  # No traducir si está vacío

        first_language_set = self.selectFirstLenguage.get()
        second_language_set = self.selectSecondLanguage.get()

        try:
            # Llamada a la función de traducción
            text_translated = self.translate_text_action(first_language_set, second_language_set, text_to_translate)

            # Actualiza el textbox de forma segura en el hilo principal
            self.after(0, self.update_translation_box, text_translated)

        except Exception as e:
            print(f"Error en la traducción: {e}")

    def translate_text_action(self, from_lang, to_lang, text):
        """Simula la traducción (reemplaza esto con tu API de traducción)."""
        # Simulación de traducción: invierte el texto
        text_translated = self.translateEngine.translate_text(from_lang,to_lang,text)

        return text_translated

    def update_translation_box(self, translated_text):
        """Actualiza el cuadro de texto de traducción."""
        self.textboxSecondLanguage.configure(state="normal")
        self.textboxSecondLanguage.delete("1.0", "end")
        self.textboxSecondLanguage.insert("1.0", translated_text)
        self.textboxSecondLanguage.configure(state="disabled")

    def on_focus_in_delete(self,entry):
        entry.delete("1.0","end")

    def on_click_reverse(self,event):
        self.reverse_action()

    def on_focus_in_label(self,entry):
        entry.configure(fg_color="#737272")

    def on_focus_out_label(self,entry):
        entry.configure(fg_color="transparent")

    def on_button_reverse(self,event):
        self.reverse_action()
        print("hola probando")

App = MainAppTraductor()

if __name__ == '__main__':
    App.mainloop()
