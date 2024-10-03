import os
import shutil
import numpy as np

def split_data(source_folder, dest_folder, train_size=0.7, val_size=0.2, test_size=0.1):
    """
    Split the data into train, validation, and test sets.
    Args:
    source_folder (str): Path to the directory containing categorized images.
    dest_folder (str): Path to the directory where train, validation, test directories will be created.
    train_size (float): Proportion of the dataset to include in the train split.
    val_size (float): Proportion of the dataset to include in the validation split.
    test_size (float): Proportion of the dataset to include in the test split.
    """
    categories = [d for d in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, d))]
    for cat in categories:
        cat_dir = os.path.join(source_folder, cat)
        images = [f for f in os.listdir(cat_dir) if f.endswith(('.jpeg', '.jpg', '.png'))]
        np.random.shuffle(images)  # Shuffle the images

        # Calculate split sizes
        train_end = int(len(images) * train_size)
        val_end = train_end + int(len(images) * val_size)
        
        # Create directories for train, validation, test under each category
        train_dir = os.path.join(dest_folder, 'train', cat)
        val_dir = os.path.join(dest_folder, 'validation', cat)
        test_dir = os.path.join(dest_folder, 'test', cat)
        for d in [train_dir, val_dir, test_dir]:
            os.makedirs(d, exist_ok=True)
        
        # Copy images to respective directories
        image_sets = [images[:train_end], images[train_end:val_end], images[val_end:]]
        directories = [train_dir, val_dir, test_dir]
        for imgs, dir in zip(image_sets, directories):
            for img in imgs:
                shutil.copy(os.path.join(cat_dir, img), os.path.join(dir, img))
                print(f"Copied {img} to {dir}")

# Example usage
source_folder = "/Users/mohammedalqadda/PlantCare/PlantCareDataset"  # Update this path to your original images directory
dest_folder = "/Users/mohammedalqadda/PlantCare"  # Update this path to where you want the splits saved
split_data(source_folder, dest_folder)
