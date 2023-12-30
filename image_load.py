import os
from PIL import Image

class ImageLoader:
    def __init__(self, directory_manager):
        self.directory_manager = directory_manager

    def load_images(self):
        rgb_images_dir = os.path.join(self.directory_manager.output_directory, 'RGB_images')
        image_files = [os.path.join(rgb_images_dir, file) 
                       for file in os.listdir(rgb_images_dir) 
                       if file.endswith('.tif')]
        images = [Image.open(file) for file in image_files]
        return images