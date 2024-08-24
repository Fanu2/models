from transformers import pipeline

def text_to_image_with_style(text, style):
    text2img = pipeline('text-to-image')
    img = text2img(text, style=style)
    img.save('output_styled_image.png')
    return 'output_styled_image.png'

# Example usage
print(text_to_image_with_style('A futuristic cityscape', 'cyberpunk'))
