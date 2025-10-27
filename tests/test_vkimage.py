#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest



class VkImage(AbstractTest):
    

    def test_all_params(self):
        
        
        params = {
                'files'     : '../examples/images/vk.jpg',
                'steps'     : '[5,4,7,7,14,22,8,3,2,7,23,22,2,8,24,5,9,20,2,5,0,6,22,4,5,11,12,12,9,6,18,3,21,18,17,7,6,'
                              '1,4,19,8,11,3,14,20,6,16,11,23,0,10,14,10,9,24,3,14,14,10,0,15,10,6,6,20,12,18,13,20,7,13,'
                              '9,22,14,24,14,17,22,0,4,6,11,10,15,18,20,0,3,6,4,23,12,15,14,18,4,2,9,5,2]',
                }
        
        sends = {
                'method'    : 'vkimage',
                'file'     : '../examples/images/vk.jpg',
                'steps'     : '[5,4,7,7,14,22,8,3,2,7,23,22,2,8,24,5,9,20,2,5,0,6,22,4,5,11,12,12,9,6,18,3,21,18,17,7,6,'
                              '1,4,19,8,11,3,14,20,6,16,11,23,0,10,14,10,9,24,3,14,14,10,0,15,10,6,6,20,12,18,13,20,7,13,'
                              '9,22,14,24,14,17,22,0,4,6,11,10,15,18,20,0,3,6,4,23,12,15,14,18,4,2,9,5,2]'
                }

        return self.send_return(sends, self.solver.vkimage, **params)





if __name__ == '__main__':

    unittest.main()

