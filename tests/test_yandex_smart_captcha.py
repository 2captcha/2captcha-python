#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest


class YandexSmartCaptchaTest(AbstractTest):

    def test_all_params(self):
        params = {
            'sitekey': 'FEXfAbHQsToo97VidNVk3j4dC74nGW1DgdxjtNB9',
            'url':     'https://captcha-api.yandex.ru/demo',
        }

        sends = {
            'method':  'yandex',
            'sitekey': 'FEXfAbHQsToo97VidNVk3j4dC74nGW1DgdxjtNB9',
            'pageurl': 'https://captcha-api.yandex.ru/demo',
        }

        return self.send_return(sends, self.solver.yandex_smart, **params)


if __name__ == '__main__':
    unittest.main()