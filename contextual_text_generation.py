from transformers import pipeline

def contextual_text_generation(prompt, context):
    generator = pipeline('text-generation', model='gpt-3')
    result = generator(prompt + context, max_length=150)
    return result[0]['generated_text']

# Example usage
print(contextual_text_generation('In a world where', ' technology advances rapidly, society changes dramatically.'))
