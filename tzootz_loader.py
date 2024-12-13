"""
TZOOTZ RESEARCH
Advanced Mask & Denoise Loader with File Browser
Created by TZOOTZ RESEARCH LABS
"""

import os
import folder_paths
import numpy as np
from PIL import Image
import torch

class TzootzMaskLoader:
    """TZOOTZ RESEARCH: Advanced image loader with mask extraction and denoise control"""
    
    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {
            "required": {
                "image": (sorted(files), {"file_browser": True}),
                "feather_amount": ("FLOAT", {
                    "default": 0.0,
                    "min": 0.0,
                    "max": 1.0,
                    "step": 0.1
                }),
            },
        }
    
    RETURN_TYPES = ("IMAGE", "MASK", "FLOAT")
    RETURN_NAMES = ("image", "mask", "denoise_value")
    FUNCTION = "load_and_process"
    CATEGORY = "TZOOTZ RESEARCH"

    def load_and_process(self, image, feather_amount):
        # Construir la ruta completa usando el directorio de entrada de ComfyUI
        image_path = os.path.join(folder_paths.get_input_directory(), image)
        
        # Cargar imagen
        try:
            img = Image.open(image_path).convert('RGBA')
        except Exception as e:
            print(f"TZOOTZ Error loading image: {e}")
            # Crear una imagen vacía en caso de error
            img = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
        
        # Separar imagen y alpha
        rgb_image = img.convert('RGB')
        
        # Extraer máscara del canal alpha si existe, si no crear máscara negra
        if 'A' in img.getbands():
            mask = img.split()[3]
        else:
            mask = Image.new('L', img.size, 0)
        
        # Aplicar feather si se especifica
        if feather_amount > 0:
            from PIL import ImageFilter
            mask = mask.filter(ImageFilter.GaussianBlur(radius=feather_amount * 20))
        
        # Convertir a formato que espera ComfyUI
        rgb_tensor = torch.from_numpy(np.array(rgb_image)).float() / 255.0
        rgb_tensor = rgb_tensor.unsqueeze(0)
        
        mask_tensor = torch.from_numpy(np.array(mask)).float() / 255.0
        mask_tensor = mask_tensor.unsqueeze(0)
        
        # Calcular valor de denoise basado en la máscara
        denoise_value = float(mask_tensor.mean())
        
        return (rgb_tensor, mask_tensor, denoise_value)

# Registro del nodo con branding TZOOTZ
NODE_CLASS_MAPPINGS = {
    "TzootzMaskLoader": TzootzMaskLoader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TzootzMaskLoader": "TZOOTZ▲MASK"
}
