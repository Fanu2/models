from transformers import pipeline

def detect_paraphrase(text1, text2):
    model_name = 'bert-base-uncased'
    model = pipeline('text-classification', model=model_name)
    result = model([text1, text2])
    return result

# Example usage
text1 = 'Hugging Face is a company specializing in NLP.'
text2 = 'Hugging Face focuses on natural language processing.'
print(detect_paraphrase(text1, text2))
