#!/usr/bin/env python3

import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncLeminTest(AsyncAbstractTest):
    def test_all_params(self):
        params = {
            'captcha_id': 'CROPPED_1abcd2f_a1234b567c890d12ef3a456bc78d901d',
            'div_id': 'lemin-cropped-captcha',
            'api_server': 'https://api.leminnow.com/',
            'url': 'http://mysite.com/',
        }

        sends = {
            'method': 'lemin',
            'captcha_id': 'CROPPED_1abcd2f_a1234b567c890d12ef3a456bc78d901d',
            'div_id': 'lemin-cropped-captcha',
            'api_server': 'https://api.leminnow.com/',
            'pageurl': 'http://mysite.com/',
        }

        self.send_return(sends, self.solver.lemin, **params)


if __name__ == '__main__':
    unittest.main()
