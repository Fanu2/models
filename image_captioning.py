from transformers import pipeline

def generate_caption(image_path):
    image_captioner = pipeline('image-captioning')
    result = image_captioner(image_path)
    return result[0]['caption']

# Example usage
print(generate_caption('example_image.jpg'))
