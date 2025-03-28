from flask import Flask, request, render_template, jsonify
from googletrans import Translator
from models.translation_model import TranslationModel

app = Flask(__name__)
translator = Translator()
translation_model = TranslationModel(translator)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    target_language = data.get('target_language')
    if not text or not target_language:
        return jsonify({'error': 'Invalid input'}), 400
    translated_text = translation_model.translate(text, target_language)
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)