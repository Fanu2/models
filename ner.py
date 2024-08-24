from transformers import pipeline

def named_entity_recognition(text):
    ner = pipeline('ner')
    result = ner(text)
    return result

# Example usage
text = 'Hugging Face is based in New York City.'
print(named_entity_recognition(text))
