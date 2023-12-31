import cv2
import numpy as np

class GaussianBlurProcessor:
    def __init__(self, kernel_size=3, sigma=0.5):
        self.kernel_size = kernel_size
        self.sigma = sigma

    def process(self, image):
        return cv2.GaussianBlur(image, (self.kernel_size, self.kernel_size), self.sigma)

class EdgeEnhancementProcessor:
    def __init__(self, kernel_size=3):
        self.kernel_size = kernel_size

    def process(self, image):
        laplacian = cv2.Laplacian(image, cv2.CV_64F)
        sharpened = cv2.addWeighted(image, 1.5, laplacian, -0.5, 0)
        return sharpened

class ContrastStretchingProcessor:
    def __init__(self, lower_percentile=10, upper_percentile=90):
        self.lower_percentile = lower_percentile
        self.upper_percentile = upper_percentile

    def process(self, image):
        lower = np.percentile(image, self.lower_percentile)
        upper = np.percentile(image, self.upper_percentile)
        stretched = cv2.normalize(image, None, lower, upper, cv2.NORM_MINMAX)
        return stretched