from transformers import pipeline

def generate_text(prompt):
    # Ensure to use the correct model identifier
    generator = pipeline('text-generation', model='gpt2')
    result = generator(prompt, max_length=50)
    return result[0]['generated_text']

if __name__ == "__main__":
    print(generate_text('Romantic  poem for Rosa'))
