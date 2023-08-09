import numpy as np
import cv2
from PIL import Image
import torch
from torchvision.models.segmentation import deeplabv3_resnet101
from size_recognizer.ImageManager import ImageManager


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def countArea(self, point):
        return abs((point.x - self.x) * (point.y - self.y))


class PersonRecognizer:

    @staticmethod
    def __make_deeplab(device):
        deeplab = deeplabv3_resnet101(pretrained=True).to(device)
        deeplab.eval()
        return deeplab

    def __init__(self):
        self.device = torch.device("cpu")
        self.image_manager = ImageManager()
        self.deeplab = self.__make_deeplab(self.device)

    def __get_predictions(self, image_batch):
        with torch.no_grad():
            output = self.deeplab(image_batch)['out'][0]
        return output.argmax(0)

    def recognize_masked_image(self, image):
        image_batch = self.image_manager.get_image_batch(image)
        prediction = self.__get_predictions(image_batch)
        mask = Image.fromarray(prediction.byte().cpu().numpy()).resize(image.size)
        return np.array(mask)

    @staticmethod
    def __find_contours(masked_image):
        contours, _ = cv2.findContours(masked_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        return contours

    @staticmethod
    def __calculate_rectangle_around_contour(contour):

        if contour is None:
            return None, None

        x_top, y_top, width, height = cv2.boundingRect(contour)

        print(height)
        print(width)

        return Point(x_top, y_top), Point(x_top+width, y_top+height)

    # def __calculate_rectangle_area(self, contour):
    #     top, bottom = self.__calculate_rectangle_around_contour(contour)
    #     area = self.__calculate_area_of_rectangle(top, bottom)
    #     return area

    def __calculate_area_of_rectangle(self, top_point, bottom_point):
        return (bottom_point.x - top_point.x)*(bottom_point.y - top_point.y) if top_point is not None else 0

    # def __recenter_contour_on_image(self, contour, image) -> np.array:
    #     top_point, bottom_point = self.__calculate_rectangle_around_contour(contour)

    #     image_new = self.image_manager.get_new_black_image()

    #     if top_point is None:
    #         return image_new

    #     contour_x_center = (bottom_point.x + top_point.x) / 2
    #     contour_y_center = (bottom_point.y + top_point.y) / 2

    #     for i in range(len(contour)):
    #         contour[i][0][0] += image.size[0]/2 - contour_x_center
    #         contour[i][0][1] += image.size[1]/2 - contour_y_center

    #     image_new = cv2.drawContours(image_new, contour, -1, (255, 255, 0), 3)

    #     return image_new

    def __get_max_contour_on_image(self, image, masked_image):

        contours = self.__find_contours(masked_image)

        if contours is None:
            return None

        max_contour = contours[0]
        max_square = cv2.contourArea(max_contour)
        for contour in contours:
            if max_square < cv2.contourArea(contour):
                max_contour = contour
                max_square = cv2.contourArea(contour)

        return max_contour

    def get_mask_from_image(self, image):
        image_new = self.image_manager.prepare_image_for_prediction(image)
        return self.recognize_masked_image(image_new)

    # Returns contour on image
    # def get_person_on_photo(self, image):

    #     masked_image = self.get_mask_from_image(image)

    #     person_contour = self.__get_max_contour_on_image(image, masked_image)

    #     return person_contour

    # def get_black_image_with_contour(self, image, recenter: bool):
    #     image_contoured = self.image_manager.get_new_black_image()
    #     contour = self.get_person_on_photo(image)

    #     if contour is None:
    #         return image_contoured

    #     if recenter is True:
    #         image_contoured = self.__recenter_contour_on_image(contour, image)

    #     image_contoured = cv2.drawContours(image_contoured, contour, -1, (255, 255, 0), 3)

    #     return image_contoured

    def __find_max_contour_from_image(self, image):
        masked_image = self.get_mask_from_image(image)
        return self.__get_max_contour_on_image(image, masked_image)

    # def get_rectangle_of_person_from_photo(self, image):
    #     return self.__calculate_rectangle_around_contour(self.__find_max_contour_from_image(image))

    # def get_area_of_rectangle_of_person_from_photo(self, image):
    #     return self.__calculate_rectangle_area(self.__find_max_contour_from_image(image))

    def get_rectangle_from_photo_and_its_area(self, image):
        contour = self.__find_max_contour_from_image(image)
        top, bottom = self.__calculate_rectangle_around_contour(contour)
        return top, bottom , self.__calculate_area_of_rectangle(top, bottom)





