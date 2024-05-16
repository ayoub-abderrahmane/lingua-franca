from googletrans import Translator

translator=Translator()

translation = translator.translate("bonjour", src="fr" , dest="en")
hehea = translation.text

print(hehea)