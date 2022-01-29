import cv2 as cv
import numpy as np
import differential_coding as dc
import make_histogram


def get_image():
    images = {
        r"test_images/barbara.pgm",
        r"test_images/boat.pgm",
        r"test_images/chronometer.pgm",
        r"test_images/lena.pgm",
        r"test_images/mandril.pgm",
        r"test_images/peppers.pgm",
    }
    return images


def histogram_entropy_test():
    for i in get_image():
        source_image = i
        image = cv.imread(source_image, cv.IMREAD_UNCHANGED)
        differential_image = dc.DifferentialEncoder.encode(image, 1)
        histogram = make_histogram.get_histogram(differential_image, (-255, 255), True)
        entropy = make_histogram.get_entropy(histogram)
        print(histogram)
        print(entropy)


if __name__ == "__main__":
    histogram_entropy_test()
