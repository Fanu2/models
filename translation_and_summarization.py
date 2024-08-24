from transformers import pipeline

def translate_and_summarize(text, target_language='fr'):
    translator = pipeline(f'translation_en_to_{target_language}')
    summarizer = pipeline('summarization')
    translated_text = translator(text)[0]['translation_text']
    summary = summarizer(translated_text)
    return summary[0]['summary_text']

# Example usage
text = 'Hugging Face has revolutionized Natural Language Processing with their state-of-the-art models and technologies.'
print(translate_and_summarize(text, 'es'))
