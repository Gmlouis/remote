import cv2
import numpy as np

class SIFTFeatureDetector(feature_detection):
    def __init__(self):
        self.sift = cv2.xfeatures2d.SIFT_create()
        self.blur_processor = GaussianBlurProcessor()
        self.edge_processor = EdgeEnhancementProcessor()
        self.contrast_processor = ContrastStretchingProcessor()

    def detect_features(self, images):
        keypoints_list = []
        descriptors_list = []

        for image in images:
            gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
            blurred = self.blur_processor.process(gray)
            enhanced = self.edge_processor.process(blurred)
            stretched = self.contrast_processor.process(enhanced)
            keypoints, descriptors = self.sift.detectAndCompute(stretched, None)
            keypoints_list.append(keypoints)
            descriptors_list.append(descriptors)

        return keypoints_list, descriptors_list