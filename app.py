from flask import Flask, render_template, request, redirect, url_for
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    languages = LANGUAGES
    return render_template('index.html', languages=languages)

@app.route('/translate', methods=['POST'])
def translate():
    text_to_translate = request.form['text']
    dest_language = request.form['language']
    translated = translator.translate(text_to_translate, dest=dest_language)
    return render_template('result.html', original=text_to_translate, translation=translated.text, dest_language=dest_language)

if __name__ == '__main__':
    app.run(debug=True)
