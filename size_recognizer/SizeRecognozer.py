from size_recognizer.PersonRecognizer import *

class SizeRecognizer:

    def __init__(self):

        self.pr = PersonRecognizer()
        self.height_koef = 5.54644
        self.width_koef = 5.71739
        self.sizes = {"XS": 5760,
             "S": 6357,
             "M": 7385,
             "L": 8037,
             "XL": 8785,
             "XXL": 9541,
             "XXXL": 1000000}

    def __recognise_size(self, area):
        for size, square_area in self.sizes.items():
            if square_area > area:
                return size

    def __reformat_area(self, area):
        return area / (self.height_koef * self.width_koef)

    # def __prepare_image(self, path):
    #     image = Image.open(path)
    #     return image.resize((self.pr.image_manager.image_width, self.pr.image_manager.image_height))

    def get_image_with_size(self, image):
        image = image.resize((self.pr.image_manager.image_width, self.pr.image_manager.image_height))
        # image = self.__prepare_image(path)
        point_top, point_bottom, area = self.pr.get_rectangle_from_photo_and_its_area(image)
        area = self.__reformat_area(area)
        size = self.__recognise_size(area)
        image = cv2.rectangle(np.array(image), (point_top.x, point_top.y), (point_bottom.x, point_bottom.y), (255, 255, 0), 2)
        image = cv2.putText(image, size, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 5)
        return image
