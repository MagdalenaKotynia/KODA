from copy import copy
import unittest
import numpy as np

import huffman_codec as ht
class TestHuffmanTree(unittest.TestCase):

    def test_get_ordered_dict(self):
        mat = np.array([[2, 2, 3, 2],
                        [1, 4, 5, 6],
                        [1, 2, 1, 2],
                        [5, 4, 3, 3]])
        
        dict_1 = ht.get_ordered_dict(mat)
        dict_2 ={
            6: 1,
            4: 2,
            5: 2,
            1: 3,
            3: 3,
            2: 5
        }

        for key_1, key_2 in zip(dict_1, dict_2):
            self.assertEqual(key_1, key_2)
            self.assertEqual(dict_1[key_1], dict_2[key_2])

    def test_check_min_two_from_two_queues(self):
        l_1 = [1, 4 , 4, 7, 8]
        l_2_0 = []
        l_2_1 = [3]
        l_2_3 = [2, 7, 10]
        
        d_1 = ht.check_min_two_from_two_queues(l_1, l_2_0)
        d_1_ = {(0, 0): 1, (0, 1): 4}
        self.assertDictEqual(d_1, d_1_)

        d_2 = ht.check_min_two_from_two_queues(l_1, l_2_1)
        d_2_ = {(0, 0): 1, (1, 0): 3, (0, 1): 4}
        self.assertDictEqual(d_2, d_2_)

        d_3 = ht.check_min_two_from_two_queues(l_1, l_2_3)
        d_3_ = {(0, 0): 1, (1, 0): 2, (0, 1): 4, (1, 1): 7}
        self.assertDictEqual(d_3, d_3_)

        ######
        l_1 = [ht.Leaf(1, 23), ht.Leaf(4, 45), ht.Leaf(7, 47)]
        l_2_1 = []

        d_1 = ht.check_min_two_from_two_queues(l_1, l_2_1)
        d_1_ = {(0, 0):l_1[0], (0, 1): l_1[1]}       
        self.assertDictEqual(d_1, d_1_)

        l_1 = [ht.Leaf(1, 23), ht.Leaf(8, 45), ht.Leaf(7, 47)]
        l_2_2 = [ht.Node(4), ht.Node(7)]

        d_2 = ht.check_min_two_from_two_queues(l_1, l_2_2)
        d_2_ = {(0, 0):l_1[0], (1, 0): l_2_2[0], (1, 1): l_2_2[1], (0, 1): l_1[1]}
        self.assertDictEqual(d_2, d_2_)
    
    def test_build_tree(self):
        decription_dict = {
            'n' : 1,
            's' : 3,
            't' : 4,
            'a' : 10,
            'i' : 12,
            'p' : 13,
            'e' : 15
        }
        huf_tree = ht.Huffman_Tree(decription_dict)
        self.assertEqual(huf_tree.root.value, 58)

if __name__ == '__main__':
    unittest.main()