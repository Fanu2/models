from transformers import pipeline

def style_transfer(text, style):
    style_transfer_pipeline = pipeline('style-transfer')
    result = style_transfer_pipeline(text, style=style)
    return result[0]['text']

# Example usage
print(style_transfer('The quick brown fox jumps over the lazy dog.', 'poetic'))
