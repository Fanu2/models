from transformers import pipeline

def analyze_sentiment(text):
    sentiment_analyzer = pipeline('sentiment-analysis')
    result = sentiment_analyzer(text)
    return result

# Example usage
print(analyze_sentiment('I love using Hugging Face models!'))
