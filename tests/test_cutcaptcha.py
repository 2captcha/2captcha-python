#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest


class CutcaptchaTest(AbstractTest):

    def test_all_params(self):
        params = {
            'misery_key': 'ad52c87af17e2ec09b8d918c9f00416b1cb8c320',
            'apikey':     'SAs61IAI',
            'url':        'https://www.site.com/page/',
        }

        sends = {
            'method':     'cutcaptcha',
            'api_key':    'SAs61IAI',
            'misery_key': 'ad52c87af17e2ec09b8d918c9f00416b1cb8c320',
            'pageurl':    'https://www.site.com/page/',
        }

        return self.send_return(sends, self.solver.cutcaptcha, **params)


if __name__ == '__main__':
    unittest.main()