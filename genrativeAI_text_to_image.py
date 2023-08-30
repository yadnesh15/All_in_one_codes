from huggingface_hub import notebook_login
notebook_login()

from diffusers import StableDiffusionPipeline
pipe=StableDiffusionPipeline.from_pretrained('runwayml/stable-diffusion-v1-5')

import torch

# Initialize a prompt
prompt = "A white cat rides a skateboard at night"
# Pass the prompt in the p
pipe(prompt).images[0]