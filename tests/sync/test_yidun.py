#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest


class CaptchaYidun(AbstractTest):

    def test_all_params(self):
        params = {
            'sitekey': '6b4d7e0c4f5a4c7db2f3a1e8c9d6f123',
            'pageurl': 'https://mysite.com/page/with/yadun',
            'yidun_get_lib': 'https://cstaticdun.126.net/load.min.js',
            'yidun_api_server_subdomain': 'c.dun.163.com',
            'challenge': '8f7e4d2c1b9a6f5e3d4c7b8a9e0f123456789abcdef123456789abcdef1234',
            'hcg': '9a217825f3dcfac3d34e551e93819d610dec931e5e2a2236edf0e1f3f320c191',
            'hct': 1751469954806,
            'useragent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/148.0.0.0 Safari/537.36",
            'proxy': {'type': 'HTTP',
                      'uri': 'login:password@IP_address:PORT'}
        }

        sends = {
            'method': 'yidun',
            'sitekey': '6b4d7e0c4f5a4c7db2f3a1e8c9d6f123',
            'pageurl': 'https://mysite.com/page/with/yadun',
            'yidun_get_lib': 'https://cstaticdun.126.net/load.min.js',
            'yidun_api_server_subdomain': 'c.dun.163.com',
            'challenge': '8f7e4d2c1b9a6f5e3d4c7b8a9e0f123456789abcdef123456789abcdef1234',
            'hcg': '9a217825f3dcfac3d34e551e93819d610dec931e5e2a2236edf0e1f3f320c191',
            'hct': 1751469954806,
            'useragent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/148.0.0.0 Safari/537.36",
            'proxytype': 'HTTP',
            'proxy': 'login:password@IP_address:PORT'
        }

        return self.send_return(sends, self.solver.yidun, **params)


if __name__ == '__main__':
    unittest.main()

