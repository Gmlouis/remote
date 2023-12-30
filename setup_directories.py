import os
from abc import abstractmethod

class DirectoryManager:
    @property
    @abstractmethod
    def input_directory(self):
        pass

    @property
    @abstractmethod
    def output_directory(self):
        pass

class DefaultDirectoryManager(DirectoryManager):
    def __init__(self, alt_directory=None):
        self.alt_directory = alt_directory

    @property
    def input_directory(self):
        return self.alt_directory if self.alt_directory else os.getcwd()

    @property
    def output_directory(self):
        new_images_dir = os.path.join(os.path.dirname(self.input_directory), 'New_images')
        if not os.path.exists(new_images_dir):
            os.makedirs(new_images_dir)
        return new_images_dir