from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline('summarization')
    result = summarizer(text)
    return result[0]['summary_text']

# Example usage
text = 'Hugging Face is a company specializing in Natural Language Processing. They offer various models for text generation, translation, and more.'
print(summarize_text(text))
