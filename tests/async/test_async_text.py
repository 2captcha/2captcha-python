#!/usr/bin/env python3
import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncTextTest(AsyncAbstractTest):
    def test_only_text(self):
        sends = {
            'method': 'post',
            'textcaptcha': 'Today is monday?',
        }

        self.send_return(sends,
                         self.solver.text,
                         text='Today is monday?')

    def test_all_params(self):
        params = {
            'text': 'Today is monday?',
            'lang': 'en',
        }

        sends = {
            'method': 'post',
            'textcaptcha': 'Today is monday?',
            'lang': 'en',
        }

        self.send_return(sends, self.solver.text, **params)


if __name__ == '__main__':
    unittest.main()
