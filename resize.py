import os
import pyheif
from PIL import Image

def resize_images_in_directory(directory, target_size=(256, 256)):
    """
    Resize all images in the specified directory to the target size.
    
    Args:
    directory (str): Directory containing images to resize.
    target_size (tuple): Desired (width, height) to resize images to.
    """
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpeg', '.jpg', '.png')):
            img_path = os.path.join(directory, filename)
            with Image.open(img_path) as img:
                # Resize the image
                img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
                # Save the resized image back to disk
                img_resized.save(img_path)
                print(f"Resized and saved {filename} at {img_path}")

def resize_all_categories(base_directory, target_size=(256, 256)):
    categories = ["Canna_indice_dead_leafs", "Canna_indice", "Egyptian_white_guava", "Noni_fruit"]
    for category in categories:
        directory = os.path.join(base_directory, category.replace(' ', '_'))
        print(f"Resizing images in {category} to {target_size}...")
        resize_images_in_directory(directory, target_size)
        print(f"Completed resizing images in {category}.")

# Example usage
base_directory = "/Users/mohammedalqadda/PlantCare/PlantCareDataset"  # Adjust this to your directory structure
resize_all_categories(base_directory, target_size=(256, 256))
