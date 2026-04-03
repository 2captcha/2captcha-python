#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest


class AltchaTest(AbstractTest):

    def test_all_params(self):
        params = {
            'pageurl': 'https://mysite.com/page/with/altcha',
            'challenge_json': '{"algorithm":"SHA-256","challenge":"a4c9d8e7f1b23a6c...",..."signature":"7b3e2a9d5c8f1046e2d91c3a..."}',
            'challenge_url': 'https://example/altcha'
        }

        sends = {
            'method': 'altcha',
            'pageurl': 'https://mysite.com/page/with/altcha',
            'challenge_json': '{"algorithm":"SHA-256","challenge":"a4c9d8e7f1b23a6c...",..."signature":"7b3e2a9d5c8f1046e2d91c3a..."}',
            'challenge_url': 'https://example/altcha'
        }

        return self.send_return(sends, self.solver.altcha, **params)


if __name__ == '__main__':
    unittest.main()