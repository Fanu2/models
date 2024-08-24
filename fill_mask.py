from transformers import pipeline

def fill_mask(text):
    fill_masker = pipeline('fill-mask', model='bert-base-uncased')
    result = fill_masker(text)
    return result

# Example usage
print(fill_mask('Hugging Face is a [MASK] company.'))
