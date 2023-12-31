import numpy as np
import cv2
from feature_enhancement import GaussianBlurProcessor, EdgeEnhancementProcessor, ContrastStretchingProcessor

class SIFTFeatureDetector:
    def __init__(self):
        self.sift = cv2.xfeatures2d.SIFT_create()
        self.blur_processor = GaussianBlurProcessor()
        self.edge_processor = EdgeEnhancementProcessor()
        self.contrast_processor = ContrastStretchingProcessor()

    def detect_features(self, images):
        keypoints_list = []
        descriptors_list = []

        for image in images:
            image_copy = image.copy()
            gray = cv2.cvtColor(np.array(image_copy), cv2.COLOR_RGB2GRAY)
            blurred = self.blur_processor.process(gray)
            enhanced = self.edge_processor.process(blurred)
            stretched = self.contrast_processor.process(enhanced)
            keypoints, descriptors = self.sift.detectAndCompute(stretched, None)

        for keypoint in keypoints:
            y, x = keypoint.pt
            y, x = int(round(y)), int(round(x))
            keypoint.pt = (x, y)

            keypoints_list.append(keypoints)
            descriptors_list.append(descriptors)

        return keypoints_list, descriptors_list