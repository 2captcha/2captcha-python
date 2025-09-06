#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest



class HcaptchaTest(AbstractTest):
    

    def test_all_params(self):
        
        
        params = {
                'sitekey' : 'f1ab2cdefa3456789012345b6c78d90e',
                'url'     : 'https://www.site.com/page/',
                }
        
        sends = {
                'method'  : 'hcaptcha',
                'sitekey' : 'f1ab2cdefa3456789012345b6c78d90e',
                'pageurl' : 'https://www.site.com/page/',
                }

        return self.send_return(sends, self.solver.hcaptcha, **params)





if __name__ == '__main__':

    unittest.main()

