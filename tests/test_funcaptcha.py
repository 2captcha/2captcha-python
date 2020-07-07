#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest



class FuncaptchaTest(AbstractTest):
    

    def test_all_params(self):
        
        
        params = {
                'sitekey'   : '69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC',
                'url'       : 'https://mysite.com/page/with/funcaptcha',
                'surl'      : 'https://client-api.arkoselabs.com',
                'userAgent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                'data'      : {'anyKey' : 'anyStringValue'},
                }
        
        sends = {
                'method'    : 'funcaptcha',
                'publickey' : '69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC',
                'pageurl'   : 'https://mysite.com/page/with/funcaptcha',
                'surl'      : 'https://client-api.arkoselabs.com',
                'userAgent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                'data'      : {'anyKey' : 'anyStringValue'},
                }

        return self.send_return(sends, self.solver.funcaptcha, **params)





if __name__ == '__main__':

    unittest.main()

