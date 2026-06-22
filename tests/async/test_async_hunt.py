#!/usr/bin/env python3

import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncHunt(AsyncAbstractTest):
    def test_all_params(self):
        params = {
                'pageurl': 'https://example.com/page-with-hunt',
                'api_get_lib': 'https://example.com/hd-api/external/apps/app-id/api.js',
                'data': 'META_TOKEN_VALUE',
                'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
                'proxy': {'type': 'HTTP',
                          'uri': 'login:password@IP_address:PORT'}
        }

        sends = {
                'method': 'hunt',
                'pageurl': 'https://example.com/page-with-hunt',
                'api_get_lib': 'https://example.com/hd-api/external/apps/app-id/api.js',
                'data': 'META_TOKEN_VALUE',
                'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
                'proxytype': 'HTTP',
                'proxy': 'login:password@IP_address:PORT'
        }

        self.send_return(sends, self.solver.hunt, **params)


if __name__ == '__main__':
    unittest.main()
