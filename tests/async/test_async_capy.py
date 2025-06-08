#!/usr/bin/env python3

import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncCapyTest(AsyncAbstractTest):
    def test_all_params(self):
        params = {
            'sitekey': 'PUZZLE_Abc1dEFghIJKLM2no34P56q7rStu8v',
            'url': 'http://mysite.com/',
        }

        sends = {
            'method': 'capy',
            'captchakey': 'PUZZLE_Abc1dEFghIJKLM2no34P56q7rStu8v',
            'pageurl': 'http://mysite.com/',
        }

        self.send_return(sends, self.solver.capy, **params)


if __name__ == '__main__':
    unittest.main()
