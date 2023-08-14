import matplotlib.pyplot as plt
import sys, os

from size_recognizer.SizeRecognozer import *


if __name__ == "__main__":
    path = sys.argv[1]
    result_path = sys.argv[2]
    # photo_index = 4
    # path = f'/home/dggz/code/smart-mirror/size_recognizer/check_img/{photo_index}.jpg'
    # result_path = path.rsplit(os.sep, 1)[0] + '/result' + path.rsplit(os.sep, 1)[1]

    size_recognozer = SizeRecognizer()
    image = Image.open(path)

    image = size_recognozer.get_image_with_size(image)
    plt.imsave(result_path, image)
    