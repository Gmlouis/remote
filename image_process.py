import os
import rasterio
from PIL import Image, ImageFilter, ImageEnhance
from abc import ABC, abstractmethod
import logging

class ImageProcessor(ABC):
    @abstractmethod
    def process_images(self):
        pass

class DefaultImageProcessor(ImageProcessor):
    def __init__(self, directory_manager, image_creator, bands=[1, 2, 3], additional_bands=[], resize_images=False, apply_filter=False, enhance_image=False):
        self.directory_manager = directory_manager
        self.image_creator = image_creator
        self.bands = bands
        self.additional_bands = additional_bands
        self.resize_images = resize_images
        self.apply_filter = apply_filter
        self.enhance_image = enhance_image

def process_images(self):
    input_images = [os.path.join(self.directory_manager.input_directory, file) for file in os.listdir(self.directory_manager.input_directory) if file.endswith('.tif')]
    for file in input_images:
        try:
            with rasterio.open(file) as HS_image:
                # Create RGB images
                bands_data = HS_image.read(self.bands)
                georeference = HS_image.profile
                georeference.update(count=len(self.bands))
                rgb_images_dir = os.path.join(self.directory_manager.output_directory, 'RGB_images')
                if not os.path.exists(rgb_images_dir):
                    os.makedirs(rgb_images_dir)
                output_images = os.path.join(rgb_images_dir, os.path.basename(file).replace(".tif", "_rgb.tif"))
                self.image_creator.create_image(bands_data, georeference, output_images)
                if self.resize_images:
                    self.resize_image(output_images)
                if self.apply_filter:
                    self.apply_filter(output_images)
                if self.enhance_image:
                    self.enhance_image(output_images)

                # Create additional single band images
                for band in self.additional_bands:
                    bands_data = HS_image.read(band)
                    georeference.update(count=1)
                    band_images_dir = os.path.join(self.directory_manager.output_directory, 'band_images')
                    if not os.path.exists(band_images_dir):
                        os.makedirs(band_images_dir)
                    output_images = os.path.join(band_images_dir, os.path.basename(file).replace(".tif", f"_band_{band}.tif"))
                    self.image_creator.create_image(bands_data, georeference, output_images)
                    if self.resize_images:
                        self.resize_image(output_images)
                    if self.apply_filter:
                        self.apply_filter(output_images)
                    if self.enhance_image:
                        self.enhance_image(output_images)
        except Exception as e:
            logging.error(f"An error occurred while processing {file}: {str(e)}", exc_info=True)

    class ImageResizeError(Exception):
        pass

    def resize_image(self, image_path, size=(256, 256)):
        try:
            img = Image.open(image_path)
            img = img.resize(size)
            img.save(image_path)
        except Exception as e:
            raise ImageResizeError(f"An error occurred while resizing {image_path}: {str(e)}")

    class ImageFilterError(Exception):
        pass

    def apply_filter(self, image_path):
        try:
            img = Image.open(image_path)
            img = img.filter(ImageFilter.FIND_EDGES)
            img.save(image_path)
        except Exception as e:
            raise ImageFilterError(f"An error occurred while applying filter to {image_path}: {str(e)}")

    class ImageEnhanceError(Exception):
        pass

    def enhance_image(self, image_path):
        try:
            img = Image.open(image_path)
            enhancer = ImageEnhance.Contrast(img)
            enhancer.enhance(1.5)
            img.save(image_path)
        except Exception as e:
            raise ImageEnhanceError(f"An error occurred while enhancing {image_path}: {str(e)}")