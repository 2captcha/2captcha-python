#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest


class MTCaptchaTest(AbstractTest):

    def test_all_params(self):
        params = {
            'sitekey': 'MTPublic-KzqLY1cKH',
            'url':     'https://2captcha.com/demo/mtcaptcha',
        }

        sends = {
            'method':  'mt_captcha',
            'sitekey': 'MTPublic-KzqLY1cKH',
            'pageurl': 'https://2captcha.com/demo/mtcaptcha',
        }

        return self.send_return(sends, self.solver.mtcaptcha, **params)


if __name__ == '__main__':
    unittest.main()
