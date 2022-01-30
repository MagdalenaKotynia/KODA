import unittest
import numpy as np

import huffman_tree as ht
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
            print(key_1, ':', dict_1[key_1])


if __name__ == '__main__':
    unittest.main()