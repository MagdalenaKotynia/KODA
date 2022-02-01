from argparse import ArgumentTypeError
from turtle import width
from xml.dom.minidom import Element
import numpy as np
from PIL import Image as im
import matplotlib.pyplot as plt
import json

import modules.predictive_coder as pc
import modules.huffman_codec as hc
from modules.utils import get_avg_bit_len

def encode_image(image_name, pred_flag):
    img = im.open(image_name)
    img_org = np.asarray(img)
    if pred_flag == 'u':
        img_predictive = pc.predictive_encode(img, "upper")
    elif pred_flag == 'm':
        img_predictive = pc.predictive_encode(img, "median")
    elif pred_flag == 'l':
        img_predictive = pc.predictive_encode(img, "left")
    else:
        raise ArgumentTypeError
    print("Image predictive encoded")
    img_huff, huf_decoder = hc.get_Huffman_image_description(img_predictive)
    encoder = {
               "predictive encoding mehod": pred_flag,
               "huffman dict": huf_decoder,
               "height": img_org.shape[0],
               "width" : img_org.shape[1]
               }
    print("Image encoded with Huffman algorithm")
    print(get_avg_bit_len(img_huff))
    return img_huff, encoder

def write_coded_image(img_huff, encoder, image_name="default"):
    with open(f'coder_{image_name}.json', 'w', encoding='utf-8') as f:
        json.dump(encoder, f, ensure_ascii=False, indent=4)
    print("Encoder saved")
    with open(f'encoded_data_{image_name}.txt', 'w') as f:
        for row in img_huff:
            for item in row:
                f.write(f"{item}\n")
    print("Encoded data saved")

def read_image(image_name="default"):
    try:
        with open(f'coder_{image_name}.json', 'r') as f:
            decoder = json.load(f)
        print("image decoder uploaded")
    except FileNotFoundError:
        print("Dictonary with data not found")
    try:
        with open(f'encoded_data_{image_name}.txt', 'r') as f:
            data = [line.strip() for line in f]
        print("image data uploaded")
    except:
        print("Data file not found")
    
    return decoder, data

def decode_image(decoder, data):
    width, height = int(decoder["width"]), int(decoder["height"])
    huff_decoder, pred_flag = decoder["huffman dict"], decoder["predictive encoding mehod"]
    inv_huff_dict = {v: k for k, v in huff_decoder.items()}
    pred_image = np.array([float(inv_huff_dict[item]) for item in data])
    pred_image = np.reshape(pred_image, (height, width))
    print(pred_image.shape)
    if pred_flag == 'u':
        img = pc.predictive_decode(pred_image, "upper")
    elif pred_flag == 'm':
        img = pc.predictive_decode(pred_image, "median")
    elif pred_flag == 'l':
        img = pc.predictive_decode(pred_image, "left")
    print("image decoded")
    return img