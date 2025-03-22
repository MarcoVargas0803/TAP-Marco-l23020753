from deep_translator import GoogleTranslator

class TranslateEngine(GoogleTranslator):
    def __init__(self):
        super().__init__()

        self.source_language = " "
        self.target_language = " "

    def convert_iso_lenguaje_format(self,entry):
        iso_dict = {
            "Español": "es",
            "Inglés": "en",
            "Portuguese": "pt",
            "Alemán": "de",
            "Ruso": "ru",
            "Francés": "fr",
            "Italiano": "it"
        }
        return iso_dict.get(entry,"auto") #Retorna "auto" si no encuentra el idioma
    def translate_text(self,entry,target,text):
        entry_iso = self.convert_iso_lenguaje_format(entry)
        target_iso = self.convert_iso_lenguaje_format(target)
        try:
            translator = GoogleTranslator(source=entry_iso,target=target_iso)
            traduccion = translator.translate(text)
            return traduccion
        except Exception as e:
            return f"No se pudo completar la traducción, {e}"

#Pruebas
app = TranslateEngine()
text1 = "Hello!"
target = "Español"
source = "Inglés"
translated_text = app.translate_text(source,target,text1)
print(translated_text)