#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest


class CybersiaraTest(AbstractTest):

    def test_all_params(self):
        params = {
            'master_url_id': 'tpjOCKjjpdzv3d8Ub2E9COEWKt1vl1Mv',
            'pageurl': 'https://demo.mycybersiara.com/',
            'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        }

        sends = {
            'method': 'cybersiara',
            'master_url_id': 'tpjOCKjjpdzv3d8Ub2E9COEWKt1vl1Mv',
            'pageurl': 'https://demo.mycybersiara.com/',
            'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        }

        return self.send_return(sends, self.solver.cybersiara, **params)


if __name__ == '__main__':
    unittest.main()

