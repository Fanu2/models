from transformers import pipeline

def classify_text(text):
    classifier = pipeline('text-classification')
    result = classifier(text)
    return result

# Example usage
print(classify_text('I feel great today!'))
