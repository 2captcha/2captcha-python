#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest


class CaptchaBasilisk(AbstractTest):

    def test_all_params(self):
        params = {
            'pageurl': 'https://example.com/login',
            'sitekey': 'b7890h...19fb2600897',
            'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'proxy': {'type': 'HTTP',
                      'uri': 'login:password@IP_address:PORT'}
        }

        sends = {
            'method': 'basilisk',
            'pageurl': 'https://example.com/login',
            'sitekey': 'b7890h...19fb2600897',
            'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'proxytype': 'HTTP',
            'proxy': 'login:password@IP_address:PORT'
        }

        return self.send_return(sends, self.solver.basilisk, **params)


if __name__ == '__main__':
    unittest.main()
