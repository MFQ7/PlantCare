import os
from PIL import Image

def check_image_sizes_and_average(directory):
    """
    Check the sizes of all images in a directory and calculate the average size.
    
    Args:
    directory (str): The directory containing the images to check.
    
    Returns:
    bool: True if all images are the same size, False otherwise.
    tuple: The average width and height of the images.
    """
    widths = []
    heights = []
    same_size = True
    first_size = None

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpeg', '.jpg', '.png')):  # check for image files
            img_path = os.path.join(directory, filename)
            with Image.open(img_path) as img:
                size = img.size
                widths.append(size[0])
                heights.append(size[1])
                if first_size is None:
                    first_size = size
                elif first_size != size:
                    same_size = False

    # Calculate average size
    average_width = sum(widths) / len(widths) if widths else 0
    average_height = sum(heights) / len(heights) if heights else 0
    average_size = (average_width, average_height)

    return same_size, average_size

def check_all_folders(base_directory):
    categories = ["Canna_indice_dead_leafs", "Canna_indice", "Egyptian_white_guava", "Noni_fruit"]
    results = {}
    for category in categories:
        directory = os.path.join(base_directory, category)
        same_size, average_size = check_image_sizes_and_average(directory)
        results[category] = {'Same Size': same_size, 'Average Size': average_size}
        print(f"{category}: Same Size - {same_size}, Average Size - {average_size}")
    return results

# Example usage
base_directory = "/Users/mohammedalqadda/PlantCare/PlantCareDataset"  # Update this path to where your JPEGs are saved
check_all_folders(base_directory)
