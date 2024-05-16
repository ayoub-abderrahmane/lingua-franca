from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def home():
    translated_text = ''
    detected_language = ''
    text_to_translate = ''
    #if the source language isn't specified , we use the automatic detection of language
    source_language = 'auto'
    target_language = 'en'

    if request.method == 'POST':
        text_to_translate = request.form['text_to_translate']
        source_language = request.form['source_language']
        target_language = request.form['target_language']

        if source_language == 'auto':
            detected_language = translator.detect(text_to_translate).lang
            source_language = detected_language

        translation = translator.translate(text_to_translate, src=source_language, dest=target_language)
        translated_text = translation.text

    return render_template('index.html', text_to_translate=text_to_translate, translated_text=translated_text, source_language=source_language, target_language=target_language, detected_language=detected_language)

if __name__ == '__main__':
    app.run(debug=True)
