import numpy as np
import sys
import PIL
import matplotlib.pyplot as plt
from PIL import Image as im
import modules.predictive_coder as pc
import modules.data_generator as gen
import modules.huffman_codec as hc
from modules.utils import get_avg_bit_len


def main(argv):
    argumentList = argv
    img_1 = im.open("my_test_images/dog.png")
    img_org = np.asarray(img_1)
    img_predictive = pc.predictive_encode(img_1, "upper")
    img_huff, decoder = hc.get_Huffman_image_description(img_predictive)

    img_huff_org, decoder_org = hc.get_Huffman_image_description(img_org)

    print("ok")
    print(type(img_huff))
    #print(img_huff)
    print(get_avg_bit_len(img_huff))
    print(get_avg_bit_len(img_huff_org))
    print(type(img_1))


if __name__ == "__main__":
    main(sys.argv[1:])
