import cv2
import numpy as np

def detect_features(self, images):
    keypoints_list = []
    descriptors_list = []

    for i, image in enumerate(images):
        image_copy = image.copy()
        gray = cv2.cvtColor(np.array(image_copy), cv2.COLOR_RGB2GRAY)
        blurred = self.blur_processor.process(gray)
        enhanced = self.edge_processor.process(blurred)
        stretched = self.contrast_processor.process(enhanced)
        keypoints, descriptors = self.sift.detectAndCompute(stretched, None)

        keypoints_list.append(keypoints)
        descriptors_list.append(descriptors)

        # Draw keypoints on the original image and replace it in the list
        images[i] = cv2.drawKeypoints(image, keypoints, outImage=np.array([]), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    return keypoints_list, descriptors_list