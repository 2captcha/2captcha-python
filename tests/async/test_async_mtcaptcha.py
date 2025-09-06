#!/usr/bin/env python3

import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncMTCaptchaTest(AsyncAbstractTest):
    def test_all_params(self):
        params = {
            'sitekey': 'MTPublic-KzqLY1cKH',
            'url': 'https://2captcha.com/demo/mtcaptcha',
        }

        sends = {
            'method': 'mt_captcha',
            'sitekey': 'MTPublic-KzqLY1cKH',
            'pageurl': 'https://2captcha.com/demo/mtcaptcha',
        }

        self.send_return(sends, self.solver.mtcaptcha, **params)


if __name__ == '__main__':
    unittest.main()
