import json
import os
from PIL import Image

# 1. Compress images to WebP
os.makedirs("assets/slides_webp", exist_ok=True)
for i in range(1, 51):
    src = f"assets/slides/slide_{i:02d}.png"
    dst = f"assets/slides_webp/slide_{i:02d}.webp"
    if os.path.exists(src):
        try:
            im = Image.open(src)
            im.save(dst, "WEBP", quality=82, method=6)
        except Exception as e:
            print(f"Error converting slide {i}: {e}")

print("Converted all slides to webp.")
