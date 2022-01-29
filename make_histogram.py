import numpy as np
from scipy.stats import entropy
import matplotlib.pyplot as plt


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