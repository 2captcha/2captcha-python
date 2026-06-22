#!/usr/bin/env python3

import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncTspd(AsyncAbstractTest):
    def test_all_params(self):
        params = {
                'pageurl': 'https://example.com/login',
                'tspd_cookie': 'TS386a400d029=082670...010245; TS386a400d078=082670...dbb3b0c',
                'html_page_base64': 'PCFET0NUWVBFIGh0bWw+...',
                'proxy': {'type': 'HTTP',
                          'uri': 'login:password@IP_address:PORT'},
                'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        }

        sends = {
                'method': 'tspd',
                'pageurl': 'https://example.com/login',
                'tspd_cookie': 'TS386a400d029=082670...010245; TS386a400d078=082670...dbb3b0c',
                'html_page_base64': 'PCFET0NUWVBFIGh0bWw+...',
                'proxytype': 'HTTP',
                'proxy': 'login:password@IP_address:PORT',
                'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        }

        self.send_return(sends, self.solver.tspd, **params)


if __name__ == '__main__':
    unittest.main()
