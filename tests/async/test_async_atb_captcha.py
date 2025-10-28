#!/usr/bin/env python3

import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncAtbCaptchaTest(AsyncAbstractTest):
    def test_all_params(self):
        params = {
            'app_id': 'af25e409b33d722a95e56a230ff8771c',
            'api_server': 'https://cap.aisecurius.com',
            'url': 'http://mysite.com/'
        }

        sends = {
            'method': 'atb_captcha',
            'app_id': 'af25e409b33d722a95e56a230ff8771c',
            'api_server': 'https://cap.aisecurius.com',
            'pageurl': 'http://mysite.com/'
        }

        self.send_return(sends, self.solver.atb_captcha, **params)


if __name__ == '__main__':
    unittest.main()
