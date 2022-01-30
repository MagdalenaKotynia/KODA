from audioop import reverse
import numpy as np

def get_ordered_dict(image):
    """function transforming numpy image into dictionary, which items are ordered by items value"""
    pix_list = list(image.flatten())
    pix_list.sort()
    dict_to_Huff = {}
    p = None
    for item in pix_list:
        if p != item:
            p = item
            dict_to_Huff[p] = 1
        else:
            dict_to_Huff[p] += 1
    dict_to_Huff = {k: v for k, v in sorted(dict_to_Huff.items(), key=lambda item: item[1])}
    return dict_to_Huff


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None
    
class Leaf(Node):
    def __init__(self, frequency, codec_value):
        super().__init__(frequency)
        self.codec_value = codec_value

class Huffman_Tree:
    def __init__(self, ordered_frequency_dict, pointer):
        self.root  = self.__build_tree(self, ordered_frequency_dict, pointer)
        self.nodes = []
        self.leaves = []
        self.root_value = 0

    def __build_tree(self, ordered_frequency_dict, pointer):
        tree_queue = []
        for key, item in ordered_frequency_dict.items()[pointer:]:
            if self.root_value <= item:
                new_leave = Leaf(item)              
                if len(self.nodes) == 0:
                    new_node = (self.root_value + item)
                    new_node.right_child = new_leave
                    new_leave.parent = new_node
                    self.nodes.append(new_node)
                    self.leaves.append(new_leave)


