from transformers import pipeline

def translate_multiple_languages(text, target_language='fr'):
    translation_pipeline = pipeline(f'translation_en_to_{target_language}')
    result = translation_pipeline(text)
    return result[0]['translation_text']

# Example usage
print(translate_multiple_languages('Good morning!', 'es'))
