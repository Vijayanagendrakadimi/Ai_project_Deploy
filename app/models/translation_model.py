class TranslationModel:
    def __init__(self, translator):
        self.translator = translator

    def translate(self, text, target_language):
        try:
            translated_text = self.translator.translate(text, dest=target_language)
            return translated_text.text
        except Exception as e:
            return str(e)