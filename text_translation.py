from transformers import pipeline

def translate_text(text, target_language='fr'):
    translator = pipeline('translation_en_to_fr' if target_language == 'fr' else 'translation_en_to_de')
    result = translator(text)
    return result[0]['translation_text']

# Example usage
print(translate_text('Hello, how are you?', 'fr'))
