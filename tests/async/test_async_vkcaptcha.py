#!/usr/bin/env python3

import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncVkCaptcha(AsyncAbstractTest):
    def test_all_params(self):
        params = {
                'redirect_uri': 'https://id.vk.ru/not_robot_captcha?domain=vk.com&session_token=eyJhbGciOiJBMjU2R0NN...',
                'userAgent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.4348.100 Yandex/23.6.1.1107 Yowser/2.5 Safari/537.36',
                'proxy': {'type': 'HTTPS',
                          'uri': 'login:password@IP_address:PORT'}
        }

        sends = {
                'method'    : 'vkcaptcha',
                'redirect_uri': 'https://id.vk.ru/not_robot_captcha?domain=vk.com&session_token=eyJhbGciOiJBMjU2R0NN...',
                'useragent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.4348.100 Yandex/23.6.1.1107 Yowser/2.5 Safari/537.36',
                'proxytype': 'HTTPS',
                'proxy': 'login:password@IP_address:PORT'
        }

        self.send_return(sends, self.solver.vkcaptcha, **params)


if __name__ == '__main__':
    unittest.main()
