from transformers import pipeline

def generate_caption(image_path):
    caption_generator = pipeline('image-captioning')
    result = caption_generator(image_path)
    return result[0]['caption']

# Example usage
print(generate_caption('example_image.jpg'))
