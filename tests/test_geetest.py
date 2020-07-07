#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest



class GeeTest(AbstractTest):
    

    def test_all_params(self):
        
        
        params = {
                'gt'        : 'f2ae6cadcf7886856696502e1d55e00c',
                'apiServer' : 'api-na.geetest.com',
                'challenge' : '69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC',
                'url'       : 'https://launches.endclothing.com/distil_r_captcha.html',                }
        
        sends = {
                'method'     : 'geetest',
                'gt'         : 'f2ae6cadcf7886856696502e1d55e00c',
                'api_server' : 'api-na.geetest.com',
                'challenge'  : '69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC',
                'pageurl'    : 'https://launches.endclothing.com/distil_r_captcha.html',
                }

        return self.send_return(sends, self.solver.geetest, **params)





if __name__ == '__main__':

    unittest.main()

