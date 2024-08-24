import torch
from diffusers import StableDiffusionPipeline


def text_to_image(prompt):
    model_id = "CompVis/stable-diffusion-v1-4"
    device = "cuda" if torch.cuda.is_available() else "cpu"

    pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=True)
    pipe = pipe.to(device)

    image = pipe(prompt).images[0]
    return image


if __name__ == "__main__":
    result = text_to_image('A beautiful sunset over the mountains.')
    result.save("output_image.png")
