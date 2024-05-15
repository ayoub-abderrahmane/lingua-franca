from flask import Flask, request, jsonify
from google.cloud import translate

app = Flask(__name__)
translate_client = translate.TranslationServiceClient()

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text')
    target_lang = data.get('target_lang')

    # Utilisation de google-cloud-translate pour traduire le texte
    parent = f"projects/{project_id}"
    response = translate_client.translate_text(
        parent=parent,
        contents=[text],
        target_language_code=target_lang,
    )
    translated_text = response.translations[0].translated_text
    
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
