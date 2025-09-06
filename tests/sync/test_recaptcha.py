#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest



class RecaptchaTest(AbstractTest):
    

    def test_v2(self):
        
        params = {
                'sitekey'   : '6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                'url'       : 'https://mysite.com/page/with/recaptcha',
                'invisible' :  1,
                'action'    : 'verify',
                'datas'     : 'Crb7VsRAQaBqoaQQtHQQ'
                }
        
        sends = {
                'method'    : 'userrecaptcha',
                'googlekey' : '6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                'pageurl'   : 'https://mysite.com/page/with/recaptcha',
                'invisible': 1,
                'enterprise': 0,                
                'action'    : 'verify',
                'version'   : 'v2',
                'data-s'    : 'Crb7VsRAQaBqoaQQtHQQ'
                }

        return self.send_return(sends, self.solver.recaptcha, **params)


    def test_v3(self):
        
        params = {
                'sitekey'   : '6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                'url'       : 'https://mysite.com/page/with/recaptcha',
                'invisible' :  1,
                'action'    : 'verify',
                'version'   : 'v3',
                }
        
        sends = {
                'method'    : 'userrecaptcha',
                'googlekey' : '6Le-wvkSVVABCPBMRTvw0Q4Muexq1bi0DJwx_mJ-',
                'pageurl'   : 'https://mysite.com/page/with/recaptcha',
                'invisible' : 1,
                'enterprise': 0,
                'action'    : 'verify',
                'version'   : 'v3',
                }

        return self.send_return(sends, self.solver.recaptcha, **params)



if __name__ == '__main__':

    unittest.main()

