from transformers import pipeline

def translate_texts(texts, target_language='fr'):
    translator = pipeline(f'translation_en_to_{target_language}')
    translations = [translator(text)[0]['translation_text'] for text in texts]
    return translations

# Example usage
texts = ['Hello, how are you?', 'What is your name?']
print(translate_texts(texts, 'de'))
