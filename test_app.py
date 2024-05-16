from flask import Flask , request , render_template
from googletrans import Translator


app = Flask(__name__)


@app.route("/", methods=["GET","POST"])



def translateText():
    translator = Translator()

    #init of data
    data=request.form

    # Texte à traduire
    text_to_translate = data.get('text_to_translate')

    #text language
    source_language=data.get('source_language')

    # Langue cible
    target_language = data.get('target_language')

    if request.method == 'POST':
        if source_language=="auto":
            detected_language = translator.detect(text_to_translate).lang
            source_language = detected_language
       
        translation = translator.translate(text_to_translate, src=source_language, dest=target_language)
    
        # Texte traduit
        translated_text = translation.text

    return render_template('index.html', text_to_translate=text_to_translate, translated_text=translated_text, source_language=source_language, target_language=target_language)


if __name__ == '__main__':
    app.run(debug=True)
