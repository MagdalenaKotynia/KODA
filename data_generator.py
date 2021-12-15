import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


_min_val = 0
_max_val = 255
_mean_val = (_max_val - _min_val)/2 + _min_val
_img_size = (512, 512)


def generate_image_uniform(min_val=_min_val, max_val=_max_val, img_size=_img_size):
    data = np.random.uniform(low=min_val, high=max_val+1, size=img_size)
    img = Image.fromarray(data.astype('uint8'), 'L')
    img.save('test_images/uniform.png')

    return img


def generate_image_normal(mi=_mean_val, sigma=0.2*_mean_val, img_size=_img_size):
    data = np.random.normal(loc=mi, scale=sigma, size=img_size)
    img = Image.fromarray(data.astype('uint8'), 'L')
    img.save('test_images/normal.png')

    return img


def generate_image_laplace(mi=_mean_val, b=0.2*_mean_val, img_size=_img_size):
    data = np.random.laplace(loc=mi, scale=b, size=img_size)
    img = Image.fromarray(data.astype('uint8'), 'L')
    img.save('test_images/laplace.png')

    return img


def save_test_images():
    generate_image_laplace().save('test_images/laplace.png')
    generate_image_normal().save('test_images/normal.png')
    generate_image_uniform().save('test_images/uniform.png')


def plot():
    laplace = Image.open('test_images/laplace.png')
    normal = Image.open('test_images/normal.png')
    uniform = Image.open('test_images/uniform.png')

    plt.subplot(2, 3, 1)
    plt.imshow(laplace, cmap='gray')
    plt.title('Rozkład Laplaca')
    plt.subplot(2, 3, 2)
    plt.imshow(normal, cmap='gray')
    plt.title('Rozkład normalny')
    plt.subplot(2, 3, 3)
    plt.imshow(uniform, cmap='gray')
    plt.title('Rozkład równomierny')
    plt.subplot(2, 3, 4)
    plt.plot(laplace.histogram())
    plt.subplot(2, 3, 5)
    plt.plot(normal.histogram())
    plt.subplot(2, 3, 6)
    plt.plot(uniform.histogram())
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    generate_image_normal
    generate_image_uniform()
    generate_image_laplace
    plot()


