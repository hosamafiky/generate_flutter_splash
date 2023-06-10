import os
import zipfile
import shutil
from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    with Image.open(input_image_path) as image:
        resized_image = image.resize(size)
        resized_image.save(output_image_path, bitmap_format='png')

# Example usage
input_path = input('Enter the path for 1024 x 1024 image to generate ios splash icons : ')
target_sizes = [(189, 207), (395, 413), (592, 619)]
zip_file_path = f'{os.path.join(os.path.dirname(input_path), "ios_splash.zip")}'

# Create a temporary directory to store resized images
temp_dir = f'{os.path.join(os.path.dirname(input_path), "temp")}'
os.makedirs(temp_dir, exist_ok=True)

# Resize and save the images
for i, size in enumerate(target_sizes):
    output_path = os.path.join(temp_dir, f'LaunchImage@{i+1}x.png' if i+1 != 1 else 'LaunchImage.png')
    resize_image(input_path, output_path, size)

# Create a ZIP file and add the resized images
with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
    for root, _, files in os.walk(temp_dir):
        for file in files:
            os.makedirs(temp_dir, exist_ok=True)
            file_path = os.path.join(root, file)
            zip_file.write(file_path, os.path.basename(file_path))

# Remove the temporary directory
shutil.rmtree(temp_dir)