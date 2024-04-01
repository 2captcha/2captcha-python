#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest


class FriendlyCaptchaTest(AbstractTest):

    def test_all_params(self):
        params = {
            'sitekey': 'FCMGEMUD2KTDSQ5H',
            'url':     'https://friendlycaptcha.com/demo',
        }

        sends = {
            'method':  'friendly_captcha',
            'sitekey': 'FCMGEMUD2KTDSQ5H',
            'pageurl': 'https://friendlycaptcha.com/demo',
        }

        return self.send_return(sends, self.solver.friendly_captcha, **params)


if __name__ == '__main__':
    unittest.main()