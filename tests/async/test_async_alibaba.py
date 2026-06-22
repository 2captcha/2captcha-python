#!/usr/bin/env python3

import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncAlibaba(AsyncAbstractTest):
    def test_all_params(self):
        params = {
                'pageurl': 'https://www.example.com',
                'scene_id': 'abc123xyz4',
                'prefix': 'dlw3kug',
                'user_id': 'Abc123Def456Ghi789Jkl012Mno345Pqr678Stu901=',
                'user_user_id': 'Xyz987Abc654Def321Ghi098Jkl765Mno432Pqr109=',
                'verify_type': '1.0',
                'region': 'sgp',
                'user_certify_id': 'abc123def456ghi789jkl012mno345pq',
                'api_get_lib': 'https://o.example.com/captcha-frontend/aliyunCaptcha/AliyunCaptcha.js?t=2041',
                'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
                'proxy': {'type': 'HTTP',
                          'uri': 'login:password@IP_address:PORT'}
        }

        sends = {
                'method': 'alibaba',
                'pageurl': 'https://www.example.com',
                'scene_id': 'abc123xyz4',
                'prefix': 'dlw3kug',
                'user_id': 'Abc123Def456Ghi789Jkl012Mno345Pqr678Stu901=',
                'user_user_id': 'Xyz987Abc654Def321Ghi098Jkl765Mno432Pqr109=',
                'verify_type': '1.0',
                'region': 'sgp',
                'user_certify_id': 'abc123def456ghi789jkl012mno345pq',
                'api_get_lib': 'https://o.example.com/captcha-frontend/aliyunCaptcha/AliyunCaptcha.js?t=2041',
                'useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
                'proxytype': 'HTTP',
                'proxy': 'login:password@IP_address:PORT'
        }

        self.send_return(sends, self.solver.alibaba, **params)


if __name__ == '__main__':
    unittest.main()
