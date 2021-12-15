import numpy as np
from PIL import Image
import PIL
from data_generator import generate_image_uniform


def predictive_encode(image: PIL.Image, neighbour):
    img = np.asarray(image)
    print('Obraz oryginalny: ', img)
    if neighbour == 'upper':
        edge = np.zeros((1, img.shape[1]))
        zeros_lower = np.vstack((np.copy(img), edge))
        zeros_upper = np.vstack((edge, np.copy(img)))
        img_diff = np.subtract(zeros_lower, zeros_upper)[:-1]
        print('Obraz roznicowy: ', img_diff)

    if neighbour == 'left':
        edge = np.zeros((img.shape[0], 1))
        zeros_right = np.hstack((np.copy(img), edge))
        zeros_left = np.hstack((edge, np.copy(img)))
        img_diff = np.subtract(zeros_right, zeros_left)
        img_diff = np.delete(img_diff, -1, axis=1)
        print('Obraz roznicowy: ', img_diff)

    # if neighbour == 'median':
    #     edge = np.zeros((img.shape[0], 1))
    #     zeros_right = np.hstack((np.copy(img), edge))
    #     zeros_left = np.hstack((edge, np.copy(img)))
    #     img_diff = np.subtract(zeros_right, zeros_left)
    #     img_diff = np.delete(img_diff, -1, axis=1)
    #     print(img_diff)
    #     return img_diff


img = generate_image_uniform(img_size=(4, 4))

img_diff_upper = predictive_encode(img, 'upper')
img_diff_left = predictive_encode(img, 'left')

# dog = Image.open('test_images/dog.png')
# dog_diff = predictive_encode(dog, 'upper')
# dog_diff.show()

