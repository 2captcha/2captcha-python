#!/usr/bin/env python3
import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest


class TextTest(AbstractTest):
    def test_only_text(self):

        sends = {
            'method': 'post',
            'textcaptcha': 'Today is monday?',
        }

        return self.send_return(sends,
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

        return self.send_return(sends, self.solver.text, **params)


if __name__ == '__main__':

    unittest.main()
