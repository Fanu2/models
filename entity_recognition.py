from transformers import pipeline

def recognize_entities(text):
    ner_pipeline = pipeline('ner')
    result = ner_pipeline(text)
    return result

# Example usage
print(recognize_entities('Hugging Face is based in New York City.'))
