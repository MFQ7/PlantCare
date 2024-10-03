import os
import pyheif
from PIL import Image

def heic_to_jpeg(heic_path, output_path, base_filename, start_index=1):
    """
    Convert HEIC files to JPEG, resize them, and save with a new name.

    Args:
    heic_path (str): Directory containing HEIC files.
    output_path (str): Directory to save JPEG files.
    base_filename (str): Base name for saving new files.
    start_index (int): Starting index for naming files.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    files = [f for f in os.listdir(heic_path) if f.lower().endswith('.heic')]
    index = start_index

    for file in files:
        try:
            # Full path to the HEIC file
            file_path = os.path.join(heic_path, file)
            # Read the HEIC file
            heif_file = pyheif.read(file_path)
            # Convert to an Image object
            image = Image.frombytes(
                heif_file.mode,
                heif_file.size,
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
            )
            # Construct the new file name
            new_filename = f"{base_filename}_{index}.jpeg"
            full_output_path = os.path.join(output_path, new_filename)
            # Save the image as JPEG
            image.save(full_output_path, "JPEG")
            print(f"Converted and saved {file} as {new_filename}")
            index += 1
        except Exception as e:
            print(f"Failed to process {file}: {str(e)}")

def convert_all_folders(base_directory, output_directory):
    # List all subdirectories to process each category
    categories = ["Canna Indice Dead Leafs", "Canna Indice", "Egyptian White Guava", "Noni Fruit"]
    for category in categories:
        heic_dir = os.path.join(base_directory, category)
        output_dir = os.path.join(output_directory, category.replace(' ', '_'))
        base_filename = category.replace(' ', '_')
        heic_to_jpeg(heic_dir, output_dir, base_filename)

# Example usage: update these paths as needed
base_directory = "/Users/mohammedalqadda/Senior Project Pics"  # Update this path to your base directory
output_directory = "/Users/mohammedalqadda/PlantCare/H2J Data" # Update to where you want the JPEGs saved
convert_all_folders(base_directory, output_directory)
