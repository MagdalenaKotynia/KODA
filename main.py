import numpy as np
import sys
import PIL
import matplotlib.pyplot as plt
from PIL import Image as im
import modules.predictive_coder as pc
import modules.data_generator as gen
import modules.huffman_codec as hc


def main(argv):
    argumentList = argv
    img_1 = im.open("test_images/dog.png")
    img_predictive = pc.predictive_encode(img_1, "upper")
    img_huff, decoder  = hc.get_Huffman_image_description(img_predictive)
    print("ok")

if __name__ == "__main__":
    main(sys.argv[1:])
