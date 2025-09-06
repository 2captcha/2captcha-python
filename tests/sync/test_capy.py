#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest



class CapyTest(AbstractTest):
    

    def test_all_params(self):
        
        
        params = {
                 'sitekey' : 'PUZZLE_Abc1dEFghIJKLM2no34P56q7rStu8v',
                 'url'     : 'http://mysite.com/',
                }
        
        sends = {
                'method'     : 'capy',
                'captchakey' : 'PUZZLE_Abc1dEFghIJKLM2no34P56q7rStu8v',
                'pageurl'    : 'http://mysite.com/',
                }

        return self.send_return(sends, self.solver.capy, **params)





if __name__ == '__main__':

    unittest.main()

