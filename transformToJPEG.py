from PIL import Image

# Load the PNG image or other extension
# and convert it to JPEG format
image_path = "image.webp"
jpeg_image_path = "newImage.jpeg"

# Open the image and save it as JPEG
with Image.open(image_path) as img:
    img = img.convert("RGB")  # Ensure the image is in RGB mode for JPEG
    img.save(jpeg_image_path, format="JPEG")

jpeg_image_path
