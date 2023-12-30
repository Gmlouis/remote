import rasterio
from abc import ABC, abstractmethod

class ImageCreator(ABC):
    @abstractmethod
    def create_image(self, bands_data, georeference, output_images):
        pass

class DefaultImageCreator(ImageCreator):
    def create_image(self, bands_data, georeference, output_images):
        with rasterio.open(output_images, 'w', **georeference) as new_image:
            new_image.write(bands_data)