import os
import zipfile
import shutil
from PIL import Image


def resize_image(input_image_path, output_image_path, size):
    with Image.open(input_image_path) as image:
        resized_image = image.resize(size)
        resized_image.save(output_image_path, bitmap_format="png")


# Example usage
input_path = input(
    "Enter the path for 1024 x 1024 image to generate android splash icons : "
)
target_sizes = [(288, 288), (432, 432), (576, 576), (864, 864), (1152, 1152)]
zip_file_path = f'{os.path.join(os.path.dirname(input_path), "android_splash.zip")}'

# Create a temporary directory to store resized images
temp_dir = f'{os.path.join(os.path.dirname(input_path), "temp")}'
os.makedirs(temp_dir, exist_ok=True)


def getName(i):
    if i == 0:
        return "drawable-mdpi"
    elif i == 1:
        return "drawable-hdpi"
    elif i == 2:
        return "drawable-xhdpi"
    elif i == 3:
        return "drawable-xxhdpi"
    else:
        return "drawable-xxxhdpi"


# Resize and save the images
for i, size in enumerate(target_sizes):
    folder_name = getName(i)
    folder_path = os.path.join(temp_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    output_path = os.path.join(folder_path, "splash.png")
    resize_image(input_path, output_path, size)

# Create a ZIP file and add the resized images
with zipfile.ZipFile(zip_file_path, "w") as zip_file:
    for root, _, files in os.walk(temp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            zip_file.write(file_path, os.path.relpath(file_path, temp_dir))

# Remove the temporary directory
shutil.rmtree(temp_dir)
