from transformers import pipeline

def summarize_with_highlights(text):
    summarizer = pipeline('summarization')
    result = summarizer(text, min_length=30, max_length=80)
    summary = result[0]['summary_text']
    return summary

# Example usage
text = 'Hugging Face is known for its impressive suite of Natural Language Processing models. The company continues to lead in open-source AI development and provides various tools for machine learning.'
print(summarize_with_highlights(text))
