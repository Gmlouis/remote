from setup_directories import DefaultDirectoryManager
from image_processing import DefaultImageProcessor
from image_creation import DefaultImageCreator

class Main:
    def __init__(self, alt_directory=None, bands=[1, 2, 3], additional_bands=[], resize_images=False, apply_filter=False, enhance_image=False):
        self.directory_manager = DefaultDirectoryManager(alt_directory)
        self.image_creator = DefaultImageCreator()
        self.image_processor = DefaultImageProcessor(self.directory_manager, self.image_creator, bands, additional_bands, resize_images, apply_filter, enhance_image)

    def run(self):
        self.image_processor.process_images()

if __name__ == "__main__":
    Main().run()