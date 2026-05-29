#!/usr/bin/env python3

import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncBinance(AsyncAbstractTest):
    def test_all_params(self):
        params = {
                'sitekey': 'register',
                'pageurl': 'https://mysite.com/page/with/binance',
                'validate_id': 'e20c622fa9384952832fc1c2a6b75c0a',
                'useragent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
                'proxy': {'type': 'HTTP',
                          'uri': 'login:password@IP_address:PORT'}
        }

        sends = {
                'method': 'binance',
                'sitekey': 'register',
                'pageurl': 'https://mysite.com/page/with/binance',
                'validate_id': 'e20c622fa9384952832fc1c2a6b75c0a',
                'useragent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
                'proxytype': 'HTTP',
                'proxy': 'login:password@IP_address:PORT'
        }

        self.send_return(sends, self.solver.binance, **params)


if __name__ == '__main__':
    unittest.main()
