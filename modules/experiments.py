import numpy as np
import sys
import PIL
import matplotlib.pyplot as plt
from PIL import Image as im
import predictive_coder as pc
import modules.data_generator as gen
import huffman_codec as hc
from utils import get_avg_bit_len, get_histogram, get_entropy
import os
from pathlib import Path
from statistics import mean

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path = str(Path(ROOT_DIR).parent.as_posix())
VAL_RANGE = (-255, 255)


def get_image(folder):
    images = os.listdir(path + folder)
    return images


def experiments(folder, diff_option):
    entropies_diff = []
    entropies_org = []
    avg_bitlens_org = []
    avg_bitlens_diff = []
    redundancies_org = []
    redundancies_diff = []

    for image in get_image(folder):
        img = im.open(path + folder + image)
        img_org = np.asarray(img)
        img_diff = pc.predictive_encode(img, diff_option)
        img_huff_diff, decoder_diff = hc.get_Huffman_image_description(img_diff)

        img_huff_org, decoder_org = hc.get_Huffman_image_description(img_org)

        avg_bitlen_org = get_avg_bit_len(img_huff_org)
        avg_bitlen_diff = get_avg_bit_len(img_huff_diff)

        hist_org = get_histogram(img_org, VAL_RANGE)
        hist_diff = get_histogram(img_diff, VAL_RANGE)

        entropy_org = get_entropy(hist_org)
        entropy_diff = get_entropy(hist_diff)

        redundancy_org = avg_bitlen_org - entropy_org
        redundancy_diff = avg_bitlen_diff - entropy_diff

        entropies_org.append(entropy_org)
        entropies_diff.append(entropy_diff)
        avg_bitlens_org.append(avg_bitlen_org)
        avg_bitlens_diff.append(avg_bitlen_diff)
        redundancies_org.append(redundancy_org)
        redundancies_diff.append(redundancy_diff)

    mean_entropy_org = round(mean(entropies_org), 3)
    mean_entropy_diff = round(mean(entropies_diff), 3)
    mean_avg_bitlens_org = round(mean(avg_bitlens_org), 3)
    mean_avg_bitlens_diff = round(mean(avg_bitlens_diff), 3)
    mean_redundancy_org = round(mean(redundancies_org), 3)
    mean_redundancy_diff = round(mean(redundancies_diff), 3)

    return mean_entropy_org, mean_avg_bitlens_org, mean_redundancy_org, mean_entropy_diff, mean_avg_bitlens_diff, mean_redundancy_diff


if __name__ == "__main__":
    diff_options = ["upper", "left"]
    folders = ["/test_images/", "/generated_test_data/"]

    for folder in folders:
        print("/ / / / / / / / / / / / / / / / ")
        print("OBRAZY ", folder)
        print("/ / / / / / / / / / / / / / / / ")
        results = experiments(folder, "upper")
        print("OBRAZY ORYGINALNE: ")
        print("Średnia entropia ", results[0])
        print("Średnia długośc słowa kodowego ", results[1])
        print("Średnia redundancja ", results[2])
        for opt in diff_options:
            results = experiments(folder, opt)
            print("/ / / / / / / / / / / / / / / / ")
            print("OBRAZY RÓŻNICOWE ", opt, ": ")
            print("Średnia entropia ", results[3])
            print("Średnia długośc słowa kodowego ", results[4])
            print("Średnia redundancja ", results[5])