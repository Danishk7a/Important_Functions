from rembg import remove
from PIL import Image

input_path = '/home/danish/Documents/Multi-Management/Uploads_to/mm.jpg'
output_path = 'output_image.png'

# Open the input image
input_image = Image.open(input_path)

# Remove the background with specific settings
output_image = remove(input_image, alpha_matting=True, alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=10, alpha_matting_erode_size=10)

# Save the output image
output_image.save(output_path)
