#!/usr/bin/env python3

import unittest

try:
    from .abstract import AbstractTest
except ImportError:
    from abstract import AbstractTest


class CaptchaImperva(AbstractTest):

    def test_all_params(self):
        params = {
            'pageurl': 'https://example.com/login',
            'incapsula_script_url': '/_Incapsula_Resource?SWUDNSAI=31&xinfo=1',
            'incapsula_cookies': 'visid_incap_123456=sample; incap_ses_123_123456=sample',
            'proxy': {'type': 'HTTP',
                      'uri': 'login:password@IP_address:PORT'},
            'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'reese84_url_endpoint': 'https://example.com/_Incapsula_Resource?reese84=1',
        }

        sends = {
            'method': 'incapsula',
            'pageurl': 'https://example.com/login',
            'incapsula_script_url': '/_Incapsula_Resource?SWUDNSAI=31&xinfo=1',
            'incapsula_cookies': 'visid_incap_123456=sample; incap_ses_123_123456=sample',
            'proxytype': 'HTTP',
            'proxy': 'login:password@IP_address:PORT',
            'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'reese84_url_endpoint': 'https://example.com/_Incapsula_Resource?reese84=1',
        }

        return self.send_return(sends, self.solver.imperva, **params)

    def test_required_params(self):
        params = {
            'pageurl': 'https://example.com/login',
            'incapsula_script_url': '/_Incapsula_Resource?SWUDNSAI=31&xinfo=1',
            'incapsula_cookies': 'visid_incap_123456=sample; incap_ses_123_123456=sample',
            'proxy': {'type': 'HTTP',
                      'uri': 'login:password@IP_address:PORT'},
        }

        sends = {
            'method': 'incapsula',
            'pageurl': 'https://example.com/login',
            'incapsula_script_url': '/_Incapsula_Resource?SWUDNSAI=31&xinfo=1',
            'incapsula_cookies': 'visid_incap_123456=sample; incap_ses_123_123456=sample',
            'proxytype': 'HTTP',
            'proxy': 'login:password@IP_address:PORT',
        }

        return self.send_return(sends, self.solver.imperva, **params)


if __name__ == '__main__':
    unittest.main()
