import numpy as np
from scipy.stats import entropy
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from predictive_encoder import predictive_encode

def get_histogram(data, values_range, show=False, output_file=None):
    hist, bins = np.histogram(data.flatten(), values_range[1] - values_range[0] + 1, values_range)

    if show or output_file is not None:
        x = range(values_range[0], values_range[1] + 1)
        plt.bar(x, hist, width=1.0, align='center')

    if output_file is not None:
        plt.savefig(output_file)

    if show:
        plt.show()

    plt.clf()

    return hist


def get_entropy(histogram):
    number_off_pixels = np.sum(histogram)
    probabilities = np.divide(histogram, number_off_pixels)
    return entropy(probabilities, base=2)


def get_image():
    images = {
        r"test_images/dog.png",
        #there you can put all testing files to get histogram and entropy test
    }
    return images


def histogram_entropy_test():
    for i in get_image():
        source_image = i
        image = cv.imread(source_image, cv.IMREAD_UNCHANGED)
        differential_image = predictive_encode(image, 'upper')
        histogram = get_histogram(differential_image, (-255, 255), True)
        entropy = get_entropy(histogram)
        print(histogram)
        print(entropy)


if __name__ == "__main__":
    histogram_entropy_test()
    
    
def get_avg_bit_len(bit_data):
    total = 0
    total_len = 0
    for row in bit_data:
        total_len += len(row)

    for row in bit_data:
        for word in row:
            total += len(word)
    avg_len = float(total) / float(total_len)
    return avg_len
