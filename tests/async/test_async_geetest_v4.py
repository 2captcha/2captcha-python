#!/usr/bin/env python3

import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncGeeTestV4Test(AsyncAbstractTest):
    def test_all_params(self):
        params = {
            'captcha_id': 'e392e1d7fd421dc63325744d5a2b9c73',
            'url': 'https://2captcha.com/demo/geetest-v4',
        }

        sends = {
            'method': 'geetest_v4',
            'captcha_id': 'e392e1d7fd421dc63325744d5a2b9c73',
            'pageurl': 'https://2captcha.com/demo/geetest-v4',
        }

        self.send_return(sends, self.solver.geetest_v4, **params)


if __name__ == '__main__':
    unittest.main()
