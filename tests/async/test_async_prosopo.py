#!/usr/bin/env python3

import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncProsopo(AsyncAbstractTest):
    def test_all_params(self):
        params = {
                'sitekey': '5EZVvsHMrKCFKp5NYNoTyDjTjetoVo1Z4UNNbTwJf1GfN6Xm',
                'pageurl': 'https://www.twickets.live/',
        }

        sends = {
                'method'    : 'prosopo',
                'sitekey': '5EZVvsHMrKCFKp5NYNoTyDjTjetoVo1Z4UNNbTwJf1GfN6Xm',
                'pageurl': 'https://www.twickets.live/',
        }

        self.send_return(sends, self.solver.prosopo, **params)


if __name__ == '__main__':
    unittest.main()
