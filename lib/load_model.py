from diffusers import DiffusionPipeline
import torch


def load_nn_model(model_path_or_url, device="cuda"):
    pipe = DiffusionPipeline.from_pretrained(model_path_or_url, torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
    pipe.to(device)
    return pipe


def generate_image(prompt,model):
    return model(prompt=prompt).images[0]