from transformers import pipeline

def generate_story(prompt):
    story_generator = pipeline('text-generation', model='gpt-2')
    result = story_generator(prompt, max_length=200)
    return result[0]['generated_text']

# Example usage
print(generate_story('A brave knight sets out on a quest to find a hidden treasure.'))
