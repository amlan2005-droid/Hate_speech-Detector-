from googletrans import Translator

translator = Translator()

def translate_text(text):
    short_text = text[:300]

    translated = translator.translate(
        short_text,
        dest="en"
    )

    return translated.text
