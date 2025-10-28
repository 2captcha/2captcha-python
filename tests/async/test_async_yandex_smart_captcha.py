#!/usr/bin/env python3

import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncYandexSmartCaptchaTest(AsyncAbstractTest):
    def test_all_params(self):
        params = {
            'sitekey': 'FEXfAbHQsToo97VidNVk3j4dC74nGW1DgdPpL4O',
            'url': 'https://www.site.com/page/',
        }

        sends = {
            'method': 'yandex',
            'sitekey': 'FEXfAbHQsToo97VidNVk3j4dC74nGW1DgdPpL4O',
            'pageurl': 'https://www.site.com/page/',
        }

        self.send_return(sends, self.solver.yandex_smart, **params)


if __name__ == '__main__':
    unittest.main()
