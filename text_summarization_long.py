from transformers import pipeline

def summarize_long_text(text):
    summarizer = pipeline('summarization', model='facebook/bart-large-cnn')
    result = summarizer(text, max_length=150, min_length=50, length_penalty=2.0)
    return result[0]['summary_text']

# Example usage
text = 'Hugging Face provides state-of-the-art Natural Language Processing tools and technologies. They are pioneers in open-source machine learning and have various models available for developers and researchers.'
print(summarize_long_text(text))
