from PIL import Image
import sys

# Load the PNG image and convert it to JPEG format
image_path = sys.argv[1]
jpeg_image_path = sys.argv[2]

# Open the image and save it as JPEG
with Image.open(image_path) as img:
    img = img.convert("RGB")  # Ensure the image is in RGB mode for JPEG
    img.save(jpeg_image_path, format="JPEG")

jpeg_image_path
