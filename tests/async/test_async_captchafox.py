#!/usr/bin/env python3

import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncCaptchaFox(AsyncAbstractTest):
    def test_all_params(self):
        params = {
                'sitekey': 'sk_ILKWNruBBVKDOM7dZs50WPNUuCUKR',
                'pageurl': 'https://mysite.com/page/with/captchafox',
                'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'proxy': {'type': 'HTTPS',
                          'uri': 'login:password@IP_address:PORT'}
        }

        sends = {
                'method'    : 'captchafox',
                'sitekey': 'sk_ILKWNruBBVKDOM7dZs50WPNUuCUKR',
                'pageurl': 'https://mysite.com/page/with/captchafox',
                'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'proxytype': 'HTTPS',
                'proxy': 'login:password@IP_address:PORT'
        }

        self.send_return(sends, self.solver.captchafox, **params)


if __name__ == '__main__':
    unittest.main()
