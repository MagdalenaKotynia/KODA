from audioop import reverse
from copy import deepcopy
from hashlib import new
from logging import root
import numpy as np
import queue as q

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

def check_min_two_from_two_queues(list_1, list_2):
    """ Function checks wheather it is possible to get 2 front values from queue and then return it in sorted by items dict"""
    dict_for_compare = {}
    try:
        dict_for_compare[(0, 0)] = list_1[0]
        try:
            dict_for_compare[(0, 1)] = list_1[1]
        except IndexError:
            # print("only one element in list")
            pass
    except IndexError:
        # print("empty q_2 list")
        pass
    try:
        dict_for_compare[(1, 0)] = list_2[0]
        try:
            dict_for_compare[(1, 1)] = list_2[1]
        except IndexError:
            # print("only one element in list")
            pass
    except IndexError:
        # print("empty q_2 list")
        pass
    return {k: v for k, v in sorted(dict_for_compare.items(), key=lambda item: item[1])}


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = None
    
    def __repr__(self):
        return "Node"
    
    def __eq__(self, __other):
        if self.value == __other.value:
            return True
        else:
            return False
    
    def __lt__(self, __other):
        if self.value < __other.value:
            return True
        else:
            return False
    
    def __le__(self, __other):
        if self.value <= __other.value:
            return True
        else:
            return False
    
    def __ge__(self, __other):
        if self.value >= __other.value:
            return True
        else:
            return False
        
    def __gt__(self, __other):
        if self.value > __other.value:
            return True
        else:
            return False
    
class Leaf(Node):
    def __init__(self, frequency, input_orginal_desc):
        super().__init__(frequency)
        self.orginal_desc = input_orginal_desc
        self.bin_description = None
    
    def __repr__(self):
        return "Leaf"


class Huffman_Tree:
    def __init__(self, ordered_frequency_dict):
        self.root = None
        self.nodes = []
        self.leaves = []

        q_0 = [Leaf(freq, value) for value, freq in ordered_frequency_dict.items()]
        q_1 = []
        queues = [q_0, q_1]
        while len(queues[0]) > 1 or len(queues[1]) > 1:
            dict_from_queues = check_min_two_from_two_queues(queues[0], queues[1])
            pos_list = list(dict_from_queues)
            q_1_num, q_1_ele, q_2_num, q_2_ele = pos_list[0][0], pos_list[0][1], pos_list[1][0], pos_list[0][1]
            node_1 = queues[q_1_num].pop(q_1_ele)
            node_2 = queues[q_2_num].pop(q_2_ele)
            new_node = Node(node_1.value + node_2.value)
            node_1.parent = new_node
            node_2.parent = new_node
            if repr(node_1) == "Leaf":
                self.leaves.append(node_1)
            if repr(node_2) == "Leaf":
                self.leaves.append(node_2)
            new_node.children = [node_1, node_2]
            self.nodes.append(new_node)
            queues[1].append(new_node)
        if len(queues[0]) == 1 and len(queues[1]) == 1:
            node_1 = queues[q_1_num].pop(q_1_ele)
            node_2 = queues[q_2_num].pop(q_2_ele)
            new_node = Node(node_1.value + node_2.value)
            node_1.parent = new_node
            node_2.parent = new_node
            self.leaves.append(node_1)
            new_node.children = [node_1, node_2]
            self.nodes.append(new_node)
            self.root = new_node
        else:
            try: 
                self.root = queues[0][0]
            except IndexError:
                pass
            try:
                self.root = queues[1][0]
            except IndexError:
                pass
        self.get_leaves_binary_description()

    def __repr__(self) -> str:
        return "Huffman Tree"
    
    def determine_parent_edge_description(node):
        if node.parent.children[0] == node:
            return 0
        else:
            return 1

    def get_leaves_binary_description(self):
        for leaf in self.leaves:
            buffer = ''
            curr_node = leaf
            while curr_node != self.root:
                digit = Huffman_Tree.determine_parent_edge_description(curr_node)
                buffer += str(digit)
                curr_node = curr_node.parent
            leaf.bin_description = buffer[::-1]
        return True
    
    def get_descriptions_dict(self):
        """Function creating dictionary: orginal value as key -> bit name mask"""
        descr_dict = {}
        for leaf in self.leaves:
            descr_dict[leaf.orginal_desc] = leaf.bin_description
        
        return descr_dict

def get_Huffman_image_description(image):
    ordered_dic = get_ordered_dict(image)
    coder = Huffman_Tree(ordered_dic)
    coder_description = coder.get_descriptions_dict()
    coded_image = []
    i, j = 0, 0
    for row in image:
        coded_image.append([])
        for pix in row:
            c = coder_description[pix]
            coded_image[i].append(coder_description[pix])
        i += 1
    return coded_image, coder_description


