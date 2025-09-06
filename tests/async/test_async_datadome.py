#!/usr/bin/env python3

import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncDatadomeTest(AsyncAbstractTest):
    def test_all_params(self):
        params = {
            'captcha_url': 'https://geo.captcha-delivery.com/captcha/?initialCid=AHrlqAAAAAMAZirHgKBVrxwAsVuKlQ%3D%3D&c',
            'pageurl': 'https://mysite.com/page/with/datadome',
            'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'proxy': {'type': 'HTTP', 'uri': 'login:password@IP_address:PORT'}
        }

        sends = {
            'method': 'datadome',
            'captcha_url': 'https://geo.captcha-delivery.com/captcha/?initialCid=AHrlqAAAAAMAZirHgKBVrxwAsVuKlQ%3D%3D&c',
            'pageurl': 'https://mysite.com/page/with/datadome',
            'userAgent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'proxy': 'login:password@IP_address:PORT',
            'proxytype': 'HTTP'
        }

        self.send_return(sends, self.solver.datadome, **params)


if __name__ == '__main__':
    unittest.main()
