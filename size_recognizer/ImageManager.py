from torchvision import transforms
import numpy as np
from PIL import Image

class ImageManager:

    def __init__(self):
        self.preprocess = self.set_preprocess()
        self.image_height = 1280
        self.image_width = 961

    @staticmethod
    def set_preprocess():
        return transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def preprocess_image(self, image):
        return self.preprocess(image)

    def get_image_batch(self, image):
        copied_image = self.preprocess_image(image)
        return copied_image.unsqueeze(0)

    @staticmethod
    def convert_image_to_rgb(image):
        return image.convert("RGB")

    def resize_image(self, image):
        return image.resize()
    def prepare_image_for_prediction(self, image):
        return self.convert_image_to_rgb(image)

    def get_new_black_image(self):
        return np.array(Image.new(mode="RGB", size=(self.image_width, self.image_height), color=3))
