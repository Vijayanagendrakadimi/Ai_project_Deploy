from flask import Blueprint, request, jsonify
from app.models.translation_model import TranslationModel

translate_bp = Blueprint('translate', __name__)

@translate_bp.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get('text')
    target_language = data.get('target_language')

    if not text or not target_language:
        return jsonify({'error': 'Text and target language are required.'}), 400

    translation_model = TranslationModel()
    translated_text = translation_model.translate(text, target_language)

    return jsonify({'translated_text': translated_text})