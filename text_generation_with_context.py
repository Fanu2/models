from transformers import pipeline

def generate_text_with_context(prompt, context):
    generator = pipeline('text-generation', model='gpt2')
    result = generator(prompt + context, max_length=100)
    return result[0]['generated_text']

# Example usage
print(generate_text_with_context('Once upon a time', ' in a land far away'))
