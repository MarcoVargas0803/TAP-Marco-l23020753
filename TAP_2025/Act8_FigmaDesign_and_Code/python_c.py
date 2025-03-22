import customtkinter as ctk
import threading

class TranslatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Traductor en Tiempo Real")
        self.geometry("500x400")

        # Selección de idiomas
        self.selectFirstLanguage = ctk.CTkComboBox(self, values=["es", "en", "fr", "de"])
        self.selectFirstLanguage.set("es")
        self.selectFirstLanguage.pack(pady=10)

        self.selectSecondLanguage = ctk.CTkComboBox(self, values=["es", "en", "fr", "de"])
        self.selectSecondLanguage.set("en")
        self.selectSecondLanguage.pack(pady=10)

        # Cuadro de texto donde el usuario escribe
        self.textboxFirstLanguage = ctk.CTkTextbox(self, width=400, height=100)
        self.textboxFirstLanguage.pack(pady=10)
        self.textboxFirstLanguage.bind("<KeyRelease>", self.on_keyrelease_translate)

        # Cuadro de texto donde aparece la traducción
        self.textboxSecondLanguage = ctk.CTkTextbox(self, width=400, height=100, state="disabled")
        self.textboxSecondLanguage.pack(pady=10)

        # Variable para evitar traducciones repetitivas con cada tecla presionada
        self.translation_pending = False

    def on_keyrelease_translate(self, event=None):
        """Espera un corto tiempo antes de traducir para no sobrecargar la API."""
        if not self.translation_pending:
            self.translation_pending = True
            self.after(500, self.perform_translation)  # Espera 500 ms antes de traducir

    def perform_translation(self):
        """Ejecuta la traducción en un hilo separado para no bloquear la GUI."""
        self.translation_pending = False  # Reseteamos la bandera
        thread = threading.Thread(target=self.translate_and_update, daemon=True)
        thread.start()

    def translate_and_update(self):
        """Obtiene el texto, lo traduce y actualiza la UI."""
        text_to_translate = self.textboxFirstLanguage.get("1.0", "end-1c").strip()
        if not text_to_translate:
            return  # No traducir si está vacío

        first_language_set = self.selectFirstLanguage.get()
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
        return text[::-1]  # Esto solo es un ejemplo, debes conectar con tu API real

    def update_translation_box(self, translated_text):
        """Actualiza el cuadro de texto de traducción."""
        self.textboxSecondLanguage.configure(state="normal")
        self.textboxSecondLanguage.delete("1.0", "end")
        self.textboxSecondLanguage.insert("1.0", translated_text)
        self.textboxSecondLanguage.configure(state="disabled")

# Ejecutar la aplicación
if __name__ == "__main__":
    app = TranslatorApp()
    app.mainloop()