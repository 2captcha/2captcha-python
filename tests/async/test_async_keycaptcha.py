#!/usr/bin/env python3

import unittest

try:
    from .abstract_async import AsyncAbstractTest
except ImportError:
    from abstract_async import AsyncAbstractTest


class AsyncKeyCaptchaTest(AsyncAbstractTest):
    def test_all_params(self):
        params = {
            's_s_c_user_id': 10,
            's_s_c_session_id': '493e52c37c10c2bcdf4a00cbc9ccd1e8',
            's_s_c_web_server_sign': '9006dc725760858e4c0715b835472f22-pz-',
            's_s_c_web_server_sign2': '2ca3abe86d90c6142d5571db98af6714',
            'url': 'https://www.keycaptcha.ru/demo-magnetic/',
        }

        sends = {
            'method': 'keycaptcha',
            's_s_c_user_id': 10,
            's_s_c_session_id': '493e52c37c10c2bcdf4a00cbc9ccd1e8',
            's_s_c_web_server_sign': '9006dc725760858e4c0715b835472f22-pz-',
            's_s_c_web_server_sign2': '2ca3abe86d90c6142d5571db98af6714',
            'pageurl': 'https://www.keycaptcha.ru/demo-magnetic/',
        }

        self.send_return(sends, self.solver.keycaptcha, **params)


if __name__ == '__main__':
    unittest.main()
