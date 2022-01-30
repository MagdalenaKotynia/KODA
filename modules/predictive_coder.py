import numpy as np
from PIL import Image
import PIL


def predictive_encode(image: PIL.Image, neighbour):
    img = np.asarray(image)

    if neighbour == 'upper':
        edge = np.zeros((1, img.shape[1]))
        zeros_lower = np.vstack((np.copy(img), edge))
        zeros_upper = np.vstack((edge, np.copy(img)))
        img_diff = np.subtract(zeros_lower, zeros_upper)[:-1]

    elif neighbour == 'left':
        edge = np.zeros((img.shape[0], 1))
        zeros_right = np.hstack((np.copy(img), edge))
        zeros_left = np.hstack((edge, np.copy(img)))
        img_diff = np.subtract(zeros_right, zeros_left)
        img_diff = np.delete(img_diff, -1, axis=1)

    elif neighbour == 'median':
        median_img = np.zeros((img.shape[0]+1, img.shape[1]+1))
        img_upper_edge = np.vstack((img[:1], img))
        img_left_upper_edge = np.hstack((img_upper_edge[:, [0]], img_upper_edge))
        for i in range(1, img.shape[0]+1):
            for j in range(1, img.shape[1]+1):
                median_img[i, j] = np.median(np.array([img_left_upper_edge[i-1, j], img_left_upper_edge[i, j-1], img_left_upper_edge[i-1, j-1]]))
        median_img = median_img[1:, 1:]
        img_diff = np.subtract(img, median_img)
        img_diff[0, 0] = img[0, 0] - 128

    else:
        raise ValueError('Nie ma takiej wartości dla argumentu neighbour. Możliwe wartości: upper, left, median')



    return img_diff


def predictive_decode(encoded: np.ndarray, neighbour):
    decoded = np.copy(encoded)
    nrows, ncols = encoded.shape
    if neighbour == 'upper':
        for i in range(1, nrows):
            decoded[i] += decoded[i-1]

    if neighbour == 'left':
        for i in range(1, ncols):
            decoded[:, i] += decoded[:, i-1]

    if neighbour == 'median':
        decoded[0, 0] = decoded[0, 0] + 128
        for j in range(1, ncols):
            decoded[0, j] = decoded[0, j] + decoded[0, j-1]
        for i in range(1, nrows):
            decoded[i, 0] = decoded[i, 0] + decoded[i-1, 0]
        for i in range(1, nrows):
            for j in range(1, ncols):
                decoded[i, j] = decoded[i, j] + np.median([decoded[i, j-1], decoded[i-1, j], decoded[i-1, j-1]])

    return decoded


def data2image(encoded: np.ndarray):
    img = Image.fromarray(encoded.astype('uint8'), 'L')
    return img


if __name__ == '__main__':
    from modules.data_generator import generate_image_uniform

    img = generate_image_uniform(img_size=(4, 4))

    img_diff_median = predictive_encode(img, 'median')
    img_decoded_median = predictive_decode(img_diff_median, 'median')

    print('Obraz oryginalny \n', np.asarray(img))
    print('Obraz różnicowy median \n', img_diff_median)
    print('Obraz zdekodowany median \n', img_decoded_median)

    img_diff_upper = predictive_encode(img, 'upper')
    img_decoded_upper = predictive_decode(img_diff_upper, 'upper')

    print('Obraz oryginalny \n', np.asarray(img))
    print('Obraz różnicowy upper \n', img_diff_upper)
    print('Obraz zdekodowany upper \n', img_decoded_upper)


    img_diff_left = predictive_encode(img, 'left')
    img_decoded_left = predictive_decode(img_diff_left, 'left')

    print('Obraz oryginalny \n', np.asarray(img))
    print('Obraz różnicowy left \n', img_diff_left)
    print('Obraz zdekodowany left \n', img_decoded_left)

    dog = Image.open('test_images/dog.png')
    dog.show()
    dog_diff = predictive_encode(dog, 'upper')
    dog_decoded = predictive_decode(dog_diff, 'upper')
    data2image(dog_decoded).show()

