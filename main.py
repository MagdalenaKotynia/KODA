from argparse import ArgumentTypeError
import imp
from msilib.schema import Error
import numpy as np
import sys
import PIL
import matplotlib.pyplot as plt
from PIL import Image as im
import modules.predictive_coder as pc
import modules.data_generator as gen
import modules.huffman_codec as hc
import modules.operations as op
from modules.utils import get_avg_bit_len


def main(argv):
    argumentList = argv
    # img_huff, encoder = op.encode_image("my_test_images/dog.png", 'u')
    # op.write_coded_image(img_huff, encoder, "dog") 
    decoder, data = op.read_image(image_name="dog")
    decoded_img = op.decode_image(decoder, data)
    plt.imshow(decoded_img)
    plt.title("Image from encoded data")
    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
